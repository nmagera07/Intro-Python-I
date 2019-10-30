# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # def _str_(self):
    #     return 'latitude: {self.lat}, longitude: {self.lon}'.format(self = self)

# latlon = LatLon(12,120)
# print(latlon)


test1 = LatLon(1, 2)
print(f'latitude: {test1.lat}, longitude: {test1.lon}')


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat,lon)
        self.name = name


test2 = Waypoint(20,30,'testname')
print(f'testname: {test2.name}')

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
     def __init__(self, name, difficulty, size, lat, lon):
         super().__init__(lat, lon, name)
         self.difficulty = difficulty
         self.size = size

test3 = Geocache(20,50,'testy','medium',60)
print(f'difficulty: {test3.difficulty} size: {test3.size}')

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

newwaypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(f'name: {newwaypoint.name}, latitude: {newwaypoint.lat}, longitude: {newwaypoint.lon}')

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)



# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

newgeocache = Geocache("Newberry Views", 'diff 1.5', 'size 2', 44.052137, -121.41556)
print(f'name: {newgeocache.name}, difficulty: {newgeocache.difficulty}, size: {newgeocache.size}, latitude: {newgeocache.lat}, longitude: {newgeocache.lon}')

# Print it--also make this print more nicely
# print(geocache)
