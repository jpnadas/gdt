from matplotlib import pyplot as plt
import json


with open("my_buildings.json") as f:
    buildings = json.load(f)

_, ax = plt.subplots()

for b in buildings['buildings']:
    # print(b['coordinates'])
    x = [a['x'] for a in b['coordinates']]
    y = [a['y'] for a in b['coordinates']]
    ax.plot(x, y)

plt.show()
