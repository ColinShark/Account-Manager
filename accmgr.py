from time import strftime, localtime
from configparser import ConfigParser

from utils.sheet import Sheet
from utils.steam import Steam
from utils.player import Player

config = ConfigParser()
config.read("config.ini")

sheet = Sheet(
    sheet_key=config.get("accmgr", "sheet_key"),
    credentials="credentials.json",
    url_column=config.get("accmgr", "url_column"),
    ban_column=config.get("accmgr", "ban_column"),
)
steam = Steam(config.get("accmgr", "steam_api"))

profile_urls = sheet.get_profile_links()
player_bans = steam.fetch_player_bans(profile_urls)
players = Player().from_dict(player_bans)
updated = sheet.update_game_bans(players)
print(
    strftime("%y-%m-%d %H:%M:%S", localtime()),
    "Updated Cells:",
    updated["updatedCells"],
)
