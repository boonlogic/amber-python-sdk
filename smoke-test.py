import time
from boonamber import AmberClient, BoonException


amber = AmberClient()

# authenticate
print("authenticating")
success, response = amber.authenticate('', '')
print("success: {}, response: {}".format(success, response))

# # create sensor
# print("creating sensor")
# success, response = amber.create_sensor('test-sensor')
# print("success: {}, response: {}".format(success, response))


# def run_create_sensor():
#     print("create_sensor")
#     start = time.time()
#     success, response = amber.create_sensor('my-sensor')
#     end = time.time()
#     print(response)
#     print("time elapsed {:.6f} sec".format(end - start))
#     print()


# def run_delete_sensor():
#     print('delete_sensor')
#     start = time.time()
#     success, response = amber.delete_sensor('my-sensor')
#     end = time.time()
#     print(response)
#     print("time elapsed {:.6f} sec".format(end - start))
#     print()


# def run_list_sensors():
#     print('list_sensors')
#     start = time.time()
#     success, response = amber.list_sensors()
#     end = time.time()
#     print(response)
#     print("time elapsed {:.6f} sec".format(end - start))
#     print()


# def run_configure_sensor():
#     print('configure_sensor')
#     start = time.time()
#     success, response = amber.configure_sensor('my-sensor', feature_count=1, streaming_window=25)
#     end = time.time()
#     print(response)
#     print("time elapsed {:.6f} sec".format(end - start))
#     print()


# def run_stream_sensor():
#     print('stream_sensor')
#     data = [0.1, 0.2, 0.3, 0.4, 0.5]

#     start = time.time()
#     success, response = amber.stream_sensor('my-sensor', data)
#     end = time.time()
#     print(response)
#     print("time elapsed {:.6f} sec".format(end - start))
#     print()


# def run_train_sensor():
#     print('train_sensor')
#     data = [0.1, 0.2, 0.3, 0.4, 0.5]

#     start = time.time()
#     success, response = amber.train_sensor('my-sensor', data)
#     end = time.time()
#     print(response)
#     print("time elapsed {:.6f} sec".format(end - start))
#     print()


# def run_get_info():
#     print('get_info')
#     start = time.time()
#     success, response = amber.get_info('my-sensor')
#     end = time.time()
#     print(response)
#     print("time elapsed {:.6f} sec".format(end - start))
#     print()


# def run_get_config():
#     print('get_config')
#     start = time.time()
#     success, response = amber.get_config('my-sensor')
#     end = time.time()
#     print(response)
#     print("time elapsed {:.6f} sec".format(end - start))
#     print()


# def run_get_status():
#     print('get_status')
#     start = time.time()
#     success, response = amber.get_status('my-sensor')
#     end = time.time()
#     print(response)
#     print("time elapsed {:.6f} sec".format(end - start))
#     print()


# amber.set_credentials('my-key', 'my-tenant')
# run_create_sensor()
# run_delete_sensor()
# run_list_sensors()
# run_configure_sensor()
# run_stream_sensor()
# run_train_sensor()
# run_get_info()
# run_get_config()
# run_get_status()
