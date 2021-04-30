import json

with open('..\\routers.json','r') as json_file:
    ourjson = json.load(json_file)
    print(ourjson)

