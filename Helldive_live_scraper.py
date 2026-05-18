from bs4 import BeautifulSoup
import requests
import re
import json

print('Hello User! \n You wish to generate a loadout for your fight against the undemocratic enemies of Super Earth so I shall provide.\n I just need to know what faction you will be fighting.\n')

base_url = 'https://utm7j5pjvi.us-east-1.awsapprunner.com/'
faction = 'faction=' + input('What faction do you want to fight? \n terminid, automaton, or illuminate ')
patch_id = 'patch_id=11'
difficulty = 'difficulty=0'
mission = 'mission=All'
modifier = 'modifier=ALL'
tipe = ['type=strategem','type=weapons','type=armor']

url = base_url + 'items_stats?' + faction + '&' + patch_id + '&' + difficulty + '&' + mission + '&' + modifier + '&' + tipe[0]
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()
data = json.loads(text)
strategems = data['items']

for key, strategem in list(strategems.items())[0:4]:
    print(key.replace('_',' '), 'with a pick rate of: ',  strategem["loadouts_percentage"], '%')

print('')

url = base_url + 'items_stats?' + faction + '&' + patch_id + '&' + difficulty + '&' + mission + '&' + modifier + '&' + tipe[1]
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()
data = json.loads(text)
weapons = data['items']

for key, weapon in list(weapons.items())[0:5]:
    print(key.replace('_',' '), 'with a pick rate of: ',  weapon["loadouts_percentage"], '%')

print('')

url = base_url + 'items_stats?' + faction + '&' + patch_id + '&' + difficulty + '&' + mission + '&' + modifier + '&' + tipe[2]
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()
data = json.loads(text)
armours = data['items']

for key, armour in list(armours.items())[0:1]:
    print(key.replace('_',' '), 'with a pick rate of: ',  armour["loadouts_percentage"], '%')