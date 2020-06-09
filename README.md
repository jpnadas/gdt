# Glasgow Digital Twin (GDT)

Contains scripts used to process the output of the GDT simulation and also scripts for setting up the simulation.

# Setup

## Building data
We fetch data from [open street maps](https://www.openstreetmap.org/) to add buildings to our simulation using their [overpass-api](https://overpass-api.de/). 

### Preview
To get a preview of which buildings you will get using the API, you can use [overpass-turbo](https://overpass-turbo.eu/). In particular, it is useful to determine the GPS coordinates of the area you want to get buildings from. Once you have the area you want on the right-hand side window, run the query below

```
node
	[building=yes]
	({{bbox}});
way
  	[building=yes]
  	({{bbox}});
(._;>;);
out;
```

After that, you can go on `export` and then select `Data`->`raw data directly from Overpass API`. On the URL generated, the GPS coordinates of the current map view will be arguments, which are easy to extract.

### Fetch building data

#### Dependencies
* [mongodb](https://www.mongodb.com/)
* [mongoimport](https://docs.mongodb.com/manual/reference/program/mongoimport/#:~:text=Synopsis,the%20inverse%20%E2%80%9Cexporting%E2%80%9D%20capability.)
* [osmtogeojson](https://www.npmjs.com/package/osmtogeojson)

#### Usage

In order to fetch the building data and add it to a mongodb collection, you can run `src/setup/buildings/fetch_building_data`.

Edit the script to configure the name of your database and also the area (in GPS coordinates) you want to get buildigns from OSM.

### Plotting the obtained data

#### Dependencies
* Python 3 (Tested under 3.8)
* matplotlib

#### Usage

In order to plot the data, you can run `src/setup/buildings/plot_building_data`, which will first convert the coordinates to a Cartesian projection using our custom C++ code (which reads from the mongodb specified) and then plot it using `matplotlib`.

You should change the script to use your central coordinates and your database.

# Utilities

## Cleanup

There is a clenaup utility which is a simple Python wrapper for dropping mongo databases. 

# License

This code is licensed under GNU General Public License v2.0.
