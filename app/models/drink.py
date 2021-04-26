from mongoengine import *


class Drinks(Document):
    nama = StringField(max_length=200, required=True)
    harga = IntField(required=True)
