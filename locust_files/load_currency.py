import random
from locust import HttpUser, task

class CurrencyLoader(HttpUser):
    @task
    def setCurrency(self):
        currencies = ['EUR', 'USD', 'JPY', 'CAD']
        self.client.post("/setCurrency", { 'currency_code': random.choice(currencies) })
