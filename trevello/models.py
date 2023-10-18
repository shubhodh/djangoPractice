from django.db import models


# Create your models here.

class Destination:
    id: int
    desc: str
    name: str
    img: str
    price: int
    offer : bool
