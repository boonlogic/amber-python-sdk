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

# os.environ["AMBER_V2_LICENSE_KEY"] = "64833cb0d29527c2a87f12e9"
# os.environ["AMBER_V2_SECRET_KEY"] = "369007e09737c043eb642ec463a1eb"
# os.environ["AMBER_V2_SERVER"] = "https://127.0.0.1/v2"
# os.environ["AMBER_V2_VERIFY"] = "False"

os.environ["AMBER_V2_LICENSE_KEY"] = "64d24cd9c6cb784f15617932"
os.environ["AMBER_V2_SECRET_KEY"] = "xXTovwqWFUxTLW14bGr6eKclsji653eA"
os.environ["AMBER_V2_SERVER"] = "https://amber.boonlogic.com/v2"


def main():
    #make amber
    amber_client = AmberV2Client.from_environment()
    version_info = amber_client.get_version()
    print(version_info)

    response = amber_client.get_models()
    all_models = response.model_list
    for model in all_models:
        if model.label == "V2SampleSystem":
            amber_client.delete_model(model.id)
            print("deleting amber model {}".format(model))
            break
    sys.exit(0)

    ############################################
    # Set the following variables before running
    ############################################
    #Must match the sensor name on vessel db
    asset_name = "LibertyIsland.LibertyPumpDrivePS.TC"
    
    #csv file captured using the mongo_query.py script from the mongo-sync repo
    file = "/home/rodney/Documents/GLDD/Vessels/Liberty/PumpDrivePS_Retrain/GLDD_Data_LibertyPumpDrivePS_2021-10-01_00:00:00.csv"

    retrain = True # Whether to overwrite local model

    #Match these labels with column labels in csv
    sub_systems = {}
    sub_systems["position1"] = ['GLDD-Liberty-Sensor5_1000_hz', 'GLDD-Liberty-Sensor5_2000_hz', 'GLDD-Liberty-Sensor5_4000_hz', 'GLDD-Liberty-Sensor5_6000_hz', 'GLDD-Liberty-Sensor5_9000_hz', 'GLDD-Liberty-Sensor5_12000_hz', 'GLDD-Liberty-Sensor5_15000_hz', 'GLDD-Liberty-Sensor5_20000_hz']
    sub_systems["position2"] = ['GLDD-Liberty-Sensor6_1000_hz', 'GLDD-Liberty-Sensor6_2000_hz', 'GLDD-Liberty-Sensor6_4000_hz', 'GLDD-Liberty-Sensor6_6000_hz', 'GLDD-Liberty-Sensor6_9000_hz', 'GLDD-Liberty-Sensor6_12000_hz', 'GLDD-Liberty-Sensor6_15000_hz', 'GLDD-Liberty-Sensor6_20000_hz']
    sub_systems["position3"] = ['GLDD-Liberty-Sensor7_1000_hz', 'GLDD-Liberty-Sensor7_2000_hz', 'GLDD-Liberty-Sensor7_4000_hz', 'GLDD-Liberty-Sensor7_6000_hz', 'GLDD-Liberty-Sensor7_9000_hz', 'GLDD-Liberty-Sensor7_12000_hz', 'GLDD-Liberty-Sensor7_15000_hz', 'GLDD-Liberty-Sensor7_20000_hz']
    sub_systems["position4"] = ['GLDD-Liberty-Sensor8_1000_hz', 'GLDD-Liberty-Sensor8_2000_hz', 'GLDD-Liberty-Sensor8_4000_hz', 'GLDD-Liberty-Sensor8_6000_hz', 'GLDD-Liberty-Sensor8_9000_hz', 'GLDD-Liberty-Sensor8_12000_hz', 'GLDD-Liberty-Sensor8_15000_hz', 'GLDD-Liberty-Sensor8_20000_hz']
    sub_systems["position5"] = ['GLDD-Liberty-Sensor9_1000_hz', 'GLDD-Liberty-Sensor9_2000_hz', 'GLDD-Liberty-Sensor9_4000_hz', 'GLDD-Liberty-Sensor9_6000_hz', 'GLDD-Liberty-Sensor9_9000_hz', 'GLDD-Liberty-Sensor9_12000_hz', 'GLDD-Liberty-Sensor9_15000_hz', 'GLDD-Liberty-Sensor9_20000_hz']
    sub_systems["position6"] = ['GLDD-Liberty-Sensor10_1000_hz', 'GLDD-Liberty-Sensor10_2000_hz', 'GLDD-Liberty-Sensor10_4000_hz', 'GLDD-Liberty-Sensor10_6000_hz', 'GLDD-Liberty-Sensor10_9000_hz', 'GLDD-Liberty-Sensor10_12000_hz', 'GLDD-Liberty-Sensor10_15000_hz', 'GLDD-Liberty-Sensor10_20000_hz']


    ############################################
    # Start of script
    ############################################
    dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

    df = pd.read_csv(file, header=0, parse_dates=['timeStamp'], date_parser=dateparse, low_memory=False)
    num_rows = df.shape[0]
    num_cols = df.shape[1]
    print("rows: {}".format(num_rows))

    #get all columns
    column_names = list(df.columns)
    print("column names: {}".format(column_names))

    time_column = "timeStamp"

    
    sensor_list = []
    for name, system in sub_systems.items():
        sensor_list.extend(system)
    feature_count = int(len(sensor_list))
    print("Feature List: {}".format(sensor_list))

    
    #get test data
    sensor_data = df[sensor_list].values
    num_samples = sensor_data.shape[0]
    print("Sensor Data Shape {}".format(sensor_data.shape))
    default_chunk_size = 1000
    chunk_size = default_chunk_size
    num_chunks = int(num_samples / chunk_size) + 1

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

        print("Configured model: {}".format(config_result))
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
            data = sensor_data[start:end, :]

            if data.shape[0] == 0:
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
            data = sensor_data[num_samples-1, :]

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
        data = sensor_data[start:end, :]

        if data.shape[0] == 0:
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

    #Add to data frame
    for key in results_keys:
        df[key] = results[key]

    #Get cluster growth array
    response = amber_client.get_status(amber_mid)
    status = response.to_dict()

    #Extract 
    num_clusters = status['cluster_count']
    totalInferences = status['sample_count']

    print("Cluster Count: {}".format(num_clusters))
    print("Total Sample Count: {}".format(totalInferences))

    legends = ["1000 hz", "2000 hz", "4000 hz", "6000 hz", "9000 hz", "12000 hz", "15000 hz", "20000 hz"]

    #Define Figure , figsize=(20,6*num_plots), dpi=100
    num_plots = len(sub_systems) + len(results_keys)
    fig, axs = plt.subplots(nrows=num_plots, ncols=1)
    fig.tight_layout(pad=10.0)
    fig.suptitle('Amber Results {} Retrain'.format(asset_name))
    plot_id = 0

    for name, system in sub_systems.items():
        
        rename_dict = {}
        for sensor, legend in zip(system, legends):
            rename_dict[sensor] = legend

        sensor_df = df[[time_column] + system]
        sensor_df.rename(columns=rename_dict, inplace=True)
        sensor_df.set_index(time_column, inplace = True)

        #Plot input data
        if plot_id % 2 == 0:
            sensor_df.plot(ax=axs[plot_id])
            axs[plot_id].legend(bbox_to_anchor=(1.0, 1), loc="upper left")
        else:
            sensor_df.plot(ax=axs[plot_id], legend=None)
        
        axs[plot_id].set(xlabel="", ylabel=name)
        plot_id += 1

    for analytic in results_keys:
        analytic_df = df[[time_column] + [analytic]]
        analytic_df.set_index(time_column, inplace = True)

        #plot analytic
        analytic_df.plot(ax=axs[plot_id], legend=None)
        axs[plot_id].set(xlabel="", ylabel=analytic)
        plot_id += 1
        
    #plt.savefig('temp.png')
    #plt.subplots_adjust(bottom=0.5)
    plt.show()


main()