import datetime
import os
import time

was = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')


def handler(event, context):
    now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    time.sleep(5)

    return was
