import json

file="data.txt"

dict = {}

with open(file) as fn:
  for d in fn:
    key,desc = d.strip().split(None,1)
    dict[key]=desc.strip()

otfile = open("output.json","w")
json.dump(dict,otfile)
otfile.close()