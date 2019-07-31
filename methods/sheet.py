import re

import gspread

from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

STEAMID_REGEX = re.compile(r'\d{17}')

class Sheet:
    def __init__(self, sheet_key, credentials):
        self.sheet_key = sheet_key
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials, SCOPE)

        gc = gspread.authorize(self.credentials)
        self.sheet = gc.open_by_key(self.sheet_key).sheet1

    def get_profile_links(self):
        return self.sheet.col_values(12)[5:]

    def update_profiles(self, players: list):
        steam_ids = [
            int(STEAMID_REGEX.search(x).group(0))
            for x
            in self.get_profile_links()
        ]

        players = sorted(players,
                         key=lambda player: steam_ids.index(player.steam_id))

        game_bans = self.sheet.range('M6:M' + str(5 + len(steam_ids)))

        for player, game_ban in zip(players, game_bans):
            game_ban.value = player.number_of_game_bans

        return self.sheet.update_cells(game_bans)
