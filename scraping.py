import codecs
from bs4 import BeautifulSoup
from urlparse import urljoin
from urllib import urlopen

base_url = "https://www.musixmatch.com"

def get_lyrics(song_url):
    response = BeautifulSoup(urlopen(song_url),"lxml")
    try:
       lyric_body = response.find('span',{'id' : 'lyrics-html'})
       if lyric_body is not None:
           return lyric_body.text.strip()
       else:
           return " "
    except:
       pass

def write_to_file(filename,content):
    with codecs.open(filename,'a','utf8') as target:
        target.write(content)


def download_lyrics(category_name):
   category = category_name
   response = BeautifulSoup(urlopen(urljoin(base_url,category)),"lxml")
   songs_list = response.findAll('a',{'class' : 'title'})
   for songs in songs_list:
      print "Writing " + songs.text + " lyrics to file  "
      write_to_file(category.replace("/","") + ".txt" ,get_lyrics(urljoin(base_url,songs["href"])))
   print "Wrote " + str(len(songs_list)) + " to file "


INTL = '/explore'
BOLLYWOOD = INTL + '/genre/Indian-Bollywood'
YO_YO = '/artist/Yo-Yo-Honey-Singh'
RAP = INTL + '/genre/Hip-Hop-Rap'
ED_SHEERAN = 'artist/Ed-Sheeran'
category_list = [INTL,BOLLYWOOD,YO_YO,RAP,ED_SHEERAN]

# Download lyrics to file for each category 
for category in category_list:
    print "Downloading lyrics for category " + INTL
    download_lyrics(category)
