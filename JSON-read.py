#Author = Vignesh Goutham
import json

jsonfile = open("network-pairs.json","r+")
jsondata = ""
for line in jsonfile:
    jsondata += line
parsed_data = json.loads(jsondata)

print(parsed_data['network_pair'][0]['source'])
