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

# TODO speed up taps, run in parallel

if __name__ == "__main__":
    device, client = connect()

    tap = '730 1000'
    
    p1 = mp.Process(target=tapping, args=(tap,))
    p1.start()
    p1.join()

    tap = '735 1010'
    p2 = mp.Process(target=tapping, args=(tap,))
    p2.start()
    p2.join()

    tap = '750 1020'
    p3 = mp.Process(target=tapping, args=(tap,))
    p3.start()
    p3.join()

    tap = '755 1030'
    p4 = mp.Process(target=tapping, args=(tap,))
    p4.start()
    p4.join()
    

    p1.close()
    p2.close()
    p3.close()
    p4.close()