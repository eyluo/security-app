import gmaps

# load a Numpy array of (latitude, longitude) pairs
data = gmaps.datasets.load_dataset('taxi_rides')

map = gmaps.heatmap(data)
gmaps.display(map)