import json
import pandas as pd

with open("middle_east_energy_exhibitor_contact.json", "r") as f:
    json_str = f.read()
data = bytes(json_str, "utf-8").decode("unicode_escape")
structured_data = json.loads(data)

# Create DataFrame
df = pd.DataFrame(structured_data)

# Save to CSV with UTF-8 encoding
df.to_csv('middle_east_energy_exhibitor_contact_list.csv', encoding='utf-8', index=False)

with open("middle_east_energy_exhibitor_contact_list.json", "w", encoding='utf-8') as f:
    json.dump(structured_data, f, ensure_ascii=False, indent=4)