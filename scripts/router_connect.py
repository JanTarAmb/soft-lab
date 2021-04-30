import json

interface = []

with open('..\\routers.json','r') as json_file:
    router_json = json.load(json_file)

for router in router_json.values():
    interface.append(f"ssh {router['user']['name']}:{router['user']['password']}@{router['mgmt_ip']} -p {router['port']}")
    
print(interface)