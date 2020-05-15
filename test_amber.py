import boonamber as amber


def test_create_sensor():
    sensor_id = 'my-sensor'
    api_key = 'my-key'
    api_tenant = 'my-tenant'

    amber.create_sensor(sensor_id, api_key, api_tenant)


def main():
    test_create_sensor()


if __name__ == '__main__':
    main()
