import json
from enb_model import *


connect('test')

with open("./json/parsed.json") as json_file:
    data = json.load(json_file)

with open("./json/enb_info.json") as json_file:
    enb_data = json.load(json_file)

enb_id = enb_data['enb_id']
mcc = enb_data['mcc']
mnc = enb_data['mnc']
region = enb_data['region']
lat = enb_data['lat']
long = enb_data['long']

enb = Enb(enb_id=enb_id, mcc=mcc, mnc=mnc, region=region, lat=lat, long=long)
enb.save()

for d in data:
    notes = None
    print("")
    print("")
    print(f"Processing {d['name']}")
    print("")
    cell_name = d['name']
    for p in d['properties']:
        if p['children'][0]['text'] not in ["*", "5G ENDC Available"]:
            print(f"{p['children'][0]['text']} = {p['children'][1]['text']}")
            if p['children'][0]['text'] == "Cell Identifier":
                id = int(p['children'][1]['text'])
            if p['children'][0]['text'] == "System Subtype":
                system_subtype = p['children'][1]['text']
            if p['children'][0]['text'] == "PCI":
                pci = p['children'][1]['text']
            if p['children'][0]['text'] == "Bandwidth":
                bandwidth = p['children'][1]['text']
            if p['children'][0]['text'] == "EARFCN":
                earfcn = int(p['children'][1]['text'])
            if p['children'][0]['text'] == "Maximum Signal (RSRP)":
                max_rsrp = p['children'][1]['text']
            if p['children'][0]['text'] == "Direction":
                direction = p['children'][1]['text']
            if p['children'][0]['text'] == "Notes":
                notes = p['children'][1]['text']
            if p['children'][0]['text'] == "Uplink Frequency":
                uplink_freq = p['children'][1]['text']
            if p['children'][0]['text'] == "Downlink Frequency":
                downlink_freq = p['children'][1]['text']
            if p['children'][0]['text'] == "Frequency Band":
                frequency_band = p['children'][1]['text']

    cell = Cell(cell_name=cell_name, cell_id=id, system_subtype=system_subtype, pci=pci , earfcn=earfcn, max_rsrp=max_rsrp,
                        direction=direction, bandwidth=bandwidth, uplink_freq=uplink_freq, downlink_freq=downlink_freq,
                        frequency_band=frequency_band,notes=notes, enb=enb)
    cell.save()
