import requests
import datetime
from bs4 import BeautifulSoup
import csv

today=datetime.date.today()

set_month = today.strftime("%Y%m")
set_today = today.strftime("%Y%m%d")
load_url = "http://www.shijou-nippo.metro.tokyo.jp/JS/"+str(set_month)+"/"+str(set_today)+"/Kak/JS_Kak_Zen_index.html"

html = requests.get(load_url)

soup = BeautifulSoup(html.content, "html.parser")

#print(soup)

#table = soup.findAll("caption",{"class":"yotei-page-sei-caption"})[0]
table = soup.find_all("table")[2]
rows = table.find_all("tr")
print(rows)

#text write ---
file = open(str(set_today)+".txt","w")
file.write(soup.find("tr","").text)
file.write(soup.find_all("table")[2].text)
file.close()
#text end ---

#csv write ---
#f = open('out.csv','w')
#write = csv.writer(f)
#write.writerow(soup.find_all("table")[2].text)
#f.close()
#csv end ---
