from bs4 import BeautifulSoup
import requests
import csv

lst = []
url = 'http://datachart.500.com/dlt/history/newinc/history.php?start=07001&end=23138'
r = requests.get(url)
r.encoding = 'utf-8'
text = r.text
soup = BeautifulSoup(text, "html.parser")
tbody = soup.find('tbody', id="tdata")
tr = tbody.find_all('tr')

# 动态确定网页上实际的行数
total_rows = len(tr)

for page in range(total_rows):
    td = tr[page].find_all('td')
    lst.append([td[0].text, td[1].text, td[2].text, td[3].text, td[4].text, td[5].text, td[6].text, td[7].text])

with open(r"C:\Users\abc\Desktop\Lottery_data.csv", 'w', newline='', encoding='gbk') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['期号', '号码1', '号码2', '号码3', '号码4', '号码5', '号码6', '号码7'])
    writer.writerows(lst)
