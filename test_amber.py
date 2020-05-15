import boonamber as amber


def test_create_sensor():
    sensor_id = 'my-sensor'
    api_key = 'my-key'
    api_tenant = 'my-tenant'

    print("create_sensor")
    success, response = amber.create_sensor(sensor_id)
    if not success:
        raise amber.BoonException("create sensor failed: {}".format(response))
    print(response)
    print()


def main():
    amber.set_credentials(api_key='my-key', api_tenant='my-tenant')
    test_create_sensor()


if __name__ == '__main__':
    main()
