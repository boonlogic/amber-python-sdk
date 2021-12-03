import csv
import sys
from datetime import datetime
from boonamber import AmberClient, AmberCloudError

"""Demonstrates a streaming use case in which we read continuously
   from a CSV file, inference the data line by line, and print results.
"""


class AmberStream:

    def __init__(self, sensor_id=None, label=None, feature_count=1, streaming_window_size=25, samples_to_buffer=10000,
                 anomaly_history_window=10000, learning_rate_numerator=10, learning_rate_denominator=10000,
                 learning_max_clusters=1000, learning_max_samples=1000000, features=None):
        """
        Initializes the AmberStream example class.
        :param sensor_id: The sensor_id to be used by AmberStream.  If sensor_id is None, then a sensor is created
        """
        self.data = []
        self.sample_cnt = 0
        self.sensor_id = sensor_id
        self.label = label
        self.feature_count = feature_count
        self.streaming_window_size = streaming_window_size
        self.samples_to_buffer = samples_to_buffer
        self.anomaly_history_window = anomaly_history_window
        self.learning_max_clusters = learning_max_clusters
        self.learning_max_samples = learning_max_samples
        self.learning_rate_numerator = learning_rate_numerator
        self.learning_rate_denominator = learning_rate_denominator
        self.features = features

        try:
            self.amber = AmberClient()
            if sensor_id is None:
                self.sensor_id = self.amber.create_sensor(label=self.label)
                print("created sensor {}".format(self.sensor_id))
            else:
                print("using sensor {}".format(self.sensor_id))

            config = self.amber.configure_sensor(self.sensor_id, feature_count=self.feature_count,
                                                 streaming_window_size=self.streaming_window_size,
                                                 samples_to_buffer=self.samples_to_buffer,
                                                 anomaly_history_window=self.anomaly_history_window,
                                                 learning_max_clusters=self.learning_max_clusters,
                                                 learning_max_samples=self.learning_max_samples,
                                                 learning_rate_numerator=self.learning_rate_numerator,
                                                 learning_rate_denominator=self.learning_rate_denominator,
                                                 features=self.features)
 
            print("{} config: {}".format(self.sensor_id, config))
        except AmberCloudError as e:
            print(e)
            sys.exit(1)

    def do_analytics(self):
        """
        Run analytics based on self.data and provide example of formatted results
        :return: None
        """
        self.sample_cnt += len(self.data)
        d1 = datetime.now()
        results = self.amber.stream_sensor(self.sensor_id, self.data, False)
        d2 = datetime.now()
        delta = (d2 - d1).microseconds / 1000
        print("State: {}({}%), inferences: {}, clusters: {}, samples: {}, duration: {}".format(
            results['state'], results['progress'], results['totalInferences'], results['clusterCount'], self.sample_cnt,
            delta))
        print("Message: {}".format(results['message']))
        for analytic in ['ID', 'SI', 'RI', 'AD', 'AH', 'AM', 'AW']:
            if analytic == 'AM':
                analytic_pretty = ','.join("{:.6f}".format(a) for a in results[analytic])
            else:
                analytic_pretty = ','.join("{}".format(a) for a in results[analytic])
            print("{}: {} ".format(analytic, analytic_pretty))

        neg_ids = [num for num in results['ID'] if num < 0]
        if len(neg_ids) > 0:
            print("Root Cause:")
            rc = self.amber.get_root_cause(self.sensor_id, id_list=neg_ids)
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

        batch_size = samples_per_request * self.feature_count
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


# Specifying sensor_id will use existing over creating a new one
features = [
    {
       "minVal": 0,
       "maxVal": 75
    }
]

streamer = AmberStream(sensor_id=None, feature_count=1, streaming_window_size=120,
                       samples_to_buffer=10000, anomaly_history_window=10000,
                       learning_rate_numerator=10, learning_rate_denominator=10000,
                       learning_max_clusters=1000, learning_max_samples=1000000,
                       features=features)
streamer.stream_csv('DCD_AssemblyRoom_Hp-training.csv', samples_per_request=10)
