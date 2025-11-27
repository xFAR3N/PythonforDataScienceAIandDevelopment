import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import requests
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

'''def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)'''

nba_teams = teams.get_teams()

dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)
#print(df_teams.head())

df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
#print(df_warriors)

id_warriors = df_warriors.iloc[0,0]
#print(id_warriors)

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

games_ = gamefinder.get_json()
#print(games_)
games = gamefinder.get_data_frames()[0]
#print(games.head())

'''file_url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl'

file_name = 'Golden_State.pkl'
download(file_url, file_name)

gamesFromFile = pd.read_pickle(file_name)

print(gamesFromFile.head())'''

games_home = games[games['MATCHUP'] == 'GSW vs. TOR']
games_away = games[games['MATCHUP'] == 'GSW @ TOR']
print(games_home.head())
print(games_away.head())


fig, ax = plt.subplots()
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

mean_home = games_home['PTS'].mean()
print('Mean at home:',mean_home)
mean_away = games_away['PTS'].mean()
print('Mean away:', mean_away)

