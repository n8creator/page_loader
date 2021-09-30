from urllib.parse import urlunparse
from page_loader.path import parse_url
from operator import itemgetter


def parse_links(tag, attr, soup):
    """Get list of links from HTML page (for specified tag and attribute)."""
    links = soup.find_all(tag)
    links = [link.get(attr) for link in links]  # get attributes from each link
    return links


def remove_duplicates(data: list) -> list:
    """Remove duplicate items from the list."""
    return list(dict.fromkeys(data))


def filter_links(links: list, url: str):
    """Filter any links outside URL's domain."""
    filtered = []
    domain_netloc = parse_url(url)['netloc']  # Get URL's domain name
    for link in links:
        link_netloc = parse_url(link)['netloc']  # Get link's domain name
        if link is None:  # Skip all None values from links[] list
            continue
        if link_netloc == '':
            filtered.append(link)
        if link_netloc == domain_netloc:
            filtered.append(link)
    return remove_duplicates(filtered)


def get_links(tag_meta: dict, url: str, soup) -> list:
    """Get list of links for specified 'tag & meta' tags to parse & replace."""
    links = []
    for tag, attr in tag_meta.items():
        local_links = parse_links(tag=tag, attr=attr, soup=soup)
        for link in filter_links(links=local_links, url=url):
            links.append((link, tag))
    return links


def get_absolute_link(page_url: str, local_link: str) -> str:
    """Convert local link into absolute link in 'page_url' domain."""
    domain_params = parse_url(page_url)
    local_params = parse_url(local_link)

    scheme, netloc = itemgetter('scheme', 'netloc')(domain_params)
    path, params, query, fragment = itemgetter(
        'path', 'params', 'query', 'fragment')(local_params)

    return urlunparse([scheme, netloc, path, params, query, fragment])
