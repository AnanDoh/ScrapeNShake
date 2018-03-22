import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

print (soup.title.name) #get the tag name
print (soup.title.text) #get the inside title tag
print (soup.p.text) #get the first paragraph element
print (soup.find_all('p')) #get the all paragraph element

for paragraph in soup.find_all('p'):
    print(paragraph.string) #print out string
    print(str(paragraph.text))#print out unicode


print(soup.get_text())#print out all text??

for url in soup.find_all('a'):#finds anchor tag and trys to get linhk
    print(url.get('href'))  #gets urls from href="nblah"
