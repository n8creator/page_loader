from page_loader.path import parse_url
from urllib.parse import urlparse


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


def filter_links(links: list, url: str):
    """Filter any links outside parent's url.

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

    # Get domain from url
    domain_netloc = parse_url(url)['netloc']

    filtered = []

    # Filter all None and external links (outside parent domain)
    for link in links:

        # Skip all None values from links[] list
        if link is None:
            continue

        # Get link netloc
        link_netloc = parse_url(link)['netloc']

        # Add to the filtered[] all links without netlock (i.e. local links)
        if link_netloc == '':
            filtered.append(link)

        # Add to filtered[] all links that contain parent domain name
        # (add paths only without parent domain name)
        if link_netloc == domain_netloc:
            filtered.append(urlparse(link).path)

    # Add a slash at the beginning of line (if local link does not have slash)
    filtered = map(lambda link: ('/' + link) if link[:1] != '/' else link,
                   filtered)

    # Return list of filtered local links
    return list(filtered)


if __name__ == "__main__":
    print(filter_links(['assets/application.css',
                        '/assets/favicon.ico',
                        'https://ru.hexlet.io/professions',
                        'https://en.hexlet.io/professions',
                        'https://js.stripe.com/v3/'],
                       'https://ru.hexlet.io/professions'))

