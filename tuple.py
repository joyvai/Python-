from collections import namedtuple
station = namedtuple("station","id, city,state,lat,long")
denver = station(44,"Denver",'co',40, 105)
print denver
print denver.city
print denver[1]
