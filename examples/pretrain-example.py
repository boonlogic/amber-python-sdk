import csv
import sys
import json
import time
from boonamber import AmberClient, AmberCloudError, AmberUserError

"""Demonstrates a use case in which we pretrain on data in a CSV file."""


class AmberStream:

    def __init__(self, sensor_id=None):
        """
        Initializes the AmberStream example class.
        :param sensor_id: The sensor_id to be used by AmberStream.  If sensor_id is None, then a sensor is created
        """
        self.data = []
        self.sample_cnt = 0

        try:
            self.amber = AmberClient()
            if sensor_id is None:
                self.sensor_id = self.amber.create_sensor(label='stream-example-sensor')
                print("created sensor {}".format(sensor_id))
            else:
                self.sensor_id = sensor_id
                print("using sensor {}".format(sensor_id))

            config = self.amber.configure_sensor(self.sensor_id, feature_count=1, streaming_window_size=25,
                                                 samples_to_buffer=1000, learning_max_clusters=1000,
                                                 learning_max_samples=20000, learning_rate_numerator=0,
                                                 learning_rate_denominator=20000)
            print("{} config: {}".format(self.sensor_id, config))
        except AmberCloudError as e:
            print(e)
            sys.exit(1)

    def pretrain_csv(self, csv_file):
        """
        Given a path to a csv file, read all data and run pretraining
        :param csv_file: Path to csv file
        :return: None
        """
        print("Reading CSV...\n")
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            self.data = []
            self.sample_cnt = 0
            for row in csv_reader:
                for d in row:
                    self.data.append(float(d))
            try:
                results = self.amber.pretrain_sensor(self.sensor_id, self.data)
            except AmberCloudError as e:
                print(e)
                sys.exit(1)
            except AmberUserError as e:
                print(e)
                sys.exit(1)
            print(json.dumps(results))

    def pretrain_csv_nonblocking(self, csv_file):
        """
        Given a path to a csv file, read all data and run pretraining
        in non-blocking mode, querying occasionally to check when done.
        :param csv_file: Path to csv file
        :return: None
        """
        print("Reading CSV...\n")
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            self.data = []
            self.sample_cnt = 0
            for row in csv_reader:
                for d in row:
                    self.data.append(float(d))
            try:
                results = self.amber.pretrain_sensor(self.sensor_id, self.data, block=False)
            except AmberCloudError as e:
                print(e)
                sys.exit(1)
            except AmberUserError as e:
                print(e)
                sys.exit(1)

        try:
            while True:
                time.sleep(5)
                results = self.amber.get_pretrain_state(self.sensor_id)
                if results['message'] == "pretraining in progress":
                    print(results)
                elif results['message'] == "not pretraining":
                    print(results)
                    break
                else:
                    break
        except AmberUserError as e:
            print(e)
            sys.exit(1)

# Specifying sensor_id will use existing over creating a new one
streamer = AmberStream(sensor_id='6ed988ad8b729aed')
streamer.pretrain_csv('output_current.csv')
# streamer.pretrain_csv_nonblocking('output_current.csv')
