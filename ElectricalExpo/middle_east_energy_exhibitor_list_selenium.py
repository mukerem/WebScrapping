import csv
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor

options = Options()
options.headless = True
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
driver.set_window_size(1280, 720)

# driver = webdriver.Chrome()

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

def load_company_page():
    driver.get('https://exhibitors.energy-utilities.com/mee2023/')
    q = 1
    while True:
        print(q)
        button = driver.find_element(By.CLASS_NAME, 'show-more-results')
        if button.is_displayed():
            button.click()
        else:
            break

        q += 1

        # Click the button
        button.click()
    elements = driver.find_elements(By.CLASS_NAME, 'exhibitor-card-details-reveal__profile-link')

    # loop through the elements and perform some action
    exhibitors = []
    c = 1
    for elem in elements:
        link = elem.get_attribute('href')
        exhibitors.append(link)
        print(c, link)
        c += 1
    return exhibitors

def detail_page(url):
    driver.get(url)

    company_name, website, email, phone, country = [None] * 5

    with ignore_errors():
        contact = driver.find_element(By.CLASS_NAME, 'company-profile-section__contact')
        
    with ignore_errors():
        company_name = contact.find_element(By.CLASS_NAME, 'company-profile-section__company-name').text
        
    with ignore_errors():
        website = contact.find_element(By.CLASS_NAME, 'company-profile-section__link--website').get_attribute("href")
    
    with ignore_errors():
        email_to = contact.find_element(By.CLASS_NAME, 'company-profile-section__link--email').get_attribute("href")
        email = email_to.split(':')[1]
        
    with ignore_errors():
        phone = contact.find_element(By.CLASS_NAME, 'company-profile-section__company-phone').text
    
    with ignore_errors():
        address_section = driver.find_element(By.CLASS_NAME, 'company-profile-section__address')
        address = address_section.find_element(By.TAG_NAME, 'p').text
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

counter = 1
for exhibitor in exhibitors:
    data = detail_page(exhibitor)
    exhibitors_contact.append(data)
    print(counter)
    counter += 1

data = json.dumps(exhibitors_contact, indent=4)

with open("middle_east_energy_exhibitor_contact.json", "w") as f:
    f.write(data)

with open('middle_east_energy_exhibitor_contact.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=exhibitors_contact[0].keys())
    writer.writeheader()
    writer.writerows(exhibitors_contact)