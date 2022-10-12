import json
import glob

a = []
json_list = [f for f in glob.glob("*.json") if 'contact' in f]
phone = []
for path in json_list:
    f = open(path, "r")
    data = json.load(f)
    f.close()
    for mobile in data:
        if mobile[:5] != '+2519':
            continue
        if mobile in phone:
            continue
        
        temp = {
            "mobile": mobile,
            "name": data[mobile][0],
            "category": data[mobile][1]
        }
        a.append(temp)
h = open("all_bussiness_directory_list.json", "w")
h.write(json.dumps(a, indent=4))
h.close()

import pandas as pd
df = pd.read_json (r'all_bussiness_directory_list.json')
df.to_csv (r'all_bussiness_directory_list.csv', index = ['Company Name', 'Contact', 'Category'])