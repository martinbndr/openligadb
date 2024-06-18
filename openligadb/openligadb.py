import requests
from .session import RequestsSession

from .objects import League, Sport, Match

class Openligadb:
    session: RequestsSession | None

    def __init__(self):
        self.session = RequestsSession()
        
    def get_leagues(self) -> list[League]:
        """
        Gets all available leagues.
        """
        rsp = self.session.get('/getavailableleagues')
        leagues_list = []
        for i in rsp.json():
            leagues_list.append(League(i))
        return leagues_list
    
    def get_sports(self) -> list[Sport]:
        """
        Gets all available sports.
        """
        rsp = self.session.get('/getavailablesports')
        sports_list = []
        for i in rsp.json():
            sports_list.append(Sport(i))
        return sports_list
    
    def get_match(self, matchId: int) -> Match:
        """
        Gets a match by id.
        """
        rsp = self.session.get(f"/getmatchdata/{matchId}")
        return Match(rsp.json())
        