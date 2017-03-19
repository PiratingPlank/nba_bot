import json
import requests
from os.path import join
from pprint import pprint

destination_directory = 'Downloads'
url = 'http://stats.nba.com/js/data/widgets/home_daily.json'
resp = requests.get(url)
txt = resp.text
data = json.loads(txt)

def top_scorers():
    pprint(data)

top_scorers()


def get_teams():
    mylist = []

    for stats in data:
        mylist.append(stats['teamstats'])
    return mylist 
