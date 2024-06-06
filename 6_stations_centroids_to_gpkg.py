folder = r"C:\Users\laura\OneDrive - Scientific Network South Tyrol\Documents\Master\Semester2\3.advanced geomatics\GitHub"
csvpath = f"{folder}/datasets/stations.txt"
geopackagePath=r"C:\Users\laura\Desktop\natural_earth_vector.gpkg\packages\natural_earth_vector.gpkg"
tmpfolder = r"C:\Users\laura\OneDrive - Scientific Network South Tyrol\Documents\Master\Semester2\3.advanced geomatics\GitHub\tmp"
from pyqgis_scripting_ext.core import *

# cleanup
HMap.remove_layers_by_name(["OpenStreetMap", "stations","centroids", "ne_50m_admin_0_countries"])


osm=HMap.get_osm_layer()
HMap.add_layer(osm)

#convert station to geopackage 

with open (csvpath,'r')as file:
    lines = file.readlines()

# name of the field and type of value -> bule print of attribute table

schema={
    "stationid":"int",
    "name": "string",
    "country":"string",
    "height":"double"
}
#create memory laxer with this schema
stationsLayer = HVectorLayer.new("stations","Point","EPSG:4326", schema)



for line in lines:
    line =line.strip()
    
#parce the file to get the information out of the file
#get the geometry

    if not line.startswith("#"):
        lineSplit = line.split(",")
        
        longString = lineSplit[4]
        
        longSplit=longString.split(":")
    
        long_deg = int(longSplit[0])
        long_min = int(longSplit[1])/60
        long_sec = int(longSplit[2])/3600

        longitude = float(long_deg+long_min+long_sec)
    
        latString =lineSplit[3]
    
        lat = lineSplit[3].replace("+","")
        latSplit=lat.split(":")
    
        lat_deg = int(latSplit[0])
        lat_min = int(latSplit[1])/60
        lat_sec = int(latSplit[2])/3600

        latitude = float(lat_deg+lat_min+lat_sec)
        
        
        point =HPoint (longitude,latitude)
        
        attributes = [
            int(lineSplit[0]),
            lineSplit[1],
            lineSplit[2],
            lineSplit[-1]
        ]
        
        stationsLayer.add_feature(point,attributes)
    #print(line)


HMap.add_layer(stationsLayer)

outputPath =f"{tmpfolder}/stations.gpkg"

stationsLayer.dump_to_gpkg(outputPath, overwrite=True)

#dumpedStationsLayer = HVectorLayer.open(outputPath,"stations")
#HMap.add_layer(dumpedStationsLayer)


########################################################################################################
#centroids

schema2={"name":"string"}

centroidsLayer =HVectorLayer.new("centroids" ,"Point","EPSG4326", schema2 )
countryLayer = HVectorLayer.open(geopackagePath,countriesName)
nameIndex= countryLayer.field_index ("NAME")

nonInCountryList =[]

for country in countryLayer.features():
    countryGeom = country.geometry
    name = country.attributes[nameIndex]
    
    centroid = countryGeom.centroid()
    
    centroidsLayer.add_feature(centroid, [name])
    
    if not centroid.intersects(countryGeom):
        nonInCountryList.append(name)
 
 
 
simpleStyle= HMarker("circle",10)+ HLabel("name") + HHalo()
centroidsLayer.set_style(simpleStyle)

HMap.add_layer(centroidsLayer)
print("these countries have there centroid outside:")
for c in nonInCountryList:
    print(c)
##############################################################################
#create geopackage for centroids


output_path = f"{tmpfolder}/centroids.gpkg"
error = centroidsLayer.dump_to_gpkg(output_path, overwrite=True)
if(error):
    print(error)
    
    
    
###########################################################################################################
#add colour range for population
countriesName = "ne_50m_admin_0_countries"
countriesLayer=HVectorLayer.open (geopackagePath,countriesName)

ranges = [
    [80000000, float('inf')],
    [1000000, 80000000],
    [float('-inf'),1000000]
]
styles=[
    HFill("255,0,0,70"),
    HFill("0,255,0,70"),
    HFill("0,0,255,70")
]

lableStyle = HLabel ("POP_EST")+HHalo()
countriesLayer.set_graduated_style ("POP_EST", ranges, styles, lableStyle)
HMap.add_layer(countriesLayer)



  