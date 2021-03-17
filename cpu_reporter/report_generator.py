from datetime import timedelta, datetime
from pyspectator.processor import Cpu
from time import sleep



def generate_report(duration: timedelta):
    cpu = Cpu(monitoring_latency=0.1)

    measurements = []
    with cpu:
        end_time = datetime.now() + duration

        now = datetime.now()
        while now < end_time:
            measurements.append((datetime.now(), cpu.load))
            now = datetime.now()
            sleep(0.04)

    return measurements
