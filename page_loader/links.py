from urllib.parse import urlunparse
from page_loader.url import parse_url
from operator import itemgetter


def filter_links_in_domain(links_tags: list, url: str):
    """Filter any links outside URL's domain."""
    domain_netloc = parse_url(url)['netloc']
    filtered = []
    for link, tag in links_tags:
        link_netloc = parse_url(link)['netloc']
        if link_netloc == '' or link_netloc == domain_netloc:
            filtered.append((link, tag))
    return filtered


def get_links(tag_meta: dict, url: str, soup) -> list:
    """Get list of links for specified 'tag & meta' tags to parse & replace."""
    links = []
    for tag, attr in tag_meta.items():
        tag_links = soup.find_all(tag)
        links.extend([(link.get(attr), tag) for link in tag_links])
    return filter_links_in_domain(links_tags=links, url=url)


def get_absolute_link(page_url: str, local_link: str) -> str:
    """Convert local link into absolute link in 'page_url' domain."""
    domain_params = parse_url(page_url)
    local_params = parse_url(local_link)

    scheme, netloc = itemgetter('scheme', 'netloc')(domain_params)
    path, params, query, fragment = itemgetter(
        'path', 'params', 'query', 'fragment')(local_params)

    return urlunparse([scheme, netloc, path, params, query, fragment])
