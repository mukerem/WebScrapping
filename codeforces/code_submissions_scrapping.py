import requests
from bs4 import BeautifulSoup

PYTHON = {'Python 2', 'PyPy 3', 'PyPy 2', 'Python 3'}
CPP = {'GNU C11', 'GNU C++11', 'GNU C', 'MS C++ 2017', 'MS C++', 'GNU C++14', 'GNU C++17'}

def auth(email, password):
    auth_url = "https://codeforces.com/enter"
    login = {"user": email, "password": password, "script": "true"}

    response = requests.post(auth_url, data=login)
    
    if response.status_code == 200:
        return response.cookies

    raise Exception("Invalid credintials")

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

def popup_page():
    pass

def get_submission(user, username, page=1, status_filter='Accepted'):
    url = f'https://codeforces.com/submissions/{username}/page/{page}'
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

def download_submission(user, username):
    page = 1
    cont = True
    while cont:
        cont = get_submission(user, username, page)
        page += 1

email = "mukeremali112@gmail.com"
password = "amina@life"
username = "mukeremali"
user = auth(email, password)
download_submission(user, username)


# error_types = {'Time limit exceeded', 'Wrong answer', 'Accepted', 'Hacked', 'Compilation error', 'Memory limit exceeded', 'Runtime error'}
# languages = {'GNU C11', 'GNU C++11', 'GNU C', 'MS C++ 2017', 'Python 2', 'PyPy 3', 'MS C++', 'PyPy 2', 'Python 3', 'GNU C++14', 'GNU C++17'}