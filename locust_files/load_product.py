import random
from locust import HttpUser, task, between

products = [
    '0PUK6V6EV0',
    '1YMWWN1N4O',
    '2ZYFJ3GM2N',
    '66VCHSJNUP',
    '6E92ZMYYFZ',
    '9SIQT8TOJO',
    'L9ECAV7KIM',
    'LS4PSXUNUM',
    'OLJCESPC7Z']

class ProductLoader(HttpUser):
    wait_time = between(1, 5)
    @task
    def browseIndex(self):
        self.client.get("/")

    @task
    def browseProduct(self):
        self.client.get("/product/" + random.choice(products))

