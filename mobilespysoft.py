import requests, bs4


urls_pages = list()
link_page = list()
list_301 = list()
list_errors = list()
base_url = "https://mobilespysoft.com"

print(f"processing {base_url}")
get_base_url = requests.get(base_url)
base_url_text = get_base_url.content
soup = bs4.BeautifulSoup(base_url_text, 'html.parser')
containers = soup.find_all('a', href=True)
for container in containers:
    container_text = container.text
    container_urls = container.get('href')
    if base_url in container_urls:
        urls_pages.append(container_urls)
    # print('%s = %s' % (container_text, container_urls))

for urls_page in urls_pages:
    print(f"processing url - {urls_page}")
    try:
        link = requests.get(urls_page)
    except Exception as err:
        print('Погане посилання', err)
    link_text = link.content
    link_soup = bs4.BeautifulSoup(link_text, 'html.parser')
    link_containers = link_soup.find_all('a', href=True)
    for link_container in link_containers:
        print(f"processing link - {link_container}")
        link_container_text = link_container.text
        link_url = link_container.get('href')
        print(link_url)
        if base_url in link_url:
            responce = requests.get(link_url)
            if responce.status_code == 200:
                list_errors.append(link_url)
            elif responce.status_code == 301:
                list_301.append(link_url)
        # urls_page.append(link_url)
        # print('%s = %s' % (txt, url))
for error in list_errors:
    print(error)





# for link in urls:
#     print(f"processing {base_url + link}")
#     r = requests.get(base_url + link)
#     urls_blog = r.content
#     soup = bs4.BeautifulSoup(urls_blog, 'html.parser')
#     hrefs_blog = soup.findAll('a', href=True)
#     for href_blog in hrefs_blog:
#         urlsblog.append(href_blog['href'])
# print(urlsblog)
# for urlblog in urlsblog:
#     if urlblog == '/order':
#         print(f"processing {urlblog}")
#         list_errors.append(urlblog)