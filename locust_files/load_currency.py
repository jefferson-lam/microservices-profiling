import random
from locust import HttpUser, task, between

class CurrencyLoader(HttpUser):
    wait_time = between(1, 5)
    @task
    def setCurrency(self):
        currencies = ['EUR', 'USD', 'JPY', 'CAD']
        self.client.post("/setCurrency", { 'currency_code': random.choice(currencies) })
