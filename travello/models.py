from django.db import models

# Create your models here.
class Destination():
    id: int
    name: str
    image: str
    desc: str
    price: int
    offer: bool
    
    def __init__(self, id, name, desc, image, price, offer):
        self.id = id
        self.name = name
        self.image = image
        self.desc = desc
        self.price = price
        self.offer = offer