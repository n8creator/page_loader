def edit_soup(remote_link: str, tag: str, meta: str, local_link: str, soup):
    # soup = BeautifulSoup(soup, 'lxml')
    # Find all elements containing specified Tag and Meta values
    items = soup.find_all(tag, {meta: remote_link})

    # Find and replace links
    for item in items:
        # item[meta] = item[meta].replace(remote_link, local_link)
        item[meta] = local_link

    # # Return formatted
    return soup
