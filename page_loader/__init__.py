"""Module downloading HTML content from specified URL into file."""
from page_loader.url import get_filepath, get_netloc
from page_loader.loader import get_html
from page_loader.file import save_file, read_file
from bs4 import BeautifulSoup
from urllib.parse import urlparse

ASSET_TAGS = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def download(url, local_path):
    """Download data from specified URL & save it into file.

    Args:
        url ([str]): url, like "https://python.org/3/library/exceptions.html"
        local_path ([str]): local path, like: "/var/tmp"
    """
    # Generate file_path to save data
    file_path = get_filepath(url=url, local_path=local_path)

    # Get HTML data from URL & save parsed data into file
    html = get_html(url)
    try:
        save_file(data=html, local_path=file_path)
        return(file_path)
    except Exception as err:
        print('An error occurred:' + str(err))


def modify_links(url, file_path):
    # Read HTML data into variable
    html = read_file(file_path)

    # Initialize soup object
    soup = BeautifulSoup(html, 'lxml')

    # Get links as a dict
    output = {}
    for tag, attr in ASSET_TAGS.items():
        # output[tag] = get_links(tag, attr, soup, url)
        output[tag] = filter_local_links(get_links(tag, attr, soup), url)

    return output


def get_links(tag, attr, soup):
    """Get list of links from HTML page (for specified tag and attribute).

    Args:
        tag ([str]): HTML meta-tag
        attr ([str]): meta-tag attribute
        soup ([soup]): BeautifulSoup Object

    Returns:
        [type]: list of local and external links, like:
                ['assets/application.css',
                '/assets/favicon.ico',
                'https://ru.hexlet.io/lessons.rss',
                'https://js.stripe.com/v3/',
                'https://cdn2.hexlet.io/packs/js/application-6d2cae17d8f39.js']
    """
    # Parse list of specified tags
    links = soup.find_all(tag)

    # Get attributes (url's) from list of tags
    links = [link.get(attr) for link in links]

    # Return list of links
    return links


def filter_local_links(page_links, page_url):
    """Remove any links outside parent's url.

    Args:
        page_links ([list]): list of internal and external links, like:
                            ['assets/application.css',
                            '/assets/favicon.ico',
                            'https://ru.hexlet.io/lessons.rss',
                            'https://js.stripe.com/v3/']
        domain_url ([str]): page url, like:
                            "https://python.org/3/library/exceptions.html"

    Returns:
        [list]: filtered list of local links, like:
                ['/assets/favicon.ico',
                '/assets/application.css',
                '/lessons.rss',
                '/professions']
    """

    # Get domain netlock
    domain_netlock = get_netloc(page_url)

    filtered = []

    # Filter None values and all external links (outside parent domain)
    for link in page_links:
        # Skip all None values
        if link is None:
            continue

        link_netloc = get_netloc(link)

        # Add to the filtered[] all links without netlock (i.e. local links)
        if link_netloc is None:
            filtered.append(link)

        # Add to filtered[] all link that matches parent domain name
        # (add paths only without parent domain name)
        if link_netloc == domain_netlock:
            filtered.append(urlparse(link).path)

    # Add a slash at the beginning of line (if local link does not have slash)
    filtered = map(lambda link: ('/' + link) if link[:1] != '/' else link,
                   filtered)

    # Return list of filtered local links
    return list(filtered)



url = 'https://ru.hexlet.io/courses/'
file_path = '/home/n8creator/projects/python-project-lvl3/tests/fixtures/ru-hexlet-io-professions.html'

print(modify_links(url=url, file_path=file_path))
