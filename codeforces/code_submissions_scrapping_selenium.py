import requests
import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/usr/bin/chromedriver')
PYTHON = {'Python 2', 'PyPy 3', 'PyPy 2', 'Python 3'}
CPP = {'GNU C11', 'GNU C++11', 'GNU C', 'MS C++ 2017', 'MS C++', 'GNU C++14', 'GNU C++17'}


def get_detail(user, link):
    url = f"https://codeforces.com{link}"
    data = {"script": "true"}
    page_content = requests.get(url, data=data, cookies=user)
    
    soup = BeautifulSoup(page_content.text, "html.parser")
    header = soup.find('div', attrs={'class': "datatable"}).find('table')
    try:
        problem_name = header.find_all('tr')[1].find_all('td')[2].find('a').text.strip()
    except IndexError:
        print(link)
        problem_name = link 
    try:
        code = soup.find('pre', attrs={'id': "program-source-text"}).contents[0]
    except:
        print(link, 2)
        return None, None
    return problem_name, code

def popup_page(popup, driver):
    main_window_handle = None
    while not main_window_handle:
        main_window_handle = driver.current_window_handle
    popup.click()
    print(popup)
    detail_window_handle = None
    while not detail_window_handle:
        print(1, driver.window_handles)
        for handle in driver.window_handles:
            if handle != main_window_handle:
                detail_window_handle = handle
                break
    driver.switch_to.window(detail_window_handle)
    return main_window_handle

def get_submission(username, page=1, status_filter='Accepted'):
    url = f'https://codeforces.com/submissions/{username}/page/{page}'
    driver.get(url) 
    element = driver.find_elements(By.XPATH, "//*[@class= 'status-frame-datatable']/tbody/tr")
    
    for row in element[1:]:

        col = row.find_elements(By.XPATH, 'td')
        main_window_handle = popup_page(col[0], driver)
        detail_content = driver.find_element(By.ID, "facebox")
        print(detail_content)
        driver.switch_to.window(main_window_handle)
    
    return
    data = {"script": "true"}
    page_content = requests.get(url, data=data, cookies=user)
    soup = BeautifulSoup(page_content.text, "html.parser")

    table = soup.find('table', attrs={"class": "status-frame-datatable"})
    rows = table.find_all('tr')[1:]

    pagination = soup.find_all('span', attrs={"class": "page-index"})
    li = pagination[-1].find('a').text.strip()
    if li.isdigit():
        if page > int(li):
            return False
    else:
        return False
    print(f'page {page} contains {len(rows)} submissions')
    duplicate = []

    for row in rows:
        cols = row.find_all('td')
        print(cols[0])
        btn_onclick=cols[0]['onclick']
        # a = cols[0].click()
        print(btn_onclick)
        try:
            link = cols[0].find('a').get('href')
        except:
            print(cols[0])
            continue
        cols = [ele.text.strip() for ele in cols]
        submission_id = cols[0]
        time = cols[1]
        title = cols[3]
        language = cols[4]
        status = cols[5]
        if 'on test' in status or 'on pretest' in status:
            status = ' '.join(status.split()[:-3])
        
        if not status == status_filter:
            continue
        if title in duplicate:
            continue
        
        if language in PYTHON:
            language = "Python"
        elif language in CPP:
            language = "C++"

        problem_name, code = get_detail(user, link)
        if code == None:
            continue
        original_title = title
        title = '_'.join(title.split()[1:])
        file_name = [title, problem_name]
        file_name = '_'.join(file_name).replace('-', '_').replace(' ', '_').replace('.', '_').replace('__', '')
        header = ""
        if language == "Python":
            header += f'# Time: {time}\n'
            header += f'# Title: {original_title}\n'
            header += f'# Submission ID: {submission_id}\n'
            header += f'# Language: {language}\n\n\n'
            code = header + code
            file_name += '.py'
        elif language == "C++":
            header += f'// Time: {time}\n'
            header += f'// Title: {original_title}\n'
            header += f'// Submission ID: {submission_id}\n'
            header += f'// Language: {language}\n\n\n'
            code = header + code
            file_name += '.cpp'
        open(f"archive/{file_name}", "w").write(code)
        duplicate.append(title)
    return True

def download_submission(username):
    page = 1
    cont = True
    while cont:
        cont = get_submission(username, page)
        page += 1

username = "mukeremali"
download_submission(username)

driver.close()
 

# error_types = {'Time limit exceeded', 'Wrong answer', 'Accepted', 'Hacked', 'Compilation error', 'Memory limit exceeded', 'Runtime error'}
# languages = {'GNU C11', 'GNU C++11', 'GNU C', 'MS C++ 2017', 'Python 2', 'PyPy 3', 'MS C++', 'PyPy 2', 'Python 3', 'GNU C++14', 'GNU C++17'}