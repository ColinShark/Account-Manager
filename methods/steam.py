import requests

API = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/"


class Steam:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def __repr__(self):
        return '<%s - API: %s>' % (self.__class__.__name__, self.api_key)

    def fetch_player_bans(self, steam_ids: list):
        params = {'key': self.api_key,
                  'steamids': ','.join(steam_ids)}
        return requests.get(API, params).json()['players']
