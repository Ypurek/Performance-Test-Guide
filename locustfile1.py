from locust import HttpUser, task, constant
import random as r


class HelloWorldUser(HttpUser):
    wait_time = constant(1)
    host = 'http://192.168.1.86:49172'

    @task
    def unstable(self):
        self.client.get("/unstable", name='unstable response 1/30')

    # @task
    def fib(self):
        rng = 20, 25
        number = r.randint(*rng)
        self.client.get(f'/fibonacci?number={number}', name=f'fibonacci {rng}')

    # @task
    def default(self):
        self.client.get('/', name='default response')

    # @task
    def wait(self):
        self.client.get("/wait?time=10", name='10 sec response')

    # @task
    def sort(self):
        self.client.get('/sort?n=15000', name='sort 15k-list')
