import teams_for_analysis_python as ta
import numpy as np
import pandas as pd
import simulator as s
import statistics
import matplotlib.pyplot as plt

team_data = pd.read_excel(r'C:\Users\Sam Oberly\OneDrive - Johns Hopkins\Desktop\Football_proj_2021_Fall\DDF end simulator\TeamData.xlsx')
#result_code = pd.read_excel(r'C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\ResultCodes.xlsx')
#play_chart_matrix = pd.read_excel(r"C:\Users\Sam Oberly\OneDrive - Johns Hopkins\DDF end simulator\PlayChartMatrix.xlsx")
teams = pd.read_excel(r"C:\Users\Sam Oberly\OneDrive - Johns Hopkins\Desktop\Football_proj_2021_Fall\DDF end simulator\Teams.xlsx")



def choose_opponents(offense_list, defense_list):
    
    picker_o  = np.random.randint(15)
    a,b = offense_list[picker_o].split()
    year_o = int(a)
    team_o = b
    #print(team_o)
    
    picker_d  = np.random.randint(15)
    c,d = defense_list[picker_d].split()
    year_d = int(c)
    team_d = d
    #print(team_d)
    

    off_team_year = year_o
    offense = team_o
    off_teams = teams[teams['Year']== off_team_year]
    #print(off_teams)
    
    
    def_team_year = year_d
    defense = team_d
    def_teams = teams[teams['Year']== def_team_year]
    #print(def_teams)
    '''
        3. write a function that takes the name of 2 teams and returns their team ID
        '''
    for i in range(len(off_teams['TeamAbbr'])):
        if off_teams.TeamAbbr.iloc[i] == offense:
            off_ID = off_teams.TeamChartID.iloc[i]
    #print(off_ID)
            
    for j in range(len(def_teams['TeamAbbr'])):
        if def_teams.TeamAbbr.iloc[j] == defense:
            def_ID = def_teams.TeamChartID.iloc[j]
    #print(def_ID)
            
# print(get_teamID(offense,defense))
#This returns the team ids that will be used with team charts

    '''
    4. Access the play charts for the teams based on IDs
    '''    
    off_team_chart = team_data[team_data['TeamChartID']==off_ID]
    def_team_chart = team_data[team_data['TeamChartID']==def_ID] 
    return off_team_chart,def_team_chart


def experiment1(offense_list, defense_list, num_sims, yards_to_go, strategy,seconds_to_go):
    final_data_chart = []
    final_time_remaining = []
    final_yards_gained = []
    for i in range(num_sims):
        off_chart, def_chart = choose_opponents(offense_list, defense_list)
        data_chart, time, yards = s.sim_games(off_chart,def_chart, yards_to_go, 1, strategy,seconds_to_go)
        
        final_data_chart.append(data_chart[0])
        final_time_remaining.append(time[0])
        final_yards_gained.append(yards[0])
    return final_data_chart, final_time_remaining, final_yards_gained
    
#seconds_to_go = 120
#a,b,c = experiment1(ta.best_off, ta.bad_def, 1000, 50, 0, seconds_to_go)
#print(statistics.mean(c))

def driver1(offense_list, defense_list, sims, yardline_start,seconds_to_go):


    data_strat0,time0, yards0 = experiment1(offense_list,defense_list, sims, yardline_start, 0,seconds_to_go)

    goal_yards = yardline_start - 30
    data_strat1,time1, yards1 = experiment1(offense_list,defense_list, sims, goal_yards, 1,seconds_to_go)

    a = statistics.mean(data_strat0)
    b = statistics.stdev(data_strat0)
    c = np.max(data_strat0)
    strat1_mean = a

    x = statistics.mean(data_strat1)
    y = statistics.stdev(data_strat1)
    z = np.max(data_strat1)
    strat2_mean = x

    print('====================================')

    print("Usual strategy- prob of winning/tying:")
    print("mean: {:.3f}".format(a))
    print("standard deviation {:.3f}".format(b))
    print("max: {:.3f}".format(c))
    print("New strategy- prob of winning:")
    print("mean: {:.3f}".format(x))
    print("standard deviation {:.3f}".format(y))
    print("max: {:.3f}".format(z))
    

    w = statistics.mean(time0)
    t = statistics.stdev(time0)
    s = np.max(time0)


    d = statistics.mean(time1)
    e = statistics.stdev(time1)
    f = np.max(time1)

    print('=======================================')

    print("Usual strategy- time left:")
    print("mean: {:.3f}".format(w))
    print("standard deviation {:.3f}".format(t))
    print("max: {:.3f}".format(s))
    print("New strategy- time left:")
    print("mean: {:.3f}".format(d))
    print("standard deviation {:.3f}".format(e))
    print("max: {:.3f}".format(f))
    
    
    l = statistics.mean(yards0)
    m = statistics.stdev(yards0)
    strat1_yards = l
    
    n = statistics.mean(yards1)
    o = statistics.stdev(yards1)
    strat2_yards = n
    print('=======================================')

    print("Usual strategy- yards gained:")
    print("mean: {:.3f}".format(l))
    print("standard deviation {:.3f}".format(m))
    print("Usual strategy- yards gained:")
    print("mean: {:.3f}".format(n))
    print("standard deviation {:.3f}".format(o))
    
    
    
    return strat1_mean, strat2_mean, strat1_yards, strat2_yards

'''


offense_list = ta.med_off
defense_list = ta.med_def



#pick teams
off_chart,def_chart = choose_opponents(offense_list, defense_list)
data_strat0,time0 = s.sim_games(off_chart,def_chart, 50, 10000, 0)

off_chart,def_chart = choose_opponents(offense_list, defense_list)
data_strat1,time1 = s.sim_games(off_chart, def_chart, 20, 10000, 1)




data = [data_strat0,data_strat1]
plt.boxplot(data)


a = statistics.mean(data_strat0)
b = statistics.stdev(data_strat0)
c = np.max(data_strat0)

x = statistics.mean(data_strat1)
y = statistics.stdev(data_strat1)
z = np.max(data_strat1)

print('====================================')

print("Usual strategy- prob of winning/tying:")
print("mean: {:.3f}".format(a))
print("standard deviation {:.3f}".format(b))
print("max: {:.3f}".format(c))
print("New strategy- prob of winning:")
print("mean: {:.3f}".format(x))
print("standard deviation {:.3f}".format(y))
print("max: {:.3f}".format(z))
    

w = statistics.mean(time0)
t = statistics.stdev(time0)
s = np.max(time0)


d = statistics.mean(time1)
e = statistics.stdev(time1)
f = np.max(time1)

print('=======================================')

print("Usual strategy- time left:")
print("mean: {:.3f}".format(w))
print("standard deviation {:.3f}".format(t))
print("max: {:.3f}".format(s))
print("New strategy- time left:")
print("mean: {:.3f}".format(d))
print("standard deviation {:.3f}".format(e))
print("max: {:.3f}".format(f))
    
'''
