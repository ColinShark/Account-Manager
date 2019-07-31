import re

import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

from methods.player import Player
from methods.sheet import Sheet
from methods.steam import Steam

# Put your SheetID and the downloaded credentials from your
# Google Project here. Just keep it as a string.
sheet = Sheet('<Sheet Key here>',
              '<Google Credentials here>.json')
# This is your Steam API key. Get your own from
# https://steamcommunity.com/dev/apikey
steam = Steam("<Your API Key here>")

# This runs the code, don't touch this lol
links = sheet.get_profile_links()
bans = steam.fetch_player_bans(links)
players = Player().from_dict(bans)
updated = sheet.update_profiles(players)
