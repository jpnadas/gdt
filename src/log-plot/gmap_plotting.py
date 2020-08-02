'''
Plot on google maps the sequence of latitude and longitudes from
the routes mobility model.
'''
import gmplot
import json
from my_model import Enb
from mongoengine import connect


connect('test')

with open("google_api_key") as f:
    key = f.read()


gmap = gmplot.GoogleMapPlotter(lat=55.86939625225858,
                               lng=-4.286459782828637,
                               zoom=15,
                               apikey=key)

with open('./results/lat_long.json') as json_file:
    data = json.load(json_file)
    data = data['nodes']

for d in data.values():
    lats = d['latitude']
    longs = d['longitude']
    gmap.scatter([lats[0], lats[-1]], [longs[0], longs[-1]], color='#FF0000', size=1, marker=False)
    gmap.plot(lats, longs, 'cornflowerblue', edge_width=2.5)

for enb in Enb.objects():
    gmap.scatter([enb.lat], [enb.long], size=5, marker='d')


# lats = [41.15511, 41.15514, 41.15514, 41.15514]
# longs = [-8.61284, -8.6129, -8.61296, -8.61302]

gmap.draw('glasgow.html')
