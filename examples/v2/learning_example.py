import csv
import sys
import json
from datetime import datetime
from boonamber import AmberV2Client, ApiException
import boonamber
import random

def generate_random_array(size, min_val, max_val):
    return [random.uniform(min_val, max_val) for _ in range(size)]

def generate_random_variant(input, noise):
    return [input[ii] + random.uniform(-noise, noise) for ii in range(len(input))]

model_id = None  # fill this in if a model has already been created.

try:
    random.seed(123) 

    # genereate random clusters
    num_clusters = 10
    clusters = []
    feature_count = 5
    streaming_window = 1
    min_val = 0.0
    max_val = 1000.0
    noise = 5.0
    for ii in range(num_clusters):
        random_array = generate_random_array(feature_count, min_val, max_val)
        clusters.append(random_array)
    #Some new clusters outside of our original range
    extra_cluster = generate_random_array(feature_count, max_val, 2.0*max_val)
    extra_cluster_2 = generate_random_array(feature_count, 2.0*max_val, 3.0*max_val)

    amber = AmberV2Client()

    # Create a new model
    if model_id is None:
        param = boonamber.PostModelRequest(label='amber.learning.example')
        model = amber.post_model(param)
        print(json.dumps(model.to_dict(), indent=4))
        model_id = model.id
        print("Created New Model: ", model_id)
    else:
        print("Using Existing Model: ", model_id)

    #create features list
    features = []
    for ii in range(feature_count):
        label = "feature-" + str(ii)
        features.append(boonamber.FeatureConfig(label))

    # Check if we need to reconfigure
    reconfigure = True
    try:
        current_config = amber.get_config(model_id=model_id)
        print("Current Config: ", json.dumps(current_config.to_dict(), indent=4))

        reconfigure = len(current_config.Features) != feature_count
        if current_config.streaming_window != streaming_window:
            reconfigure = True
        
        for ii in range(feature_count):
            if current_config.Features[ii].name != features[ii].name:
                reconfigure = True
    except Exception as e:
        reconfigure = True


    # Configure model
    learning_samples = 2000
    if reconfigure:
        print("(Re)Configuring Model")

        training = boonamber.TrainingConfig(history_window=1000, buffering_samples=1000, learning_max_samples=learning_samples, learning_max_clusters=1000, learning_rate_numerator=1, learning_rate_denominator=10000)
        autotuning = boonamber.AutotuneConfig(range=True, percent_variation=True)

        body = boonamber.PostConfigRequest(streaming_window=streaming_window, features=features, training=training, autotuning=autotuning)
        config_result = amber.post_config(model_id=model_id, body=body)
        print("New Config: ", json.dumps(config_result.to_dict(), indent=4))

    print("Submitting Training Data")
    status = None
    state = ""
    total_samples = learning_samples
    for ii in range(total_samples):
        template_id = ii % num_clusters
        root_vector = clusters[template_id]
        noisy_vector = generate_random_variant(root_vector, noise)
        results = amber.post_data(model_id, data=noisy_vector)
        status = results.status
        if status.state != state:
            state = status.state
            print("Samples {} New State {}".format(ii, state))
        
    cluster_count = status.cluster_count
    sample_count = status.sample_count
    print("Sent {} Samples. Cluster Count = {}. State = {}".format(sample_count, cluster_count, state))


    print("Submitting Test Data")
    test_samples = 100
    for ii in range(test_samples):
        template_id = ii % num_clusters
        root_vector = clusters[template_id]
        noisy_vector = generate_random_variant(root_vector, noise)
        results = amber.post_data(model_id, data=noisy_vector)
        estimated_id = results.analytics.id[0]
        cluster_id = template_id + 1
        if estimated_id != cluster_id:
            print("Clustering Error: {} != {}".format(estimated_id, cluster_id))

    #put it back in buffering for an extra 100 samples
    restate = "Buffering" 
    extra_samples = 100
    training = boonamber.TrainingConfig(buffering_samples=extra_samples, learning_max_samples=extra_samples)
    learning = boonamber.PostLearningRequest(state=restate, training=training)
    new_state = amber.enable_learning(model_id, learning)

    print("New State: {}".format(new_state))

    print("Submitting New Buffering Data")
    state = ""
    status = None
    last_id = 0
    for ii in range(2*extra_samples):
        noisy_vector = generate_random_variant(extra_cluster, noise)
        results = amber.post_data(model_id, data=noisy_vector)
        status = results.status
        if status.state != state:
            state = status.state
            print("Samples {} New State {}".format(ii, state))
        if status.state == "Monitoring":
            estimated_id = results.analytics.id[0]
            last_id = estimated_id
            if estimated_id < 0:
                print("Incorrect ID ", estimated_id)
    cluster_count = status.cluster_count
    sample_count = status.sample_count
    print("Sent {} Samples. New Cluster Count = {}. State = {}".format(sample_count, cluster_count, state))



    #put it back in learning for an extra 100 samples
    restate = "Learning"
    extra_samples = 100
    autotuning = boonamber.AutotuneConfig(percent_variation=False, range=False)
    training = boonamber.TrainingConfig(buffering_samples=extra_samples, learning_max_samples=extra_samples)
    learning = boonamber.PostLearningRequest(state=restate, training=training, autotuning=autotuning)
    new_state = amber.enable_learning(model_id, learning)

    print("Submitting New Learning Data")
    state = ""
    status = None
    for ii in range(2*extra_samples):
        noisy_vector = generate_random_variant(extra_cluster_2, noise)
        results = amber.post_data(model_id, data=noisy_vector)
        status = results.status
        
        #This should generate negative IDs since the values are clipping
        if state == "Monitoring":
            estimated_id = results.analytics.id[0]
            if estimated_id > 0:
                print("Incorrect ID {}".format(estimated_id))
        #In learning we will match with the last pattern we sent in (e.g. cluster id  11)
        if state == "Learning":
            estimated_id = results.analytics.id[0]
            if estimated_id != last_id:
                print("Incorrect ID {}!={}".format(estimated_id, last_id)) 
        if status.state != state:
            state = status.state
            print("Samples {} New State {}".format(ii, state))
    cluster_count = status.cluster_count
    sample_count = status.sample_count
    print("Sent {} Samples. New Cluster Count = {}. State = {}".format(sample_count, cluster_count, state))


    #put it back in buffering again
    restate = "Buffering" 
    extra_samples = 100
    training = boonamber.TrainingConfig(buffering_samples=extra_samples, learning_max_samples=extra_samples)
    learning = boonamber.PostLearningRequest(state=restate, training=training)
    new_state = amber.enable_learning(model_id, learning)

    print("Submitting New Buffering Data")
    state = ""
    status = None
    for ii in range(2*extra_samples):
        noisy_vector = generate_random_variant(extra_cluster_2, noise)
        results = amber.post_data(model_id, data=noisy_vector)
        status = results.status
        if status.state != state:
            state = status.state
            print("Samples {} New State {}".format(ii, state))
        if status.state == "Monitoring":
            estimated_id = results.analytics.id[0]
            if estimated_id < 0:
                print("Incorrect ID ", estimated_id)
    cluster_count = status.cluster_count
    sample_count = status.sample_count
    print("Sent {} Samples. New Cluster Count = {}. State = {}".format(sample_count, cluster_count, state))


    amber.delete_model(model_id)

except ApiException as e:
    print(f"Error: {e}")
    sys.exit(1)

