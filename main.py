import json

from laba2 import Information
from merge_sort import merge_sort

with open('correct_data.txt', 'r') as file_read:
    data = json.load(file_read)

data = merge_sort(data)
with open('sort_json.txt', 'w') as sort_json:
    sort_json.write(json.dumps(data))

result_data = []
for inf in data:
    result_data.append(inf)
print(result_data[0])
with open('sort_json.json', 'w') as f:
    json.dump(result_data, f)

with open('sort_json.json', 'r') as f:
    data_new = json.load(f)
print(data_new)