import json
import requests
from bs4 import BeautifulSoup


def get_detail(link):
    url = link
    data = {"script": "true"}
    page_content = requests.get(url, data=data)
    
    soup = BeautifulSoup(page_content.text, "html.parser")

    try:
        name = soup.find('h1', attrs={'class': 'entry-title'}).text.strip()
        table = soup.find('table', attrs={"class": "businessdetails"})
        rows = table.find_all('tr')
    except:
        return None, None

    phone = None
    telephone = []
    for row in rows:
        col = row.find_all('td')
        if 'Mobile' in col[0].text.strip():
            try:
                phone = col[1].text.strip()
                break
            except:
                continue
        elif 'Telephone' in col[0].text.strip():
            try:
                if '+2519' in col[1].text.strip():  
                    telephone.append(col[1].text.strip())
            except:
                continue
    if phone is None and telephone:
        phone = telephone[0]
    return name, phone

def extract_contact():
    url = "https://addisbiz.com/business-directory/shopping?city=Addis%20Ababa"
    data = {"script": "true"}
    page_content = requests.get(url, data=data)
    soup = BeautifulSoup(page_content.text, "html.parser")
    all_categories = soup.find_all('li', attrs={'class': 'categories'})
    all_categories.reverse()
    ORDER = 26

    for category in all_categories[25:]:
        contact = {}
        row = category.find('a')
        count = category.find('span').text.strip().replace('(', '').replace(')','')
        count = (int(count))
        category_name = row.text.strip()
        page_link = row.get('href')
        print(category_name, count)
        page = 1
        while True:
            url = f"{page_link}&page={page}"
            page_content = requests.get(url, data=data)
            soup = BeautifulSoup(page_content.text, "html.parser")
            table = soup.find('div', attrs={'class': 'regularbusinesses'})
            if table == None:
                break
            print('---> page = ', page)
            table = table.findAll('div', attrs={'class':'details'})
            page += 1
            for row in table[:-3]:
                link = row.find('a').get('href')
                name, phone = get_detail(link)
                if name == None or phone == None:
                    continue
                if phone in contact:
                    continue
                contact[phone] = (name, category_name)
        category_name = category_name.replace(' ', '').replace('&', '').replace('/', '')
        files = open(f'contact_{ORDER}_{category_name}.json', 'w')
        files.write(json.dumps(contact, indent=4))
        files.close()
        ORDER += 1
extract_contact()