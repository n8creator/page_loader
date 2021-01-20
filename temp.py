from bs4 import BeautifulSoup

with open('tests/fixtures/ru-hexlet-io-professions.html', 'r') as f:
    data = f.read()


def get_links(data):
    soup = BeautifulSoup(data, 'lxml')
    # imgs = soup.find_all('link')
    imgs = soup("img")
    output = []
    for img in imgs:
        src = img.get('src')
        output.append(src)
    return output
    return imgs


print(get_links(data))
