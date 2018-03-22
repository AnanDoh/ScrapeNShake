import bs4 as bs
import urllib.request
from textblob import TextBlob

source = urllib.request.urlopen('https://www.nytimes.com/search/stem?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage').read()
soup = bs.BeautifulSoup(source,'lxml')
ol = soup.ol#finds all <ol>

for things in ol.find_all('a'):
    print(things.get('href')) #gets urls from href="nblah" 
    print(things.text)
    print('\n')
    anal = things.text
    blob = TextBlob(anal)
    print(blob.tags)#tells you part of speech
    print('\n')
    print(blob.noun_phrases)#tells you nouns
    print('\n')
    for sentence in blob.sentences:
        print(sentence.sentiment)#rates how positive or negative a sentence in the title is and if based on personal innfluence
    print('==========================='+'\n')
