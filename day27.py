

import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
r = requests.get('https://www.amazon.in/')
soup = BeautifulSoup(r.text, 'lxml')
f = csv.writer(open(' dataprocessing.csv ','w'))
f.writerow(['Title'])
f.writerow([soup.title.text])
