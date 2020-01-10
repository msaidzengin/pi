import json

with open(r"result1m.json", "r") as read_file:
    phones = json.load(read_file)


with open("result2.txt", "w") as text_file:
    for i in phones:
        text_file.write(i['phone'] + ' ' + str(i['index']) + '\n')
