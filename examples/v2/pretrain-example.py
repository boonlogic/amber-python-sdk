import csv
import sys
import json
import time
from boonamber import AmberV2Client, ApiException
import boonamber

"""Demonstrates pretraining of data in a CSV file."""

class AmberStream:

    def __init__(self, model_id=None):
        """
        Initializes the AmberStream example class.
        :param model_id: The model_id to be used by AmberStream.  If model_id is None, then a model is created
        """
        self.data = []
        self.sample_cnt = 0
        self.model_id = model_id

        try:
            self.amber = AmberV2Client()
            if self.model_id is None:
                param = boonamber.PostModelRequest(label='amber.sdk.example.v2:pretrain')
                model_result = self.amber.post_model(param)
                self.model_id = model_result.id
                print("created model {}".format(self.model_id))
            else:
                print("using model {}".format(self.model_id))

            body = boonamber.PostConfigRequest(streaming_window=25, features=[boonamber.FeatureConfig("feature-1")])
            config_result = self.amber.post_config(model_id=self.model_id, body=body)
            print("{} config: {}".format(self.model_id, config_result))
        except ApiException as e:
            print(e)
            sys.exit(1)

    def pretrain_csv(self, csv_file, chunk_size=400000):
        """
        Given a path to a csv file, read all data and run pretraining
        in non-blocking mode, querying occasionally to check when done.
        :param csv_file: Path to csv file
        :return: None
        """
        print("Reading CSV...")
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            self.data = []
            self.sample_cnt = 0
            for row in csv_reader:
                for d in row:
                    self.data.append(float(d))
            try:
                results = self.amber.post_pretrain(model_id=self.model_id, data=self.data, chunk_size=chunk_size, block=False)
                if results.status == "Pretrained":
                    return results
            except ApiException as e:
                print(e)
                sys.exit(1)

        print("Pretraining...")
        try:
            while True:
                time.sleep(5)
                results = self.amber.get_pretrain(self.model_id)
                if results.status == "Pretraining":
                    print(results)
                elif results.status == "Pretrained":
                    return results
                else:
                    break
        except Exception as e:
            print(e)
            sys.exit(1)

# Specifying model_id will use existing over creating a new one
streamer = AmberStream()
results = streamer.pretrain_csv('output_current.csv', chunk_size=15000)
print(json.dumps(results.to_dict(), indent=4))