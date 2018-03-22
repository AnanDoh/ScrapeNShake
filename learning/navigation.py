import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

nav = soup.nav#finds all <nav>

for url in nav.find_all('a'):#finds anchor tag and trys to get linhk from nav
    print(url.get('href')) #gets urls from href="nblah" 

#finds two nav bar due to the smaller nav that is used when website is small 
    
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)
    
for div in soup.find_all('div', class_='body'): #find the divs and specify class
    print(div.text)