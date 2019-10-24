class Player(object):
    def __init__(
        self,
        steam_id: int = None,
        community_banned: bool = None,
        vac_banned: bool = None,
        number_of_vac_bans: int = None,
        days_since_last_ban: int = None,
        number_of_game_bans: int = None,
        economy_ban: str = None,
    ):
        """
        Keyword Arguments:
            steam_id {int} -- The player's 64 bit ID.
            community_banned {bool} -- Indicates whether or not the player is banned
                from Steam Community.
            vac_banned {bool} -- Indicates whether or not the player has VAC bans on
                record.
            number_of_vac_bans {int} -- Number of VAC bans on record.
            days_since_last_ban {int} -- Number of days since last ban.
            number_of_game_bans {int} -- Numer of bans in games, this includes CS:GO
                Overwatch bans.
            economy_ban {str} -- The Player's ban status in the economy. If the player
                has no bans on record the string will be "none", if the player is on
                probation it will say "probation", etc.
        """
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
        return [
            Player(
                steam_id=int(player["SteamId"]),
                community_banned=bool(player["CommunityBanned"]),
                vac_banned=bool(player["VACBanned"]),
                number_of_vac_bans=int(player["NumberOfVACBans"]),
                days_since_last_ban=int(player["DaysSinceLastBan"]),
                number_of_game_bans=int(player["NumberOfGameBans"]),
                economy_ban=bool(player["EconomyBan"]),
            )
            for player in api_response
        ]
