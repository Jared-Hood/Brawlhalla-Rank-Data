<h1>Brawlhalla Ranked Data</h1>

The primary purpose of this program is to scrape ranked data off of the <a href="https://www.brawlhalla.com/rankings/1v1/"> Brawlhalla website </a> in order to create informative ranking graphs like the following. Brawlhalla has an API endpoint that developers can request access however this program still remains to be used by anyone without access. 
<br>
<br>
Brawlhalla's website has a request cap of 5 pages per second and with over 30000 pages of over 1.5 million player's data it would take a long time to recieve all the results. In fact it would take 6000 seconds or 1.6 hours to complete. The way this program gets around this large time is that it intelligently decides what pages to request. The data in the Brawlhalla database is laid out in sequential order based on current player ranking starting with the highest ranks. Therefore, since the only data we need to grab in order to create a ranking cumulative distribution function is the current ranking for each player we can skip ahead pages and reliably know what the ranks where on the skipped pages. This can simply be done using a binary search and a predictive hueristic algorithm, which greatly reduces the search time!
