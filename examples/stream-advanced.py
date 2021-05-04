import csv
import sys
from datetime import datetime
from boonamber import AmberClient, AmberCloudError

"""Demonstrates a streaming use case in which we read continuously
   from a CSV file, inference the data line by line, and print results.
"""


class AmberStream:

    def __init__(self, sensor_id=None):
        """
        Initializes the AmberStream example class.
        :param sensor_id: The sensor_id to be used by AmberStream.  If sensor_id is None, then a sensor is created
        """
        self.data = []
        self.sample_cnt = 0

        try:
            self.amber = AmberClient(verify=False)
            if sensor_id is None:
                self.sensor_id = self.amber.create_sensor(label='stream-example-sensor')
                print("created sensor {}".format(sensor_id))
            else:
                self.sensor_id = sensor_id
                print("using sensor {}".format(sensor_id))

            #config = self.amber.configure_sensor(self.sensor_id, feature_count=1, streaming_window_size=25,
            #                                     samples_to_buffer=1000, learning_max_clusters=1000,
            #                                     learning_max_samples=20000, learning_rate_numerator=0,
            #                                     learning_rate_denominator=20000)
            #print("{} config: {}".format(self.sensor_id, config))
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
        results = self.amber.stream_sensor(self.sensor_id, self.data)
        d2 = datetime.now()
        delta = (d2 - d1).microseconds / 1000
        print("State: {}({}%), inferences: {}, clusters: {}, samples: {}, duration: {}".format(
            results['state'], results['progress'], results['totalInferences'], results['clusterCount'], self.sample_cnt,
            delta))
        for analytic in ['ID', 'SI', 'AD', 'AH', 'AM', 'AW']:
            if analytic == 'AM':
                analytic_pretty = ','.join("{:.6f}".format(a) for a in results[analytic])
            else:
                analytic_pretty = ','.join("{}".format(a) for a in results[analytic])
            print("{}: {} ".format(analytic, analytic_pretty))
        self.data = []

    def stream_csv(self, csv_file, batch_size=20):
        """
        Given a path to a csv file, stream data to Amber in sizes specified by batch_size
        :param csv_file: Path to csv file
        :param batch_size: Batch size to be used on each request
        :return: None
        """
        # Open csv data file and begin streaming
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
streamer = AmberStream(sensor_id='fa3e84492dcf96c6')
# streamer = AmberStream()
streamer.stream_csv('output_current.csv', batch_size=25)
