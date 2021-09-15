'''
This code serves to incorporate the excel play charts into the simulator.
The way this will work is I will set up the game centered around the 
mechanism for choosing and running a play
'''

'''
1. import the excels
'''
import pandas as pd

team_data = pd.read_excel(r'C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\TeamData.xlsx')
#result_code = pd.read_excel(r'C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\ResultCodes.xlsx')
#play_chart_matrix = pd.read_excel(r"C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\PlayChartMatrix.xlsx")
teams = pd.read_excel(r"C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\Teams.xlsx")



#all 4 charts are imported correctly

'''
2. Select the year of interest for the teams

'''
######################################################
def pick_teams():
    off_team_year = int(input('Enter year of offense team: '))
    offense = input('Enter offense team abbreviation: ').upper()
    off_teams = teams[teams['Year']== off_team_year]
    
    
    def_team_year = int(input('Enter year of defense team: '))
    defense = input('Enter Defense team abbreviation: ').upper()
    def_teams = teams[teams['Year']== def_team_year]
    '''
        3. write a function that takes the name of 2 teams and returns their team ID
        '''
    for i in range(len(off_teams['TeamAbbr'])):
        if off_teams.TeamAbbr.iloc[i] == offense:
            off_ID = off_teams.TeamChartID.iloc[i]
            
    for j in range(len(def_teams['TeamAbbr'])):
        if def_teams.TeamAbbr.iloc[j] == defense:
            def_ID = def_teams.TeamChartID.iloc[j]
            
# print(get_teamID(offense,defense))
#This returns the team ids that will be used with team charts

    '''
    4. Access the play charts for the teams based on IDs
    '''    
    off_team_chart = team_data[team_data['TeamChartID']==off_ID]
    def_team_chart = team_data[team_data['TeamChartID']==def_ID] 
    return off_team_chart,def_team_chart
########################################################
#print(off_team_chart)
#This gives the offense and defense play charts!! I have my dice file already

'''
5. Call a play. Use UPCID to pick the play

pseudo code needed
high-level:
    select UPCID
    roll dice
    get result code
    use result code to get outcome code
    use outcome matrix to get result of play 
    
'''
import Dice as dice

#off_UPCID = int(input('Enter UPCID for Offense Play: '))
#1 through 9 are for offense
#def_UPCID = int(input('Enter UPCID for Deffense Play: '))
#10 through 63 are for defense
###########################################################
#off_UPCID = int(input('Enter UPCID for Offense Play: '))
def off_play(off_team_chart, off_UPCID):
    
    off_play = off_team_chart[off_team_chart['UPCID'] == off_UPCID]
    oRoll = dice.oDice()
    
    oPlay = off_play[off_play['DieRoll']==oRoll]
    oResult = oPlay['ResultCodeID'].item()
    oYards = oPlay['Yards'].item()
    return oResult, oYards, off_UPCID



#def_UPCID = int(input('Enter UPCID for Deffense Play: '))
def def_play(def_team_chart,def_UPCID):
    
    def_play = def_team_chart[def_team_chart['UPCID']== def_UPCID]
    dRoll = dice.dDice()
    
    dPlay = def_play[def_play['DieRoll']==dRoll]
    dResult = dPlay.ResultCodeID.item()
    dYards = dPlay.Yards.item()
    return dResult, dYards
#####################################################


