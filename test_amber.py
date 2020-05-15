import sys
import boonamber as amber


def test_create_sensor():
    print("create_sensor")
    success, response = amber.create_sensor('my-sensor')
    print(response)
    print()


def main():
    amber.set_credentials(api_key='my-key', api_tenant='my-tenant')
    test_create_sensor()


if __name__ == '__main__':
    main()
