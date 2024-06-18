from typing import Optional, Union

class League:
    def __init__(self, payload: dict):
        self.payload = payload

    def __repr__(self):
        return f"<Object League: {self.leagueId}>"
    
    def to_dict(self) -> dict:
        """
        Returns the api result in dict format.
        """
        return self.payload
    
    @property
    def leagueId(self) -> int:
        """
        Returns the leagueID.
        """
        return self.payload["leagueId"]
    
    @property
    def leagueName(self) -> Optional[str]:
       """
       Returns the leagueName.
       """
       return self.payload.get("leagueName")
    
    @property
    def leagueShortcut(self) -> Optional[str]:
       """
       Returns the leagueShortcut.
       """
       return self.payload.get("leagueShortcut")
    
    @property
    def leagueSeason(self) -> Optional[str]:
       """
       Returns the leagueSeason.
       """
       return self.payload.get("leagueSeason")
    
    @property
    def sport(self) -> Optional['Sport']:
       """
       Returns the leagueSport as Sport object.
       """
       return self.payload.get("sport")
    
class Sport:
    def __init__(self, payload: dict):
        self.payload = payload

    def __repr__(self):
        return f"<Object Sport: {self.sportId}>"
    
    def to_dict(self) -> dict:
        """
        Returns the api result in dict format.
        """
        return self.payload
    
    @property
    def sportId(self) -> int:
       """
       Returns the sportId.
       """
       return self.payload["sportId"]
    
    @property
    def sportName(self) -> Optional[str]:
       """
       Returns the sportName.
       """
       return self.payload.get("sportName")
    
class Match:
    def __init__(self, payload: dict):
        self.payload = payload

    def __repr__(self):
        return f"<Object Match: {self.matchID} >"
    
    def to_dict(self) -> dict:
        """
        Returns the api result in dict format.
        """
        return self.payload
    
    @property
    def matchID(self) -> int:
       """
       Returns the matchId.
       """
       return self.payload["matchID"]
    
    @property
    def matchDateTime(self) -> Optional[str]:
       """
       Returns the matchDateTime.
       """
       return self.payload.get("matchDateTime")
    
    @property
    def timeZoneID(self) -> Optional[str]:
       """
       Returns the timeZoneID.
       """
       return self.payload.get("timeZoneID")
    
    @property
    def league(self) -> League:
       """
       Returns the League object.
       """
       return League({"leagueId": self.payload["leagueId"],"leagueName": self.payload["leagueName"],"leagueSeason": self.payload["leagueSeason"], "leagueShortcut": self.payload["leagueShortcut"]})
    
class Location:
    def __init__(self, payload: dict):
        self.payload = payload

    def __repr__(self):
        return f"<Object Location: {self.sportId}>"
    
    def to_dict(self) -> dict:
        """
        Returns the api result in dict format.
        """
        return self.payload
    
    @property
    def locationID(self) -> int:
       """
       Returns the locationID.
       """
       return self.payload["locationID"]
    
    @property
    def locationCity(self) -> Optional[str]:
       """
       Returns the locationCity.
       """
       return self.payload.get("locationCity")
    
    @property
    def locationStadium(self) -> Optional[str]:
        return self.payload.get("locationStadium")
    
class Group:
    def __init__(self, payload: dict):
        self.payload = payload

    def __repr__(self):
        return f"<Object Group: {self.groupID}>"
    
    def to_dict(self) -> dict:
        """
        Returns the api result in dict format.
        """
        return self.payload
    
    @property
    def groupID(self) -> int:
       """
       Returns the groupID.
       """
       return self.payload["groupID"]
    
    @property
    def groupName(self) -> Optional[str]:
       """
       Returns the groupName.
       """
       return self.payload.get("groupName")
    
    @property
    def groupOrderID(self) -> int:
        """
        Returns the groupOrderID.
        """
        return self.payload["groupOrderID"]
    
class GoalGetter:
    def __init__(self, payload: dict):
        self.payload = payload

    def __repr__(self):
        return f"<Object GoalGetter: {self.goalGetterId}>"
    
    def to_dict(self) -> dict:
        """
        Returns the api result in dict format.
        """
        return self.payload
    
    @property
    def goalGetterId(self) -> int:
       """
       Returns the goalGetterId.
       """
       return self.payload["goalGetterId"]
    
    @property
    def goalGetterName(self) -> Optional[str]:
       """
       Returns the goalGetterName.
       """
       return self.payload.get("goalGetterName")
    
    @property
    def goalCount(self) -> int:
        """
        Returns the goalCount.
        """
        return self.payload["goalCount"]
    
class GlobalResultInfo:
    def __init__(self, payload: dict):
        self.payload = payload

    def __repr__(self):
        return f"<Object GlobalResultInfo: {self.id}>"
    
    def to_dict(self) -> dict:
        """
        Returns the api result in dict format.
        """
        return self.payload
    
    @property
    def id(self) -> int:
       """
       Returns the id.
       """
       return self.payload["id"]
    
    @property
    def name(self) -> Optional[str]:
       """
       Returns the name.
       """
       return self.payload.get("name")
    
class BlTableTeam:
    def __init__(self, payload: dict):
        self.payload = payload

    def __repr__(self):
        return f"<Object BlTableTeam: {self.teamInfoId}>"
    
    def to_dict(self) -> dict:
        """
        Returns the api result in dict format.
        """
        return self.payload
    
    @property
    def teamInfoId(self) -> int:
       """
       Returns the teamInfoId.
       """
       return self.payload["teamInfoId"]
    
    @property
    def teamName(self) -> Optional[str]:
       """
       Returns the teamName.
       """
       return self.payload.get("teamName")
    
    @property
    def shortName(self) -> Optional[str]:
       """
       Returns the shortName.
       """
       return self.payload.get("shortName")
    
    @property
    def teamIconUrl(self) -> Optional[str]:
       """
       Returns the teamIconUrl.
       """
       return self.payload.get("teamIconUrl")
    
    @property
    def points(self) -> int:
        """
        Returns the points.
        """
        return self.payload["points"]
    
    @property
    def opponentGoals(self) -> int:
        """
        Returns the opponentGoals.
        """
        return self.payload["opponentGoals"]
    
    @property
    def goals(self) -> int:
        """
        Returns the goals.
        """
        return self.payload["goals"]
    
    @property
    def matches(self) -> int:
        """
        Returns the matches.
        """
        return self.payload["matches"]
    
    @property
    def won(self) -> int:
        """
        Returns the number of matches won.
        """
        return self.payload["won"]
    
    @property
    def lost(self) -> int:
        """
        Returns the number of matches lost.
        """
        return self.payload["lost"]
    
    @property
    def draw(self) -> int:
        """
        Returns the number of matches drawn.
        """
        return self.payload["draw"]
    
    @property
    def goalDiff(self) -> int:
        """
        Returns the goal difference.
        """
        return self.payload["goalDiff"]