import time
import boonamber as amber


def test_create_sensor():
    print("create_sensor")
    start = time.time()
    success, response = amber.create_sensor('my-sensor')
    end = time.time()
    print(response)
    print("time elapsed {:.6f} sec".format(end - start))
    print()


def test_delete_sensor():
    print('delete_sensor')
    start = time.time()
    success, response = amber.delete_sensor('my-sensor')
    end = time.time()
    print(response)
    print("time elapsed {:.6f} sec".format(end - start))
    print()


def test_list_sensors():
    print('list_sensors')
    start = time.time()
    success, response = amber.list_sensors()
    end = time.time()
    print(response)
    print("time elapsed {:.6f} sec".format(end - start))
    print()


def test_configure_sensor():
    print('configure_sensor')
    start = time.time()
    success, response = amber.configure_sensor('my-sensor', feature_count=1, streaming_window=25)
    end = time.time()
    print(response)
    print("time elapsed {:.6f} sec".format(end - start))
    print()


def test_stream_sensor():
    print('stream_sensor')
    data = [0.1, 0.2, 0.3, 0.4, 0.5]

    start = time.time()
    success, response = amber.stream_sensor('my-sensor', data)
    end = time.time()
    print(response)
    print("time elapsed {:.6f} sec".format(end - start))
    print()


def test_train_sensor():
    print('train_sensor')
    data = [0.1, 0.2, 0.3, 0.4, 0.5]

    start = time.time()
    success, response = amber.train_sensor('my-sensor', data)
    end = time.time()
    print(response)
    print("time elapsed {:.6f} sec".format(end - start))
    print()


def test_get_info():
    print('get_info')
    start = time.time()
    success, response = amber.get_info('my-sensor')
    end = time.time()
    print(response)
    print("time elapsed {:.6f} sec".format(end - start))
    print()


def test_get_config():
    print('get_config')
    start = time.time()
    success, response = amber.get_config('my-sensor')
    end = time.time()
    print(response)
    print("time elapsed {:.6f} sec".format(end - start))
    print()


def test_get_status():
    print('get_status')
    start = time.time()
    success, response = amber.get_status('my-sensor')
    end = time.time()
    print(response)
    print("time elapsed {:.6f} sec".format(end - start))
    print()


amber.set_credentials('my-key', 'my-tenant')
test_create_sensor()
test_delete_sensor()
test_list_sensors()
test_configure_sensor()
test_stream_sensor()
test_train_sensor()
test_get_info()
test_get_config()
test_get_status()
