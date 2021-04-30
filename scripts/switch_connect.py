import yaml

interface = []

with open('..\\switches.yaml','r') as yaml_file:
    switch_yaml = yaml.safe_load(yaml_file)

for switch in switch_yaml.values():
    interface.append(f"ssh {switch['user']['name']}:{switch['user']['password']}@{switch['mgmt_ip']} -p {switch['port']}")
    
print(interface)