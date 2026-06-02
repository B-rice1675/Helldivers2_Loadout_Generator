from bs4 import BeautifulSoup
from collections import defaultdict
import requests
import json

BASE_URL = 'https://utm7j5pjvi.us-east-1.awsapprunner.com/'

def fetch_items(faction, patch_id, difficulty, mission, modifier, item_type):
    url = (
        f"{BASE_URL}items_stats?"
        f"{faction}&{patch_id}&{difficulty}&{mission}&{modifier}&type={item_type}"
    )
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = json.loads(soup.get_text())
    return data['items']

def fetch_categories(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = json.loads(soup.get_text())
    return {key: item['category'] for key, item in data['items'].items()}

def print_grouped(stats, category_map, top_n=4):
    grouped = defaultdict(dict)
    for key, item in stats.items():
        category = category_map.get(key, 'Unknown')
        grouped[category][key] = item
    for category, group in grouped.items():
        if category == 'Unknown':
            continue
        print(f"\n  [{category}]")
        for key, item in list(group.items())[:top_n]:
            print(f"    {key.replace('_', ' ')} — pick rate: {item['loadouts_percentage']}%")

def print_flat(stats, top_n=3):
    for key, item in list(stats.items())[:top_n]:
        print(f"  {key.replace('_', ' ')} — pick rate: {item['loadouts_percentage']}%")


print(
    "Hello User!\n"
    "You wish to generate a loadout for your fight against the undemocratic enemies of Super Earth,\n"
    "so I shall provide. I just need to know what faction you will be fighting.\n"
)

faction    = 'faction=' + input('What faction do you want to fight?\n  terminid, automaton, or illuminate: ').strip().lower()
patch_id   = 'patch_id=12'
difficulty = 'difficulty=0'
mission    = 'mission=All'
modifier   = 'modifier=ALL'

strat_categories  = fetch_categories('stratagem_types')
weapon_categories = fetch_categories('weapon_types')

# --- Stratagems ---
print("=== Top Stratagems ===")
strat_stats = fetch_items(faction, patch_id, difficulty, mission, modifier, 'strategem')
print_grouped(strat_stats, strat_categories, top_n=4)

# --- Weapons ---
print("\n=== Top Weapons ===")
weapon_stats = fetch_items(faction, patch_id, difficulty, mission, modifier, 'weapons')
print_grouped(weapon_stats, weapon_categories, top_n=4)

# --- Armour ---
print("\n=== Top Armour ===")
armour_stats = fetch_items(faction, patch_id, difficulty, mission, modifier, 'armor')
print_flat(armour_stats, top_n=4)
