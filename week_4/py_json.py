# Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.

import json
from data import data1

array = [["DN", "Description", "Speed", "MTU"], ['-' * 50, '-' * 20, '-' * 10, '-' * 10]]
print('Interface Status')
print('=' * 100)

data_1 = dict(json.loads(data1))
for value in data_1["imdata"]:
    arruy = []
    dict1 = value["l1PhysIf"]["attributes"]

    arruy.append(dict1["dn"])
    arruy.append(dict1["descr"])
    arruy.append(dict1["speed"])
    arruy.append(dict1["mtu"])

    array.append(arruy)

for i in array:
    num = 0
    for j in i:
        print(j, ' ' * (len(array[1][num]) - len(j)), end=' ')
        num += 1
    print()