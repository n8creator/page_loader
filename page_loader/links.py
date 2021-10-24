from urllib.parse import urlunparse
from page_loader.url import parse_url
from operator import itemgetter


def filter_links_in_domain(links_tags: list, url: str):
    """Filter any links outside URL's domain."""

    def in_domain(link_tag: tuple, url: str):
        link, _ = link_tag  # destructure link_tag tuple
        domain_netloc = parse_url(url)['netloc']
        link_netlock = parse_url(link)['netloc']
        if (link_netlock == '' or link_netlock == domain_netloc):
            return True
        return False

    return list(filter(lambda link_tag: in_domain(link_tag=link_tag, url=url),
                       links_tags))


def get_links(tag_meta: dict, url: str, soup) -> list:
    """Return list of links (as dict's) for specified 'tag & meta' tags
    to parse & replace on HTML page."""
    # Parse all links for specified 'tag & meta' and filter any links outside
    # url's domain
    links = []
    for tag, attr in tag_meta.items():
        tag_links = soup.find_all(tag)
        links.extend([(link.get(attr), tag) for link in tag_links])
    filtered_links = filter_links_in_domain(links_tags=links, url=url)

    # Convert filtered links into list of dicts
    output = []
    for link, tag in filtered_links:
        output.append({'fact_link': link,
                       'abs_link': get_abs_link(page_url=url, local_link=link),
                       'tag': tag})
    return output


def get_abs_link(page_url: str, local_link: str) -> str:
    """Convert local link into absolute link in 'page_url' domain."""
    domain_params = parse_url(page_url)
    local_params = parse_url(local_link)

    scheme, netloc = itemgetter('scheme', 'netloc')(domain_params)
    path, params, query, fragment = itemgetter(
        'path', 'params', 'query', 'fragment')(local_params)

    return urlunparse([scheme, netloc, path, params, query, fragment])
