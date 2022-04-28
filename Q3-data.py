import csv
import json

csv_File_Path=input()
json_File_Path=input()

jsonlist=[]

with open(csv_File_Path,'r') as csvf:
    csvReader=csv.DictReader(csvf)
    for row in csvReader:
        jsonlist.append(row)
with open(json_File_Path,'w') as jsonf:
    jsonString=json.dumps(jsonlist,indent=4)
    jsonf.write(jsonString)
    



