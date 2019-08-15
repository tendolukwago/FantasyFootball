import requests
import json


class SleeperAPI(object):

    def __init__(self, league_id='', user_id=''):
        self.league_id = league_id
        self.user_id = user_id

    def get_user_info(self, username):
        """
        @description: Returns user info given a username
        """

        url = f'https://api.sleeper.app/v1/user/{username}'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_league_info(self, league_id):
        """
        @description: Returns league info given a league id
        """

        url = f'https://api.sleeper.app/v1/league/{league_id}'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_league_settings(self, league_id):
        """
        @description: Returns league settings given a league id
        """
        json_ = self.get_league_info(league_id)
        return json_['settings']

    def get_league_scoring_settings(self, league_id):
        """
        @description: Returns league scoring settings given a league id
        """
        json_ = self.get_league_info(self, league_id)
        return json_['scoring_settings']

    def get_league_rosters(self, league_id):
        """
        @description: Returns league rosters given a league id
        """
        url = f'https://api.sleeper.app/v1/league/{league_id}/rosters'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_league_users(self, league_id):
        """
        @description: Returns league users given a league id
        """
        url = f'https://api.sleeper.app/v1/league/{league_id}/users'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_week_matchups(self, league_id, week_num):
        """
        @description: Returns weekly matchups given a league_id and week number
        """
        url = f'https://api.sleeper.app/v1/league/{league_id}/matchups/{week_num}'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_all_week_matchups(self, leauge_id):
        """
        @description: Returns all weekly matchups given a league_id in the form of a dictionary
        """

        week_matchups = {}

        for week in range(1, 20):
            try:
                week_data = self.get_week_matchups(leauge_id, week_num=week)
                if len(week_data) > 0:
                    week_matchups[week] = week_data

            except:
                pass

        return week_matchups

    def get_winners_bracket(self, league_id):
        """
        @description: Returns the winners bracket of a league's playoffs.
                      The t1 and t2 variables return the roster_id of each team.
                      w & l display the winners and losers of each match.
        """

        url = f'https://api.sleeper.app/v1/league/{league_id}/winners_bracket'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_losers_bracket(self, league_id):
        """
        @description: Returns the losers bracket of a league's playoffs.
                      The t1 and t2 variables return the roster_id of each team.
                      w & l display the winners and losers of each match.
        """

        url = f'https://api.sleeper.app/v1/league/{league_id}/losers_bracket'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_league_transactions(self, league_id, week_num):
        """
        @description: Returns the transactions that took place given a league id and week_num.
        """

        url = f'https://api.sleeper.app/v1/league/{league_id}/transactions/{week_num}'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_all_league_transactions(self, league_id):
        """
        @description: Returns all transactions that took place given a league id.
        """

        week_transactions = {}

        for week in range(1, 20):
            try:
                week_data = self.get_league_transactions(league_id, week)

                if len(week_data) > 0:
                    week_transactions[week] = week_data

            except Exception as e:
                print(f'Error @ week =  {week}: {e}')
                pass

        return week_transactions

    def get_traded_picks(self, league_id):
        """
        @description: Returns all picks that were traded given a league id.
        """

        url = f'https://api.sleeper.app/v1/league/{league_id}/traded_picks'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_user_drafts(self, user_id, year):
        """
        @description: Returns all drafts from a user in a given year.
        """

        url = f'https://api.sleeper.app/v1/user/{user_id}/drafts/nfl/{year}'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_league_draft_history(self, league_id):
        """
        @description: Returns all drafts from a league sorted from earliest to most recent.
        """

        url = f'https://api.sleeper.app/v1/league/{league_id}/drafts'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_draft_info(self, draft_id):
        """
        @description: Returns draft information given a draft_id.
        """

        url = f'https://api.sleeper.app/v1/draft/{draft_id}'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_

    def get_most_recent_draft_id(self, league_id):
        """
        @description: Returns the most recent draft_id from a given league_id.
        """

        league_draft_history = self.get_league_draft_history(league_id)
        recent_draft = league_draft_history[-1]
        recent_draft_id = recent_draft['draft_id']
        return recent_draft_id

    def get_most_recent_draft(self, league_id):
        """
        @description: Returns information from the most recent draft given a league_id.
        """

        recent_draft_id = self.get_most_recent_draft_id(league_id)
        return self.get_draft_info(recent_draft_id)

    def get_draft_picks(self, draft_id):
        """
        @description : Returns all draft picks from a draft given a draft_id.
        """

        url = f'https://api.sleeper.app/v1/draft/{draft_id}/picks'
        response = requests.get(url)
        json_ = json.loads(response.content)
        return json_
    
    def fetch_players(self):
        '''
        @description: Fetches a dictionary of all players info.
        '''
        
        url = 'https://api.sleeper.app/v1/players/nfl'
        response = requests.get(url)
        json_ = json.loads(response.content) 
        return json_
    
    
    def trending_players(self, type = 'add', lookback=12, limit=25, sport='nfl'):
        '''
        @description: Fetches all trending players to add/drop in a given hours.
        '''
        url = f'https://api.sleeper.app/v1/players/{sport}/trending/{type}?lookback_hours={lookback}&limit={limit}'
        response = requests.get(url)
        json_ = json.loads(response.content) 
        return json_
    
    
    def get_season_stats(self, season_type = 'regular', sport = 'nfl', season=2019):
        '''
        @description: Returns the season total stats for each player given a season and year.
        '''
        url = f'https://api.sleeper.app/v1/stats/{sport}/{season_type}/{season}'
        response = requests.get(url)
        json_ = json.loads(response.content) 
        return json_
    
    def get_week_stats(self, week, season_type = 'regular', sport = 'nfl', season=2019):
        '''
        @description: Returns the week total stats for each player given a season, year, and week.
        '''
        
        url = f'https://api.sleeper.app/v1/stats/{sport}/{season_type}/{season}/{week}'
        response = requests.get(url)
        json_ = json.loads(response.content) 
        return json_
    
    def get_all_week_stats(self, **kwargs):
        '''
        @description: Returns all weekly total stats for each player given a season, year, and week.
        '''
        
        all_weeks = {}
        for week in range(1, 20):
            
            try:
                week_data = get_week_stats(week, **kwargs)
                if len(week_data) > 0:
                    all_weeks[week] = week_data
                    
            except:
                pass
            
        return all_weeks
    
    
    def get_season_projections(self, season_type = 'regular', sport = 'nfl', season=2019):
        '''
        @description: Returns the season total projections for each player given a season and year.
        '''
        url = f'https://api.sleeper.app/v1/projections/{sport}/{season_type}/{season}'
        response = requests.get(url)
        
        json_ = json.loads(response.content) 
        return json_
    
    def get_week_projections(self, week, season_type = 'regular', sport = 'nfl', season=2019):
        '''
        @description: Returns the week total projections for each player given a season, year, and week.
        '''
        
        url = f'https://api.sleeper.app/v1/projections/{sport}/{season_type}/{season}/{week}'
        response = requests.get(url)
        json_ = json.loads(response.content) 
        return json_
    
    
    def get_all_week_projections(self, **kwargs):
        '''
        @description: Returns all weekly total projections for each player given a season, year, and week.
        '''
        
        all_weeks = {}
        for week in range(1, 20):
            
            try:
                week_data = get_week_projections(week, **kwargs)
                if len(week_data) > 0:
                    all_weeks[week] = week_data
                    
            except:
                pass
            
        return all_weeks
