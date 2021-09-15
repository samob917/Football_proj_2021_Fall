#experiment, 3 by 3 matrix with top, middle, bottom teams

import pandas as pd

team_data = pd.read_excel(r'C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\TeamData.xlsx')
#result_code = pd.read_excel(r'C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\ResultCodes.xlsx')
#play_chart_matrix = pd.read_excel(r"C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\PlayChartMatrix.xlsx")
teams = pd.read_excel(r"C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\Teams.xlsx")



def pick_top_teams():
    
    off_team_year = int(input('Enter year of offense team: '))
    offense = input('Enter offense team abbreviation: ').upper()
    off_teams = teams[teams['Year']== off_team_year]
    
    for i in range(len(off_teams['TeamAbbr'])):
        if off_teams.TeamAbbr.iloc[i] == offense:
            off_ID = off_teams.TeamChartID.iloc[i]
            
    off_team_chart = team_data[team_data['TeamChartID']==off_ID]
    
    
    
    def_team_year = int(input('Enter year of defense team: '))
    defense = input('Enter Defense team abbreviation: ').upper()
    def_teams = teams[teams['Year']== def_team_year]

            
    for j in range(len(def_teams['TeamAbbr'])):
        if def_teams.TeamAbbr.iloc[j] == defense:
            def_ID = def_teams.TeamChartID.iloc[j]
            

    def_team_chart = team_data[team_data['TeamChartID']==def_ID] 
    
    
    return off_team_chart,def_team_chart

