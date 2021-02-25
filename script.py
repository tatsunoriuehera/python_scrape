#print('hello python')

import requests

from bs4 import BeautifulSoup

# load_url = "http://61.115.113.199/pg/list_arrival.php"

load_url = "http://61.115.113.199/pg/list_arrival.php"

html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

#print(soup)
#file = open('sample.txt','w')
#file.write(soup.find("table","").text)
#file.write(soup.find_all("tr")[2].text)
#file.close()

#list
list = [soup.find("table")]
print(list)
