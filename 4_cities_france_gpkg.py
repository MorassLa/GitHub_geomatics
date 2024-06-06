from pyqgis_scripting_ext.core import *
# load 3 layers of the geopackage in a project
 #cultural: ne_50m_admin_0_countries
 #cultural: ne_50m_populated_places
 #physical: ne_10m_rivers_lake_centerlines_scale_rank
 
# start working in the real map getting away from mapcanvas

#clean up to remove all old layers
#to have no problem while reloading
HMap.remove_layers_by_name(["OpenStreetMap"])



folder=r"C:\Users\laura\Desktop\natural_earth_vector.gpkg\packages"

geopackagePath = folder+ r"\natural_earth_vector.gpkg" 
countriesName = "ne_50m_admin_0_countries"

citiesName = "ne_50m_populated_places"

#add openstreet map layer
osm=HMap.get_osm_layer()
HMap.add_layer(osm)


#access schema
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

print("Schema (first 4 fields):")
counter = 0
for name, type in countriesLayer.fields.items():
    counter += 1
    if counter < 5:
        print("\t", name, "of type", type)

#further information
crs = countriesLayer.prjcode
print("Projection: ", crs)
print("Spatial extent: ", countriesLayer.bbox())
print("Feature count: ", countriesLayer.size()) #polygon records, number of features

#access the data from Italy

print("\nAttributes for Italy:")
countriesFeatures = countriesLayer.features() #returns a list of all features without any filter
nameIndex = countriesLayer.field_index("ADMIN") # there is a field called name with 19 values, this is key sensitive
# fieldNames = countriesLayer.field_names 

for feature in countriesFeatures:
    name=feature.attributes[nameIndex]
    if name =="Italy":
        geometry = feature.geometry # get the geometry
        print("GEOM:", geometry.asWkt()[:50] + "...")
################################################################

    if name == "France":
        geometryfrance = feature.geometry # get the geometry
        print("GEOM:", geometryfrance.asWkt()[:50] + "...")


#########################################################################################

#02- exercise find cities inside france and print the names with intersection
# print("\nStart with France")


####### transform and show France
crsHelper = HCrs() 
crsHelper.from_srid(4326) #from lat long
crsHelper.to_srid(3857) #to 

transfrance = crsHelper.transform(geometryfrance)

#### extract citie coordinates
citiesLayer = HVectorLayer.open(geopackagePath, citiesName)

citiesFeatures = citiesLayer.features() #returns a list of all features without any filter
citynameIndex = citiesLayer.field_index("NAME")


crsHelper = HCrs() 
crsHelper.from_srid(4326) #from lat long
crsHelper.to_srid(3857) #to 


citiesfrance=[]
koordcitiesfrance=[]
for feature in citiesFeatures:
        geometry = feature.geometry # get the geometry
        
        transcity = crsHelper.transform(geometry)
        
        if transcity.intersects(transfrance):
            citiesfrance.append(feature.attributes[citynameIndex])
            koordcitiesfrance.append(transcity)
            #print(transcity)
            
            


print("cities in France:")
print(citiesfrance)
#print(koordcitiesfrance[:20])



canvas = HMapCanvas.new()
osm= HMap.get_osm_layer()
canvas.set_layers([osm])
HMap.add_layer(osm)
canvas.add_geometry(transfrance,'red',1)
canvas.add_geometry(transcity,'blue',4)
canvas.set_extent(transfrance.bbox())
canvas.show()




    
