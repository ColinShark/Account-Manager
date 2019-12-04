import requests

STEAM_API = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/"


class Steam:
    def __init__(self, api_key: str):
        """Interface for the Steam API

        Arguments:
            api_key {str} -- The Steam Developer API Key
        """
        self.api_key = api_key

    def __repr__(self):
        return "<%s - API: %s>" % (self.__class__.__name__, self.api_key)

    def fetch_player_bans(self, steam_ids: list) -> list:
        """Fetch the GameBan information from the Steam API

        Arguments:
            steam_ids {list} -- A list of Steam profile URLs

        Returns:
            list -- A list of dicts, containing information about Player Bans
        """
        players = []
        for i in range(0, len(steam_ids), 100):
            params = {"key": self.api_key, "steamids": ",".join(steam_ids[i : i + 100])}
            for player in requests.get(STEAM_API, params).json()["players"]:
                players.append(player)
        return players
