folder = r"C:\Users\laura\OneDrive - Scientific Network South Tyrol\Documents\Master\Semester2\3.advanced geomatics\GitHub"

#Exercise1
print("\nEXERCISE 1\n")
age = 25
name = "Mario Rossi"
activity = "skating"
job = "engineer"
print(f"Hei,I am {name}\nI am {age} and I love to go {activity}\nI work as an {job}")

#Exercise2
print("\nEXERCISE 2\n")
csvPath = f"{folder}/datasets/01_exe2_data.csv"
with open(csvPath,"r")as file:
    lines = file.readlines()
for line in lines:
   # print(line)
   #remove white spaces from end and beginning
    line = line.strip()
    lineSplit = line.split(";")
   # print(lineSplit)
   #pickout the numbers 
    analogString = lineSplit[0]
    analogSplit = analogString.split(":")
    x1 = float(analogSplit[1])
   
    
    maxvoltageString = lineSplit[1]
    y2 = float(maxvoltageString[11:])
    
    maxanalogString = lineSplit[2]
    x2 = float(maxanalogString.split(":")[1])
   # print(x1, y2, x2)
    
    #final mathematical operation
    #x2/x1 = y2/y1
    y1 =y2*x1/x2
    #convert stings to numbers
    #insert up float()
    print(f"analogreading:{x1},maxvoltage: {y2}, maxanalog: {x2}, result: {y1}")
    
#Exercise3
print("\nEXERCISE 3\n")
string = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s"
repString = string.replace(",",";")
print(repString)

#Exercise4
print("\nEXERCISE 4\n")
list = [ 1, 2, 3, 4, 5]
for i in list:
    print(i)


#Exercise5
print("\nEXERCISE 5\n")
list2 = [ 1, 2, 3, 4, 5]
for i in list2:
     print(f"Number {i}")
     
#Exercise6
print("\nEXERCISE 6\n")
list3 = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
listb = list3[:5]
for i in listb:
    print(f"Number {i}")

#Exercise7
print("\nEXERCISE 7\n")
list4 = [1, 2, 3, 4, 5]
list5 = ["first", "second", "third", "fourth", "fifth"]
for a,b in zip(list4,list5):
    print(f"{b} is {a}")
    
#Exercise8
print("\nEXERCISE 8\n")
string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
 nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
 pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
 culpa qui officia deserunt mollit anim id est laborum."""
 
words=len(string.split())
print(f"Word count: {words}")
print(f"Characters count: {len(string)}")

textwithout = string.replace(" ","")

print(f"Characters count without spaces:{len(textwithout)}")


#Exercise9
print("\nEXERCISE 9\n")

csv_path =f"{folder}/datasets/01_exe9_data.csv"
with open(csv_path,"r")as file:
    lines = file.readlines()   

for line in lines:
   #remove white spaces from end and beginning
    line = line.strip()
    if line.startswith('#')or len(line)==0: #ignore these lines
        continue
    print(line)
    

#Exercise10
print("\nEXERCISE 10\n")


for line in lines:
    line = line.strip()
    if line.startswith('#')or len(line)==0 or float(line[3:])>1000:
        continue
    print(line)



#Exercise11
print("\nEXERCISE 11\n")

csv_path=f"{folder}/datasets/01_exe11_data.csv"
with open(csv_path,"r")as file:
    lines=file.readlines()

for line in lines:
    line=line.strip()
    lineSplit=line.split(";")
    
    baseString =lineSplit[0]
    base = baseString[5:-2]
    #print(base)
    
    heightString = lineSplit[1]
    height=float(heightString[7:])
    height = height *100
    #print(height)
    
    result=float(base)*float(height)/2
    #print(result)
    
    print(f"base * height / 2 = {base} * {height}/2 = {result}cm2")
    


#Exercise12
print("\nEXERCISE 12\n")

    
who = {
    "Daisy": 11,
    "Joe": 201,
    "Will": 23,
    "Hanna": 44
 }
what = {
    44: "runs",
    11: "dreams",
    201: "plays",
    23: "walks"
 }
where = {
    44: "to town.",
    11: "in her bed.",
    201: "in the livingroom.",
    23: "up the mountain."
 }
    
for key, value in who.items():
    activity =what.get(value,"unknown activity")
    location =where.get(value, "unknown location")
    
    print(f"{key} {activity} {location}")
    
    
#Exercise12
print("\nEXERCISE 12\n")
    
who = {
    "Daisy": 11,
    "Joe": 201,
    "Will": 23,
    "Hanna": 44
 }
what = {
    44: "runs",
    11: "dreams",
    201: "plays",
    23: "walks"
 }
where = {
    "runs": "to town.",
    "dreams": "in her bed.",
    "plays": "in the livingroom.",
    "walks": "up the mountain."
 }

for key, value in who.items():
    activity =what.get(value,"unknown activity")
    location =where.get(activity, "unknown location")
    
    print(f"{key} {activity} {location}")


#Exercise13
print("\nEXERCISE 13\n")

list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["c", "d", "e", "f", "g", "h", "a"]
list3 = ["c", "d", "e", "f", "g"]
list4 = ["c", "d", "e", "h", "a"]


list1.extend(list2)
list1.extend(list3)
list1.extend(list4)
print(list1)

    
#print(f" count of a = {list1.count('a')}")
charDic ={}
for character in list1:
    count =charDic.get(character,0)
    count +=1
    charDic[character]=count
for key,value in charDic.items():
    print(f"count of {key} ={value}")



#Exercise14
print("\nEXERCISE 14\n")

csvPath = f"{folder}/datasets/stations.txt"
with open(csvPath,"r")as file:
    lines=file.readlines()


print(lines[:20])

#Exercise15
print("\nEXERCISE 15\n")

print(f"count of stations = {len(lines)}")


#Exercise16
print("\nEXERCISE 16\n")

for line in lines[:5]:
    lineStrip = line.strip()
    lineSplit = lineStrip.split(",")
    if line.startswith('#')or len(line)==0:
        continue
print(f"count of columns = {len(lineSplit)}")
    
    
#Exercise17
print("\nEXERCISE 17\n")


for line in lines[:20]:
    lineStrip = line.strip()
    lineSplit = lineStrip.split(",")
    stationId=lineSplit[0]
    stationname=lineSplit[1]
    if line.startswith('#')or len(line)==0:
        continue
   
    print(stationId, stationname)
    

#Exercise18
print("\nEXERCISE 18\n")

summe=0
for line in lines:
    lineStrip = line.strip()
    lineSplit = lineStrip.split(",")
    if line.startswith('#')or len(line)==0:
        continue
    summe += float(lineSplit[5])
print(summe)
print (len(lines))
averageh=summe/len(lines)
print(f"average height= {averageh}")



#Exercise19
print("\nEXERCISE 19\n")

with open(csvPath,"r")as file:
    lines=file.readlines()
    
#available fields
    
for line in lines[:1]:
    lineStrip = line.strip()
    lineSplit = lineStrip.split(",")
    
line0= lineSplit[:5]
print(line0)


    
#first lines
for line in lines:
    lineStrip = line.strip()
    lineSplit = lineStrip.split(",")
linesfirst4=lines[:5]

print(f"File info: {csvPath[-12:]}\n{'-'*25}")
print(f"Stations count: {len(lines)}\nAverage value: {averageh}\nAvailable fields:")
print("First data lines:")
print(linesfirst4)


#Exercise20
print("\nEXERCISE 20\n")
  
def fileSummary(path,idFieldName, avgFieldName):
    with open(path,'r')as file:
        lines=file.readlines()
        
        
    idIndex = None
    analyzeIndex =None
    hSum=0
    count=0
    uniqueIdsList=[]
    
    for line in lines:
        line=line.strip()
        if line.startswith("#"):
            #we have the header and want the fields
            fields = line.strip("#").split(",")
            
            for index, field in enumerate(fields):
                field = field.strip()
                if field == idFieldName:
                    idIndex = index
                elif field == avgFieldName:
                    analyzeIndex = index
                    
        else:
            #here data starts
            lineSplit = line.split(",")
            value = float(lineSplit[analyzeIndex])
            if value != -9999:
                hSum += value
                count+= 1
                
            idValue = lineSplit[idIndex]
            if idValue not in uniqueIdsList:
                uniqueIdsList.append(idValue)
    
   # print(idIndex, analyzeIndex)
    
    
    avg=hSum/count
    print(f"File info:{path}")
    print("=============")
    print(f"Distinct count of filed {idFieldName}: {len(uniqueIdsList)}")
    print(f"Average value of field {avgFieldName}:{avg}")
    print("Fields:")
    for field in fields:
        print(f"-> {field.strip()}")

fileSummary(f"{folder}/datasets/station_data.txt", "STAID","RR")
print("******************")
fileSummary(f"{folder}/datasets/stations.txt", "CN","HGHT")


#Exercise21
print("\nEXERCISE 21\n")

n = 10
m = 5
for item in range(n):
    print(m*"*")
    

#Exercise22
print("\nEXERCISE 22\n")

n=10
counter =1
for item in range(n):
    print (counter*"*")
    counter+=1

#Exercise23
print("\nEXERCISE 23\n")

n=10
counter =10
for item in range(n):
    print (counter*"*")
    counter-=1
    
    
    
# #Exercise24
print("\nEXERCISE 24\n")
a=10
sumcount=0
for item in range(a):
    if item%2 != 0:
       continue
    print(item)
    sumcount+= item
print(sumcount)
    
#Exercise25
print("\nEXERCISE 25\n")

numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]
sumcounter =0
evennumber=[]
for item in numbers:
    if item%2 != 0:
        continue
    sumcounter+= item
    evennumber.append(item)
print(sumcounter)
print(evennumber)

#Exercise26
print("\nEXERCISE 26\n")


csvPath = f"{folder}/datasets/01_exe26_dataset1.csv"
with open(csvPath,"r")as file:
    lines=file.readlines()
print(lines[:5])

print("second dataset")

csvPath2 = f"{folder}/datasets/01_exe26_dataset2.csv"
with open(csvPath2,"r")as file:
    lines2=file.readlines()
print(lines2[:5])

datasetChar1 ={}
for line in lines:
    lineStrip = line.strip()
    lineSplit = lineStrip.split(",")
    if line.startswith("#") or len(line)==0:
        continue
        
    key = lineSplit[0]
    datasetChar1[key] = lineSplit[1:]

datasetChar2 ={}
for line in lines2:
    lineStrip = line.strip()
    lineSplit = lineStrip.split(",")
    if line.startswith("#") or len(line)==0:
        continue
        
    key = lineSplit[0]
    datasetChar2[key] = lineSplit[1:]
    
joined_dataset={}
for key, data1 in datasetChar1.items():
    if key in datasetChar2:
        joined_dataset[key] = data1 + datasetChar2[key]

print("joined datasets")
for key, data in joined_dataset.items():
    print(key, data)
    
    



