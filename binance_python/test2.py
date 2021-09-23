from urllib.request import urlopen as req 
from bs4 import BeautifulSoup as soup 

url = 'https://th.valutafx.com/USD-THB.htm'
webopen = req(url)
page_html = webopen.read()
webopen.close()
#print(page_html)
data = soup(page_html,'html.parser')
#print(data)
temp = data.findAll('div',{'class':'rate-value'})
temp1 = str(temp) 
print(temp1)
print(type(temp1))