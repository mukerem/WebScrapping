import csv
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor

# from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriverManager().install()
# driver = webdriver.Chrome()
# driver = webdriver.Chrome()

# Function to get the current height of the document
def get_page_height(driver):
    return driver.execute_script("return document.body.scrollHeight")

@contextmanager
def ignore_errors():
    try:
        yield
    except:
        pass

def read_company_page():
    # Open the JSON file for reading
    with open('gitex_exhibitor_link copy 3.json', 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)
    return data

# Function to scroll to the bottom of the page
def scroll_to_bottom(driver):
    old_position = driver.execute_script("return window.pageYOffset;")
    scroll = 0
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new page segments to load (if any)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer")))  # Replace with a suitable condition

        # Calculate new scroll position and compare with last scroll position
        new_position = driver.execute_script("return window.pageYOffset;")
        if new_position == old_position:
            break
        old_position = new_position
        print(scroll)
        scroll += 1


def load_company_page():

    options = Options()
    options.headless = True
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 2,
        "profile.default_content_settings_state.automaticDownloads": 0,
        "javascript.enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(300)  # Set timeout to 300 seconds
    driver.set_window_size(1280, 720)

    driver.get('https://exhibitors.gitex.com/gitex-global-2023/Exhibitor/')

    # Call the function to perform the scroll
    # scroll_to_bottom(driver)

    previous_heights = []
    scroll = 0

    # Loop to scroll until the end of the page
    while True:

        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new data to load
        time.sleep(5)  # Adjust the sleep time as needed

        # Get the new height after the scroll
        current_height = get_page_height(driver)

        # print(previous_heights, current_height)
        # # Check if we are at the bottom of the page
        # if previous_heights.count(current_height) > 20:
        #     break  # Exit the loop if we've reached the bottom

        # # Store the current page height after the scroll
        # previous_heights.append(current_height)
        scroll += 1
        print(scroll, current_height)

        
        elements = driver.find_elements(By.CLASS_NAME, 'button_block')

        # loop through the elements and perform some action
        exhibitors = []
        c = 1
        # print(elements)
        for div in elements:
            anchor = div.find_element(By.TAG_NAME, 'a')
            link = anchor.get_attribute('href')
            exhibitors.append(link)
            # print(c, link)
            c += 1
        
        with open("gitex_exhibitor_link.json", "w") as f:
            json.dump(exhibitors, f, indent=4)

    return exhibitors

def detail_page(url):

    options = Options()
    options.headless = True
    prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 720)

    driver.get(url)

    company_name, website, address, country = [None] * 4

    with ignore_errors():
        contact = driver.find_element(By.CLASS_NAME, 'company_description')
        
    with ignore_errors():
        company_name = contact.find_element(By.CLASS_NAME, 'list-group-item-heading').text
        
    with ignore_errors():
        media_element = contact.find_element(By.CLASS_NAME, 'social_media_block')
        website = media_element.find_elements(By.TAG_NAME, "li")[0].find_element(By.TAG_NAME, "a").get_attribute("href")
    # with ignore_errors():
    #     email_to = contact.find_element(By.CLASS_NAME, 'company-profile-section__link--email').get_attribute("href")
    #     email = email_to.split(':')[1]
        
    # with ignore_errors():
    #     phone = contact.find_element(By.CLASS_NAME, 'company-profile-section__company-phone').text
    
    with ignore_errors():
        address_section = driver.find_element(By.CLASS_NAME, 'head_discription')
        address_section = address_section.find_elements(By.TAG_NAME, 'p')
        address = address_section[0].text
        country = address_section[1].text

    driver.quit()

    data = {
        "Name": company_name,
        # "Email": email,
        "Address": address,
        "Country": country,
        "Website": website
    }
    return data

def load_exhibitors():
    with open("gitex_exhibitor_contact.json", "r") as f:
        return json.load(f) or []

def save_to_file(exhibitors_contact):

    data = json.dumps(exhibitors_contact, indent=4)

    with open("gitex_exhibitor_contact.json", "w") as f:
        f.write(data)

    with open('gitex_exhibitor_contact.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=exhibitors_contact[0].keys())
        writer.writeheader()
        writer.writerows(exhibitors_contact)

# exhibitors = load_company_page()
exhibitors = read_company_page()
exhibitors_contact = []
exhibitors_contact = load_exhibitors()
total_companies = len(exhibitors)
DIVIDE = 5
for step in range(total_companies // DIVIDE):
    data = exhibitors[step * DIVIDE: (step + 1) * DIVIDE]
    with ThreadPoolExecutor(max_workers=10) as executor:
        result = list(executor.map(detail_page, data))
        exhibitors_contact.extend(result)
        save_to_file(exhibitors_contact)
    print(f"part {step} finished")