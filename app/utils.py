import psutil
import sched
import time
import requests


s = sched.scheduler(time.time, time.sleep)
redis_key = 'ram_load'


def send_api_request(load_value):
    url = 'http://127.0.0.1:5000/add_overload_value/'
    requests.post(url=url, data={redis_key: load_value})


def get_ram_load():
    s.enter(30, 1, get_ram_load)
    load_value = psutil.virtual_memory().percent
    time.sleep(10)
    if load_value > 90.0:
        send_api_request(load_value)


if __name__ == '__main__':
    get_ram_load()
    s.run()

