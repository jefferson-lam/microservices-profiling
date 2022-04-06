import random
from locust import HttpUser, task

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

class CartUser(HttpUser):
    @task
    def viewCart(self):
        self.client.get("/cart")

    @task
    def addToCart(self):
        product = random.choice(products)
        self.client.get("/product/" + product)
        self.client.post("/cart", { 'product_id': product, 'quantity': random.choice([1,2,3,4,5,10]) })

    @task
    def emptyCart(self):
        self.client.post("/cart/empty")
