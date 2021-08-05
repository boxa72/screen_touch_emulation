from ppadb.client import Client as AdbClient
import multiprocessing as mp

def connect():
    client = AdbClient(host="127.0.0.1", port=5037)

    devices = client.devices()

    if len(devices) == 0:
        print('No Devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

def tapping(tap):
    for x in range(1000):
        device.shell(f'input tap {tap}')


if __name__ == "__main__":
    device, client = connect()

    tap = '730 1000'
    tapping(tap)
