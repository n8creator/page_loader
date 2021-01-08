from bs4 import BeautifulSoup

with open('ru-hexlet-io-professions.html', 'r') as f:
    data = f.read()


def get_links(data):
    soup = BeautifulSoup(data, 'lxml')
    imgs = soup.find_all('link')
    return imgs


print(get_links(data))
