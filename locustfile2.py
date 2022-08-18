from locust import HttpUser, task, constant_throughput, between
import random as r


class HelloWorldUser(HttpUser):
    wait_time = constant_throughput(1)
    host = 'http://192.168.1.86:49172'

    @task(4)
    def fib(self):
        rng = 20, 25
        number = r.randint(*rng)
        self.client.get(f'/fibonacci?number={number}', name=f'fibonacci {rng}')

    @task(4)
    def sort1(self):
        rng = 15_000, 20_000
        number = r.randint(*rng)
        self.client.get(f'/sort?n={number}', name=f'sort {rng}-list')

    @task(3)
    def sort2(self):
        number = 10_000
        self.client.get(f'/sort?n={number}', name=f'sort {number}-list')

    @task(1)
    def wait(self):
        wait_time = 5
        self.client.get(f"/wait?sec={wait_time}", name=f'{wait_time} sec response')

    @task(3)
    def unstable(self):
        self.client.get("/unstable", name='unstable response 1/30')

    @task(6)
    def default(self):
        self.client.get('/', name='default response')
