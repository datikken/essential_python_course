import json

f = open('tmp_files/into_to_python.txt', 'r')
content = f.readlines()
data = {}
data['course'] = []

for line in content:
    data['course'].append({
        'link': line,
    })

file_to_save = 'tmp_files/data.json'

with open(file_to_save, 'w') as outfile:
    json.dump(data, outfile)