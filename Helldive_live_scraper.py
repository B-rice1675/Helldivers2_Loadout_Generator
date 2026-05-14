from bs4 import BeautifulSoup
import requests
import re

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
raw_data = soup.get_text()
clean_one = raw_data.replace('"total":', '')
clean_two = clean_one.replace('"avg_level":', '')
clean_three = clean_two.replace('"change":', '')
clean_four = clean_three.replace('"isNew":false', '')
clean_five = clean_four.replace('"isNew":true', '')
clean_six = clean_five.replace('games', '')
clean_seven = clean_six.replace('loadouts', '')
clean_eight = clean_seven.replace('items', '')
clean_nine = clean_eight.replace('loadouts_total', '')
clean_ten = clean_nine.replace('loadouts_percentage', '')
clean_eleven = clean_ten.replace('_',' ')
clean_twelve = clean_eleven.replace('total','')
clean_thirteen = clean_twelve.replace('percentage','')
clean_fourteen = re.findall(r'"([^"]*)"', clean_thirteen)
clean_fifteen = ", ".join(clean_fourteen)
clean_sixteen = clean_fifteen.replace(',  ,  , ',', ')
clean_seventeen = clean_sixteen.replace(', , , ','')
strategem_list = clean_seventeen.split(', ')

url = base_url + 'items_stats?' + faction + '&' + patch_id + '&' + difficulty + '&' + mission + '&' + modifier + '&' + tipe[1]
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
raw_data = soup.get_text()
clean_one = raw_data.replace('"total":', '')
clean_two = clean_one.replace('"avg_level":', '')
clean_three = clean_two.replace('"change":', '')
clean_four = clean_three.replace('"isNew":false', '')
clean_five = clean_four.replace('"isNew":true', '')
clean_six = clean_five.replace('games', '')
clean_seven = clean_six.replace('loadouts', '')
clean_eight = clean_seven.replace('items', '')
clean_nine = clean_eight.replace('loadouts_total', '')
clean_ten = clean_nine.replace('loadouts_percentage', '')
clean_eleven = clean_ten.replace('_',' ')
clean_twelve = clean_eleven.replace('total','')
clean_thirteen = clean_twelve.replace('percentage','')
clean_fourteen = re.findall(r'"([^"]*)"', clean_thirteen)
clean_fifteen = ", ".join(clean_fourteen)
clean_sixteen = clean_fifteen.replace(',  ,  , ',', ')
clean_seventeen = clean_sixteen.replace(', , , ','')
weapons_list = clean_seventeen.split(', ')

url = base_url + 'items_stats?' + faction + '&' + patch_id + '&' + difficulty + '&' + mission + '&' + modifier + '&' + tipe[2]
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
raw_data = soup.get_text()
clean_one = raw_data.replace('"total":', '')
clean_two = clean_one.replace('"avg_level":', '')
clean_three = clean_two.replace('"change":', '')
clean_four = clean_three.replace('"isNew":false', '')
clean_five = clean_four.replace('"isNew":true', '')
clean_six = clean_five.replace('games', '')
clean_seven = clean_six.replace('loadouts', '')
clean_eight = clean_seven.replace('items', '')
clean_nine = clean_eight.replace('loadouts_total', '')
clean_ten = clean_nine.replace('loadouts_percentage', '')
clean_eleven = clean_ten.replace('_',' ')
clean_twelve = clean_eleven.replace('total','')
clean_thirteen = clean_twelve.replace('percentage','')
clean_fourteen = re.findall(r'"([^"]*)"', clean_thirteen)
clean_fifteen = ", ".join(clean_fourteen)
clean_sixteen = clean_fifteen.replace(',  ,  , ',', ')
clean_seventeen = clean_sixteen.replace(', , , ','')
armour_list = clean_seventeen.split(', ')

print('')
print('Here are the top 10 strategems')
print(", ".join(map(str, strategem_list[:10])))
print('')
print('Here are the top 10 weapons')
print(", ".join(map(str, weapons_list[:10])))
print('')
print('Here are the top 10 armours')
print(", ".join(map(str, armour_list[:10])))
print('')