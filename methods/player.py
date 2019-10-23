"""Module to get the Players from Steam API"""


class Player:
    """A Player as returned by the Steam API"""

    def __init__(
        self,
        steam_id=None,
        community_banned=None,
        vac_banned=None,
        number_of_vac_bans=None,
        days_since_last_ban=None,
        number_of_game_bans=None,
        economy_ban=None,
    ):
        self.steam_id = steam_id
        self.community_banned = community_banned
        self.vac_banned = vac_banned
        self.number_of_vac_bans = number_of_vac_bans
        self.days_since_last_ban = days_since_last_ban
        self.number_of_game_bans = number_of_game_bans
        self.economy_ban = economy_ban

    def __repr__(self):
        return "<%s ID: %s>" % (self.__class__.__name__, self.steam_id)

    @classmethod
    def from_dict(self, api_response: list):
        players = []
        for player in api_response:
            players.append(
                Player(
                    steam_id=int(player["SteamId"]),
                    community_banned=bool(player["CommunityBanned"]),
                    vac_banned=bool(player["VACBanned"]),
                    number_of_vac_bans=int(player["NumberOfVACBans"]),
                    days_since_last_ban=int(player["DaysSinceLastBan"]),
                    number_of_game_bans=int(player["NumberOfGameBans"]),
                    economy_ban=bool(player["EconomyBan"]),
                )
            )
        return players


""" Example Response from the Steam API
{
    "players": [
        {
            "SteamId": "76561198887200817",
            "CommunityBanned": False,
            "VACBanned": False,
            "NumberOfVACBans": 0,
            "DaysSinceLastBan": 0,
            "NumberOfGameBans": 0,
            "EconomyBan": None
        },
        {
            "SteamId": "76561198887096006",
            "CommunityBanned": false,
            "VACBanned": false,
            "NumberOfVACBans": 0,
            "DaysSinceLastBan": 73,
            "NumberOfGameBans": 1,
            "EconomyBan": "none"
        }
    ]
}"""
