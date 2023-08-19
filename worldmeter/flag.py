import json
import requests
from bs4 import BeautifulSoup


def extract_flag():
    base_url = "https://www.worldometers.info/"
    url = f"{base_url}/geography/flags-of-the-world/"
    data = {"script": "true"}
    page_content = requests.get(url, data=data)
    soup = BeautifulSoup(page_content.text, "html.parser")
    all_countries = soup.find_all('div', attrs={'class': 'col-md-4'})[:-1]
    countries = []

    for country in all_countries:
        country = country.find_all('div')[0]
        country_name = country.find('div').text.strip()
        flag_url =f"{base_url}/{country.find('a').get('href')}"
        response = requests.get(flag_url)
        with open(f"flag/{country_name}.gif", "wb") as f:
            f.write(response.content)
        countries.append(country_name)
        # print(country_name)

    with open("country.json", "w") as f:
        json.dump(countries, f, indent=4)
extract_flag()