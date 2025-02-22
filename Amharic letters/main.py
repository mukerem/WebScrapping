import requests
from bs4 import BeautifulSoup


def download_mp3(url, letter):
    response = requests.get(url, stream=True)  # Stream allows downloading in chunks
    if response.status_code == 200:
        save_path=f"sound/{letter}.mp3"
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):  # Download in chunks
                file.write(chunk)
        print(f"✅ MP3 downloaded successfully: {save_path}")
    else:
        print(f"❌ {letter}: Failed to download MP3. Status Code: {response.status_code}")

def download(letters):
    base_url = "https://d9seco0wfq8yu.cloudfront.net/dict/sounds/mp3"
    for letter in letters:
        url = f"{base_url}/{letter}.mp3"
        download_mp3(url, letter)


def extract():
    url = "https://amharicteacher.com/hahu"
    data = {"script": "true"}
    page_content = requests.get(url, data=data)
    soup = BeautifulSoup(page_content.text, "html.parser")
    letter_obj = soup.find_all('li', attrs={'class': 'alpha_li'})
    
    letters = []

    for letter in letter_obj:
        letter = letter.find('span').text
        letters.append(letter)
    return letters
letters = extract()
download(letters)

# url = "https://d9seco0wfq8yu.cloudfront.net/dict/sounds/mp3/muh.mp3"
# letter = "muh"
# download_mp3(url, letter)