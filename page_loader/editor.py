def edit_soup(hyperlink: str, tag: str, meta: str, local_link: str, soup):
    items = soup.find_all(tag, {meta: hyperlink})
    for item in items:
        item[meta] = local_link
    return soup
