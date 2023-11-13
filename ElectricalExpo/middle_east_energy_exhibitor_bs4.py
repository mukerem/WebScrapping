import csv
import json
import requests

from bs4 import BeautifulSoup
from contextlib import contextmanager

@contextmanager
def ignore_errors():
    try:
        yield
    except:
        pass

def read_company_page():
    # Open the JSON file for reading
    with open('middle_east_energy_exhibitor_list.json', 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)
    return data

def detail_page(url):

    company_name, website, email, phone, country = [None] * 5
    data = {"script": "true"}
    page_content = requests.get(url, data=data)
    
    soup = BeautifulSoup(page_content.text, "html.parser")

    with ignore_errors():
        contact = soup.find('div', attrs={'class': 'company-profile-section__contact'})
        
    with ignore_errors():
        company_name = contact.find('span', attrs={'class': 'company-profile-section__company-name'}).text
        
    with ignore_errors():
        website = contact.find('a', attrs={'class': 'company-profile-section__link--website'}).get("href")
    
    with ignore_errors():
        print(contact.find('a', attrs={'class': 'company-profile-section__link--email'}))
        email_to = contact.find('a', attrs={'class': 'company-profile-section__link--email'}).get("href")
        email = email_to.split(':')[1]
        # print(email_to)
        
    with ignore_errors():
        phone = contact.find('span', attrs={'class': 'company-profile-section__company-phone'}).text
    
    with ignore_errors():
        address_section = soup.find('div', attrs={'class': 'company-profile-section__address'})
        address = address_section.find('p').text
        country = address.split("\n")[-1].strip()

    data = {
        "Name": company_name,
        "Email": email,
        "Phone": phone,
        "Country": country,
        "Website": website
    }
    return data

# exhibitors = load_company_page()
exhibitors = read_company_page()
exhibitors_contact = []

for idx, exhibitor in enumerate(exhibitors[:3], 1):
    info = detail_page(exhibitor)
    exhibitors_contact.append(info)
    print(idx)

data = json.dumps(exhibitors_contact, indent=4)

with open("middle_east_energy_exhibitor_contact.json", "w") as f:
    f.write(data)

with open('middle_east_energy_exhibitor_contact.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=exhibitors_contact[0].keys())
    writer.writeheader()
    writer.writerows(exhibitors_contact)