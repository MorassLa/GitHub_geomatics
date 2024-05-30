folder = r"C:\Users\laura\OneDrive - Scientific Network South Tyrol\Documents\Master\Semester2\3.advanced geomatics\GitHub"

from pyqgis_scripting_ext.core import *

#long than lat

#Folien02:
# 00-Draw geometries on a map canvas
#with exotring the coordinates from a csv file


csvPath = f"{folder}/datasets/02_exe0_geometries.csv"
with open(csvPath,"r")as file:
    lines = file.readlines()
    
    
mypoints=[]
mylines=[]
polygons=[]

canvas = HMapCanvas.new()

    
for line in lines:
    line = line.strip()
    lineSplit = line.split(";")
    
    if lineSplit [0] == 'point':
        mypoint= lineSplit [1]
        long = float(mypoint[:4])
        lat = float(mypoint[5:])
        pointi = HPoint(long,lat)


    if lineSplit [0] == 'line':
        myline = lineSplit[1].split(" ")
        pointList=[]
        for item in myline:
            coord_lines =item.split(",")
            print(coord_lines)
            longline = float(coord_lines[0])
            latline = float(coord_lines[1])
            
            
            mylines.append([longline, latline])
        linii = HLineString.fromCoords(mylines)
        
        
    if lineSplit[0]=='polygon':
        mypolygon = lineSplit[1].split(" ")
        mypolygons=[]
        for item in mypolygon:
            coord_poly=item.split(",")
            longpoly=float(coord_poly[0])
            latpoly=float(coord_poly[1])
            mypolygons.append([longpoly,latpoly])
        polygon=HPolygon.fromCoords(mypolygons)
        polygons.append(polygon)


canvas.add_geometry(pointi, 'black',8)
canvas.add_geometry(linii, 'blue',2)
for poly in polygons:
    canvas.add_geometry(poly, 'red',1)
        
canvas.set_extent([-1, -1, 50, 50])
canvas.show()


'''data = [
['point', '30.0,10.0', '1']
['line', '31,11 10,30 20,40 40,40', '1']
['polygon', '32,12 10,20 20,39 40,39 32,12', '1']
['polygon', '15,5 40,10 10,20 5,10 15,5', '2']
['line', '40,40 30,30 40,20 30,10', '2']
]'''


# 01- create an UTM grid


# rechteck = HPolygon.fromCoords([[0, 0], [0, 800], [6, 800], [6, 0], [0, 0]])
# rechteck2 = HPolygon.fromCoords([[6, 0], [6, 800], [12, 800], [12, 0], [6, 0]])

# canvas2 = HMapCanvas.new()

# canvas2.add_geometry(rechteck, 'red',1)
# canvas2.add_geometry(rechteck2, 'red',1)
        
# canvas2.set_extent([-1, -1, 800, 800])
# canvas2.show()


breite =6
hohe =180

startx =0
starty =0

canvas3 = HMapCanvas.new()

for item in range(60):
    koordinaten =[
        [startx, starty],
        [startx, starty+hohe],
        [startx+breite, starty+hohe],
        [startx+breite, starty],
        [startx, starty]]
    
    rechteck = HPolygon.fromCoords(koordinaten)
    
    canvas3.add_geometry(rechteck,'red',1)
    startx += breite
       
canvas3.set_extent([-10, -10, 370, 190])
canvas3.show()

##################################
#other way from lecture:


# extent =6
# polygons=[]

# for lon in range (-180,180, extent):
#     minX=long
#     maxX = lon+extent
#     minY = -84
#     maxY =84
    
#     coords = [[minX,minY],[minX,maxY],[maxX,maxY],[maxX,minY], [minX,minY]]
#     polygon=HPolygon.fromCoords[coords]
#     polygons.append(polygon)
    
# canvas5 =HMapCanvas.new()

# canvas5.add_geometry(polygons,'red',1)

# canvas5.set_extent([-180, -84,180,84])
# canvas5.show()






