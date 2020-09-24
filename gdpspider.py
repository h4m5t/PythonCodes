import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as bs
from pylab import *
#支持简体中文
rcParams['font.sans-serif']=['SimHei']
year=[]
gdp=[]
url='http://value500.com/M2gdp.html'
#获取网页内容
content=requests.get(url)
content.encoding='utf-8'
#获取网页内容的text部分
content1=content.text
#print(content1)
#进行网页解析
parse=bs(content1,'html.parser')
data1=parse.find_all('table')   #获取所有的表

rows=data1[19].find_all('tr')

i=0
for row in rows:
    cols=row.find_all("td")
    if(len(cols)>0 and i==0):
        i=i+1
    else:
        year.append(cols[0].text[:-2])
        gdp.append(float(cols[2].text))

#翻转横竖坐标
year.reverse()
gdp.reverse()
#print(year, gdp)
#对横坐标进行45°倾斜显示
plt.xticks(rotation=45)
plt.plot(year,gdp)
plt.title('我国GDP')
plt.xlabel('年度')
plt.ylabel('GDP(亿元)')
plt.show()




    


