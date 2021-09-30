def edit_soup(url: str, tag: str, meta: str, local_link: str, soup):
    """Find and replace global urls to local links in BeautifulSoup object."""
    items = soup.find_all(tag, {meta: url})
    for item in items:
        item[meta] = local_link
    return soup
