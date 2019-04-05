import json

with open(r'C:\Users\aprabhakar\Desktop\snakes\testDAT\notext\predictions.jsonl') as json_file:
    data = json.load(json_file)
    # print(data[1])
    for e in data:
        print(e['Classes'])
        # print(e['Classes'][0]['Name'])

