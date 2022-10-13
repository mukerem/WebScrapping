import json
import pandas as pd
df = pd.read_csv(r'all_bussiness_directory_list_v1.csv')
result = df.to_json(orient="records")
data = json.loads(result)
h = open("all_bussiness_directory_list_v1.json", "w")
h.write(json.dumps(data, indent=4))
h.close()
print(len(data))
pure = []
phone = []
s_no = 1
remove_phone = []
for contact in data:
    if contact["sms"] == 0:
        remove_phone.append(contact['mobile'])
        continue
    if contact['mobile'] in remove_phone:
        continue
    contact.pop("sms")
    contact["S.No"] = s_no
    s_no += 1
    pure.append(contact)
    phone.append(contact["mobile"])
h = open("all_bussiness_directory_list_v2.json", "w")
h.write(json.dumps(pure, indent=4))
h.close()
print(len(pure))
df = pd.read_json (r'all_bussiness_directory_list_v2.json')
df.to_csv (r'all_bussiness_directory_list_v2.csv', index=False)

# index = ['S.No', 'Company Name', 'Contact', 'Category']