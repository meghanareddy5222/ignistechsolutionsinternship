import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

url='https://reach24.net/public_events/UnVSBUINPi1N75dp3cHxIA=='

r= requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

div= soup.find_all('div')[4].text.strip()[58:-1]

print(div)
