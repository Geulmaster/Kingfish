from collections import OrderedDict

obj = OrderedDict()
obj["name"] = "Serjio"
obj["age"] = 100

for i, v in obj.items():
    print(i+":", v)