from page_loader.path import parse_url
from urllib.parse import urlunparse


def parse_links(tag, attr, soup):
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


def remove_duplicates(data: list) -> list:
    """Remove duplicates from the list.

    Args:
        data (list): some list that main contain duplicates

    Returns:
        list: output list without duplicates
    """
    return list(dict.fromkeys(data))


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
            filtered.append(link)

    # Return list of filtered local links
    return remove_duplicates(filtered)


def get_list_of_links(tag_meta: dict, url: str, soup) -> list:
    """Generate full list of links to parse & replace.

    Args:
        tag_dict (dict): dict containing tags and meta-tags to process, like:
                        {'img': 'src', 'link': 'href', 'script': 'src'}
        url (str): page url
        soup ([type]): BeautifulSoup object containing HTML-code

    Returns:
        list: filtered list of local links with tags, like:
             '('/rynok-situatsiya-v-momente-23/', 'link')'
    """
    links = []
    for tag, attr in tag_meta.items():
        local_links = filter_links(links=parse_links(tag=tag,
                                                     attr=attr,
                                                     soup=soup),
                                   url=url)
        for link in local_links:
            links.append((link, tag))
    return links


def get_full_link(page_url: str, link: str) -> str:

    url = parse_url(page_url)
    lnk = parse_url(link)

    scheme = url['scheme']
    netloc = url['netloc']
    path = lnk['path']
    params = lnk['params']
    query = lnk['query']
    fragment = lnk['fragment']

    return urlunparse([scheme, netloc, path, params, query, fragment])
