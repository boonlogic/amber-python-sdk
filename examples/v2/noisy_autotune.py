from boonamber import AmberV2Client, ApiException, float_list_to_csv_string
import boonamber.v2.models as v2models

from datetime import datetime
import pandas as pd
import numpy as np
import logging
import time
import os
import sys
from queue import Queue, Empty
import tkinter
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import matplotlib.dates as mdates

import random

# os.environ["AMBER_V2_LICENSE_KEY"] = "64833cb0d29527c2a87f12e9"
# os.environ["AMBER_V2_SECRET_KEY"] = "369007e09737c043eb642ec463a1eb"
# os.environ["AMBER_V2_SERVER"] = "https://127.0.0.1/v2"
# os.environ["AMBER_V2_VERIFY"] = "False"

os.environ["AMBER_V2_LICENSE_KEY"] = "64d24cd9c6cb784f15617932"
os.environ["AMBER_V2_SECRET_KEY"] = "xXTovwqWFUxTLW14bGr6eKclsji653eA"
os.environ["AMBER_V2_SERVER"] = "https://amber.boonlogic.com/v2"


def generate_data(num_clusters, max_val, features):
    random.seed(9735)
    data = []
    for ii in  range(num_clusters):
        temp = [random.uniform(0.0, max_val) for _ in range(len(features))]
        data.append(temp)
    return data

def add_noise(noise, data):
    return [x + random.uniform(-noise, noise) for x in data]

def main():
    #make amber
    amber_client = AmberV2Client.from_environment()
    version_info = amber_client.get_version()
    print(version_info)


    ############################################
    # Set the following variables before running
    ############################################
    #Must match the sensor name on vessel db
    asset_name = "noisyautotuner"
    
    retrain = True # Whether to overwrite local model

    sensor_list = ["sensor1", "sensor2", "sensor3", "sensor4", "sensor5", "sensor6", "sensor7", "sensor8", "sensor9", "sensor10"]

    feature_count = int(len(sensor_list))
    print("Feature List: {}".format(sensor_list))

    #get test data
    num_samples = 10000
    default_chunk_size = 1000
    chunk_size = default_chunk_size
    num_chunks = int(num_samples / chunk_size) + 1

    num_clusters = 5
    max_val = 10000
    noise = 200
    base_vectors = generate_data(num_clusters, max_val, sensor_list)
    print(base_vectors)
    sensor_data = []
    for ii in range(num_samples):
        clusterid = ii % num_clusters
        temp = add_noise(noise, base_vectors[clusterid])
        sensor_data.append(temp)

    

    # colors = [plt.cm.hsv(i) for i in np.linspace(0, 1, 600)]
    # random.seed(187) # uncomment this if you want the same colors everytime
    # random.shuffle(colors)

    # print(colors)

    # featureid = [x for x in range(feature_count)]
    # plt.figure()
    # for ii in range(num_samples):
    #     clusterid = ii % num_clusters
    #     print(clusterid)
    #     if len(featureid) != len(sensor_data[ii]):
    #         raise Exception("WTF {} {} ".format(len(featureid), len(sensor_data[ii])))
    #     plt.plot(featureid, sensor_data[ii], color=colors[clusterid])
    # plt.show()

    # sys.exit(0)

    #find sensor
    response = amber_client.get_models()
    all_models = response.model_list
    amber_mid = None
    reconfigure = False
    for model in all_models:
        if model.label == asset_name:
            #either use existing sensor or delete
            if retrain:
                amber_client.delete_model(model.id)
            else:
                amber_mid = model.id
            break


    if amber_mid == None:
        #Create model id
        param = v2models.PostModelRequest(label=asset_name)
        model_result = amber_client.post_model(param)
        amber_mid= model_result.id
        print("Created model ID {}".format(amber_mid))
        reconfigure = True
    else:
        print("Using existing model ID {}".format(amber_mid))

        #Get config
        config_response = amber_client.get_config(amber_mid)
        print("Amber Config: {} ".format(config_response))

        feature_count = len(config_response.features)
        if len(sensor_list) != feature_count:
            print("Different number of features")
            reconfigure = True

    #Either we need to configure or reconfigure this model
    if reconfigure:
        training = v2models.TrainingConfig(history_window=10000, buffering_samples=num_samples, learning_max_samples=num_samples, learning_max_clusters=1000, learning_rate_numerator=1, learning_rate_denominator=10000)
        autotuning = v2models.AutotuneConfig(range=True, percent_variation=True)
        features = []
        for sensor in sensor_list:
            feature = v2models.FeatureConfig(sensor)
            features.append(feature)

        body = v2models.PostConfigRequest(streaming_window=1, percent_variation=0.05, features=features, training=training, autotuning=autotuning)
        response = amber_client.post_config(model_id=amber_mid, body=body)
        config_result = response.to_dict()

        print("Configured model: {} {}".format(len(response.features), config_result))
        retrain = True


    previous_sample_count = 0
    if retrain:
        print("\nTraining Model With All Data")

        #Run Data through to monitoring
        previous_state = "Default"
        start = 0
        end = 0
        while(True):
            start = end
            end = min(end + chunk_size, num_samples)
            data = sensor_data[start:end]

            if len(data) == 0:
                print("Empty Chunk")
                continue

            #print("Inferencing {} to {}".format(start, end))

            #inference data
            response = amber_client.post_data(
                amber_mid,
                data=data,
            )
            analytics = response.analytics.to_dict()
            status = response.status.to_dict()

            state = status["state"]
            progress = status["progress"]
            sample_count = status["sample_count"]
            if state != previous_state:
                print("State: {}".format(state))
                previous_state = state

            if sample_count <= previous_sample_count:
                print("Sample Count Wrong")
            previous_sample_count = sample_count

            print("Progress: {}".format(progress))

            # response2 = amber_client.get_status(amber_mid)
            # print("status: {}".format(response2)) 

            if state == "Autotuning":
                chunk_size = 1
            else:
                chunk_size = default_chunk_size

            if state == "Monitoring":
                break

            if end == num_samples:
                break

        print("Buffering Sample Count {}".format(previous_sample_count))
        print("\nRun Autotuning")

        #Run Autotuning through to completion
        while(True):
            data = sensor_data[num_samples-1]

            #inference data
            response = amber_client.post_data(
                amber_mid,
                data=data,
            )
            analytics = response.analytics.to_dict()
            status = response.status.to_dict()

            state = status["state"]
            progress = status["progress"]
            sample_count = status["sample_count"]
            if state != previous_state:
                print("State: {}".format(state))
                previous_state = state
            
            if sample_count <= previous_sample_count:
                print("Sample Count Wrong")
            previous_sample_count = sample_count

            print("Progress: {}".format(progress))

            if state == "Learning" or state == "Monitoring":
                break

        print("Autotuning Sample Count {}".format(previous_sample_count))
    elif pretrain:
        print("post_pretrain...")
        state = amber_client.post_pretrain(
            model_id=amber_mid, data=sensor_data, block=True
        )
        print("state: {}".format(state))

    #Which results to store
    results_keys = ["RI", "SI", "AH", "AD", "AW", "NI", "NS", "NW", "OM"]
    results = {}
    for key in results_keys:
        results[key] = []

    print("\nInferencing All Data")

    #now rerun data through for inferencing
    chunk_size = default_chunk_size
    start = 0
    end = 0
    while(True):
        start = end
        end = min(end + chunk_size, num_samples)
        data = sensor_data[start:end]

        if len(data) == 0:
            print("Empty Chunk")
            continue

        print("Inferencing {} to {}".format(start, end))

        #inference data
        response = amber_client.post_data(
            amber_mid,
            data=data,
        )
        analytics = response.analytics.to_dict()
        status = response.status.to_dict()

        for key in results_keys:
            results[key].extend(analytics[key.lower()])

        if end == num_samples:
            break

    print("Results Length: {}".format(len(results["RI"])))


    #Get cluster growth array
    response = amber_client.get_status(amber_mid)
    status = response.to_dict()

    #Extract 
    num_clusters = status['cluster_count']
    totalInferences = status['sample_count']

    print("Cluster Count: {}".format(num_clusters))
    print("Total Sample Count: {}".format(totalInferences))


main()