

import requests
from bs4 import BeautifulSoup as BS
import re
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

#
# Select series info 
#
t = ''
for p in range(1, 6) :
    r = requests.get("https://www.kinopoisk.ru/lists/movies/series-top250/?page=" + str(p))
    sleep(5)
    t += r.text 
soup = BS( t, features="html.parser")
all_s = soup.find_all('div', class_='styles_root__3a8vf')

#
# Select genre of the series 
#
genre = []
for film in all_s :
    g = film.find('span', class_='desktop-list-main-info_truncatedText__2Q88H').text

    try :
        found = re.search(' • (.+?)\xa0', g).group(0)
    except AttributeError :
        found = 'No genre found' # error message

    f = found[3:-1]
    genre.append( f )

#
# Count number of unique genre keys
#
from collections import Counter
c = Counter(genre)
#print(c, len(c))
#print(c.keys())

#
# Create a hist to show series distribution by genre
#
f = plt.figure(figsize = (20, 10)) # Set figure size
b = [x+n for n in range(0, len(c)) for x in [0.0, 1.0]]+[len(c)] # Set ticks positions on the center of each bin
plt.hist(genre, rwidth=0.9, bins=b, align='left') # Create a hist
plt.ylabel("Количество раз", size=22) # Set y label 
plt.grid(axis='y')
plt.show()

#
# END
#
