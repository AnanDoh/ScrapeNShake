import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.find('table') #find al the tables

table_rows = table.find_all('tr')#finding all table rows with

for tr in table_rows:  
    td = tr.find_all('td')  #find all the table data
    row = [i.text for i in td]
    print(row)
    
    #initial row is missing because those are the headers of it