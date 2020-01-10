import json

with open(r"result1m.json", "r") as read_file:
    phones = json.load(read_file)


search = '5559991122'
for phone in phones:
    if search == phone['phone']:
        print('found', phone)