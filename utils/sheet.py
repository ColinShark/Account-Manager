import re
from string import ascii_lowercase

import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

STEAMID_REGEX = re.compile(r"(\d+)")


class Sheet:
    def __init__(
        self, sheet_key: str, credentials: str, url_column: str, ban_column: str
    ):
        """Sets up interaction with the Google Spreadsheet.

        Arguments:
            sheet_key {str} -- The identifier of the Spreadsheet we will work with
            credentials {str} -- The filename of the used json keyfile from Google
            url_column {str} -- The column containing the steam profile URLs
            ban_column {str} -- The column containing the GameBan counter
        """
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials, SCOPE
        )
        self.url_column = url_column.lower()
        self.ban_column = ban_column.lower()

        gc = gspread.authorize(credentials)
        self.sheet = gc.open_by_key(sheet_key).sheet1

    def get_profile_links(self) -> list:
        """Get a list of steam profile URLs from the spreadsheet

        Returns:
            list -- All Steam URLs from the Spreadsheets URL column
        """
        column = ascii_lowercase.index(self.url_column) + 1
        cells = self.sheet.col_values(column)[1:]
        return [
            cell.value
            for cell in self.sheet.range(
                "{0}2:{0}{1}".format(self.url_column.upper(), len(cells) + 1)
            )
        ]

    def update_game_bans(self, players: list):
        """Update the spreadsheet with GameBan of each account"""
        steam_ids = []
        for steam_id in self.get_profile_links():
            steam_ids.append(int(STEAMID_REGEX.search(steam_id).group(0)))

        players = sorted(players, key=lambda player: steam_ids.index(player.steam_id))

        game_bans = self.sheet.range(
            "{0}2:{0}{1}".format(self.ban_column, str(1 + len(steam_ids)))
        )

        for player, game_ban in zip(players, game_bans):
            game_ban.value = player.number_of_game_bans

        return self.sheet.update_cells(game_bans)
