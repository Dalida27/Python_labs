import json

with open('data-json.json') as some_file:
    data = json.load(some_file)

print("Interface Status")
print("=" * 80)
print("{:<50}{:<20}{:<8}{:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for i in data['imdata']:
    attributes = i['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print("{:<50}{:<20}{:<8}{:<6}".format(dn, description, speed, mtu))