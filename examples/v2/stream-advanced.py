import csv
import sys
from datetime import datetime
from boonamber import AmberV2Client, ApiException, float_list_to_csv_string
import boonamber

"""Demonstrates a streaming use case in which we read continuously
   from a CSV file, inference the data line by line, and print results.
"""


class AmberStream:
    def __init__(self, model_id=None, label='amber.sdk.example.v2:advanced-default', model_config=None):

        """
        Initializes the AmberStream example class.
        :param model_id: The model_id to be used by AmberStream.  If model_id is None, then a sensor is created
        """
        self.data = []
        self.sample_cnt = 0
        self.model_id = model_id
        self.label = label
        self.config = model_config

        try:
            self.amber = AmberV2Client.from_license_file()
            if model_id is None:
                param = boonamber.PostModelRequest(label=self.label)
                model_result = self.amber.post_model(param)
                self.model_id = model_result.id
                print("created model {}".format(self.model_id))
            else:
                print("using model {}".format(self.model_id))

            config_result = self.amber.post_config(model_id=self.model_id, body=model_config)
            print("{} config: {}".format(self.model_id, config_result))
        except ApiException as e:
            print(e)
            sys.exit(1)

    def do_analytics(self):
        """
        Run analytics based on self.data and provide example of formatted results
        :return: None
        """
        self.sample_cnt += len(self.data)
        d1 = datetime.now()
        # TODO: convert float array to csv string as we don't yet have float array handling built into v2
        data_csv = float_list_to_csv_string(self.data)
        results = self.amber.post_data(self.model_id, data=data_csv, save_image=True)
        d2 = datetime.now()
        delta = (d2 - d1).microseconds / 1000
        status = results.status
        print("State: {}({}%), inferences: {}, clusters: {}, samples: {}, duration: {}".format(
            status.state, status.progress, status.sample_count, status.cluster_count, self.sample_cnt, delta))
        analytics = results.analytics
        if status.message is not None:
            print("Message: {}".format(status.message))

        if status.state in ["Learning", "Monitoring"]:
            for key in analytics.attribute_map.keys():
                analytic = getattr(analytics, key)
                if type(analytic[0]) is float:
                    analytic_pretty = ','.join("{:.6f}".format(a) for a in analytic)
                else:
                    analytic_pretty = ','.join("{}".format(a) for a in analytic)
                print("{}: {} ".format(key, analytic_pretty))

        neg_ids = [num for num in getattr(analytics, 'id') if num < 0]
        if len(neg_ids) > 0:
            print("Root Cause:")
            rc = self.amber.get_root_cause(self.model_id, id_list=neg_ids)
            root_cause_pretty = ['\t' + str(id) + ': ' + ','.join("{:.6f}".format(a) for a in root) for (root, id) in
                                 zip(rc, neg_ids)]
            for root in root_cause_pretty:
                print(root)
        self.data = []

    def stream_csv(self, csv_file, samples_per_request=5):
        """
        Given a path to a csv file, stream data to Amber in sizes specified by batch_size
        :param csv_file: Path to csv file
        :param samples_per_request: number of samples per streaming request
        :return: None
        """
        # Open csv data file and begin streaming

        batch_size = samples_per_request * len(self.config.features)
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            self.data = []
            self.sample_cnt = 0
            for row in csv_reader:
                for d in row:
                    self.data.append(float(d))
                    if len(self.data) == batch_size:
                        try:
                            self.do_analytics()
                        except Exception as e:
                            print(e)
                            sys.exit(1)

            # send the remaining partial batch (if any)
            if len(self.data) > 0:
                self.do_analytics()


# construct a configuration
streaming_window = 25
percent_variation = None
feature = boonamber.FeatureConfig()
features = [feature]
training = None     # boonamber.TrainingConfig
autotuning = None   # boonamber.AutotuneConfig
config = boonamber.PostConfigRequest(streaming_window=streaming_window, percent_variation=percent_variation,
                                    features=features, training=training, autotuning=autotuning)

# init the streamer
streamer = AmberStream(model_id=None, label='amber.sdk.example.v2:streaming-advanced', model_config=config)

streamer.stream_csv('output_current.csv', samples_per_request=10)
