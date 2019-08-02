from methods.player import Player
from methods.sheet import Sheet
from methods.steam import Steam

# Put your SheetID and the downloaded credentials from your
# Google Project here. Just keep it as a string.
sheet = Sheet(
    sheet_key='<Sheet key from spreadsheet URL>',
    credentials='<Authentication File-name>.json',
    url_col='N', ban_col='O')

# This is your Steam API key. Get your own from
# https://steamcommunity.com/dev/apikey
steam = Steam("<Steam API Key>")

# This runs the code, don't touch this lol
links = sheet.get_profile_links()
bans = steam.fetch_player_bans(links)
players = Player().from_dict(bans)
updated = sheet.update_profiles(players)
print(updated)
