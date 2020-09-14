import bs4
import requests
from requests.auth import HTTPBasicAuth

url_list = [
"https://dev.celltrackingapps.com/spy-app-android/",
"https://dev.fivebestvpn.com/best-vpn-for-gaming/",
"https://dev.ilogiciel.com/espionner-snapchat/",
"https://dev.toplogicielespion.com/localiser-un-portable/",
"https://dev.vpn-lab.com/compare-nordvpn-expressvpn/",
"https://dev.bestparentalcontrolapps.com/iphone-ipad/"
    ]
link_to_check = [
"/download/"
    ]
user = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
list_errors = []
for url in url_list:
    print("\nproccesing - " + url + '\n')
    get_url = requests.get(url, headers=user, auth=HTTPBasicAuth('devdev', 'UStZj2epgWZFKCVc'))
    url_text = get_url.content
    soup = bs4.BeautifulSoup(url_text, 'html.parser')
    links = soup.findAll('a')
    for link in links:
        print(link)
        # if link['href'] in link_to_check:
        try:
            if link['rel'] != ['sponsored'] and link['target'] != ['_blank']:
                list_errors.append('Error in {} link - {} rel = {}'.format(url, link['href'], link['rel']))
        except:
            ('немає атрибута rel')

for error in list_errors:
    print(error)
