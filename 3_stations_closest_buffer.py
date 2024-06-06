folder = r"C:\Users\laura\OneDrive - Scientific Network South Tyrol\Documents\Master\Semester2\3.advanced geomatics\GitHub"
csvpath = f"{folder}/datasets/stations.txt"

from pyqgis_scripting_ext.core import *

#always long lat

#02- plot stations file
#Write a script that plots the positions of the stations in the station file.
#Input: the stations file


with open(csvpath,"r")as file:
    lines = file.readlines()
    
crsHelper = HCrs() 
crsHelper.from_srid(4326) #from lat long
crsHelper.to_srid(3857) #to 


koordinaten_mit_namen=[]

stations = []  
for line in lines:
    line = line.strip()
    if line.startswith('#')or len(line)==0:
        continue
    lineSplit = line.split(",")
    name=lineSplit[1].strip()
    #converting the coordinates
    long = lineSplit[4].replace("+","")
    longSplit=long.split(":")
    
    long_deg = int(longSplit[0])
    long_min = int(longSplit[1])/60
    long_sec = int(longSplit[2])/3600

    longitude = float(long_deg+long_min+long_sec)
    
    lat = lineSplit[3].replace("+","")
    latSplit=lat.split(":")
    
    lat_deg = int(latSplit[0])
    lat_min = int(latSplit[1])/60
    lat_sec = int(latSplit[2])/3600

    latitude = float(lat_deg+lat_min+lat_sec)
    
    
    stationPoint = HPoint(longitude,latitude)
    
    stations.append(stationPoint)
    
    koordinaten_mit_namen.append((name, longitude, latitude))

    
canvas = HMapCanvas.new()
 
osm= HMap.get_osm_layer()
canvas.set_layers([osm])

TransStations =[]

for item in stations:
    point3857 = crsHelper.transform(item)
    TransStations.append(point3857)
    canvas.add_geometry(point3857,'red',1)
    

canvas.set_extent([-1000000, 4000000, 5000000, 10000000])
canvas.show()

# print(f" point transformed is {point3857}")


#from 4326 to 3857

######################################################################

#count stations in countries:

stationDic ={}
country=[]
for line in lines:
    line = line.strip()
    if line.startswith('#')or len(line)==0:
        continue
    lineSplit = line.split(",")
    #print(line)
    countries = lineSplit[2]
    country.append(countries)
    
for character in country:
    
    count =stationDic.get(character,0)
    count +=1
    stationDic[character]=count
    
for key,value in stationDic.items():
    print(f"{key}:{value}")

#######################################################################

#03 
# write a script to get the nearest station as a result
# use the distance function

entfernungen = []

university = HPoint(11.34999, 46.49809)
for station in stations:
    entfernung = university.distance(station)
    entfernungen.append(entfernung)
    
closest_station_e = entfernungen.index(min(entfernungen))
closest_station = stations[closest_station_e]

print("Closest station:", closest_station)
# print("Distance:", min(entfernungen))

#############################
# name of the closests station

longstation = closest_station.x
latstation = closest_station.y

print(longstation)
print(latstation)

for line in koordinaten_mit_namen:
    
    if longstation == line[1]:
        if latstation == line[2]:
            print("name of the closest station is", line[0])
   

#########################################################################

#04 
# define again a coordinate and a redius and find all stations within this buffer
# buffer in lat and long -> transform to degrees....
# choose a projection  3857 convert the point to the and buffer by 10000
#convert tstations also to the same projection


randompoint =HPoint(11.34999, 46.49809)

transrandompoint = crsHelper.transform(randompoint)


radius = 20000 #related to the projection system
listwithin =[]

bufferarea = transrandompoint.buffer(radius)


#stations in lat and long
#TransStations

for stat in TransStations:
    if bufferarea.contains(stat):
        listwithin.append(stat)
    else: continue

print("stations within the bufferarea")
print(listwithin)
    
######################
#name of the stations within a distance
transformedwithin =[]

for item in listwithin:
    backwithin = crsHelper.transform(item, inverse = True) 
    transformedwithin.append(backwithin)


print("transformed within the bufferarea")
print(transformedwithin)


longiii =[]
latiii=[]
for points in transformedwithin:
    longiii.append(points.x)
    latiii.append(points.y)
    
    
# longiii and latiii are now the back transformed koordinates for the stations within the buffer
print("longiii is")
print(longiii)
print("latiii is")
print(latiii)

counter =0
print(longiii[counter])

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#can access the single koordinates but cant find them then in the list

stationnames=[]
count = 0

for line in koordinaten_mit_namen:
    if  line[1]== longiii[count] and line[2] == latiii[count]:
        stationnames.append(line[0])
    else:
        continue
    count+= 1
        
print("name of the stations within the buffer are:")
print (stationnames)


print(koordinaten_mit_namen[:10])


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# longsta = longiii[1]
# latsta = latiii[1]

# print(longsta)
# print(latsta)

# for line in koordinaten_mit_namen:
    
#     if longsta == line[1]:
#         if latsta == line[2]:
#             print("name of the closest station is", line[0])