# Rscta
Contains code and presentation for my submission for National Conference  on Recent Statistical Computing Techniques and their Applications

First part depicts how a Second Order Markov Chain can be used to generate random and yet funny at times text. For this demo, lyrics for  following categories
 <ul>
  <li> Top Chart WorldWide </li>
  <li> Indian Bollywood </li>
  <li> Hip-Hop/Rap </li>
  <li> Ed Sheeran </li>
  <li> Honey Singh </li>
</ul>

 were scraped off from [MusixMatch](https://www.musixmatch.com) to generate local files containing list of song lyrics which then were feed to a third order Markov chain to generate random lyrics.

Web scraper was made using BeautifulSoup 4 for the scraping part and written to files in Unicode format using Codecs.
For the Markov chain part, it is based and totally credited to [Shabda Raj](http://agiliq.com/blog/author/shabda/) of [Agiliq](http://agiliq.com/) discussed on their[ blog here](http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/)



