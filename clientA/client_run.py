import signal
from time import sleep
import json
import subprocess
import os

from p2p.message_manager import MSG_NEW_TRANSACTION
from core.client_core import ClientCore

my_p2p_client = None
dirname = os.path.dirname(__file__)


def signal_handler(signal, frame):
    shutdown_client()


def shutdown_client():
    global my_p2p_client
    my_p2p_client.shutdown()


def subpr_api():
    cmd = "python {}/call_train_api.py".format(dirname)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    bus_data = proc.stdout.read().decode()
    return json.loads(bus_data)
    # return bus_data


def main():
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_client
    my_p2p_client = ClientCore(50095, '192.168.11.35', 50082)
    my_p2p_client.start()

    sleep(10)

    while True:
        my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, json.dumps(subpr_api()))
        # for data in subpr_api():
        #     my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, json.dumps(data))
        sleep(30)


if __name__ == '__main__':
    main()
    # print("python {}/call_train_api.py".format(dirname))
