from mongoengine import *

class Enb(Document):
    enb_id = IntField()
    mcc = IntField()
    mnc = IntField()
    region = IntField()
    bands = ListField(IntField())
    long = FloatField()
    lat = FloatField()


class Cell(Document):
    cell_name = StringField()
    cell_id = IntField() 
    system_subtype = StringField()
    pci = StringField()
    earfcn = IntField()
    max_rsrp = StringField()
    direction = StringField()
    bandwidth = StringField()
    uplink_freq = StringField()
    downlink_freq = StringField()
    notes = StringField()
    frequency_band = StringField()
    enb = ReferenceField(Enb)
