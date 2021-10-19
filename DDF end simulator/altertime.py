
'''
This code will run both experiments and return the means

'''

import teams_for_analysis_python as ta
import functions_for_experiment1 as fun1
import experiment2 as fun2


levels = ['best', 'med', 'bad']



outcomes_exp1 = []
outcomes_exp2 = []
outcomes_yds = []




for i in levels:
    for j in levels:
        offense_list = eval('ta.'+ i + '_off')
        defense_list = eval('ta.'+ j + '_def')
        for seconds_to_go in range(30,300,30):
        
            yardline_start = 50
            
            #edit this to try buckets
            tdf1, fgf1, tdf_yds, fgf_yds = fun1.driver1(offense_list, defense_list, 10, yardline_start,seconds_to_go)
            tdf2, fgf2 = fun2.driver2(offense_list, defense_list, 10, yardline_start,seconds_to_go)
            
            outcomes_exp1.append([seconds_to_go, tdf1, fgf1])
            outcomes_exp2.append([seconds_to_go, tdf2, fgf2])
            outcomes_yds.append([tdf_yds, fgf_yds])

        print(outcomes_exp1)
        print(outcomes_exp2)
        
'''   
print('==============================')
print('THE RESULTS ARE')
print('==============================')

print('Best Offense vs Best Defense')
print('Average Yards by Strategy (on first drive)')
print('tdf average yards for first drive: {:.3f}'.format(outcomes_yds[0][0]))
print('fgf average yards for first drive: {:.3f}'.format(outcomes_yds[0][1]))

print('Experiment 1')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp1[0][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp1[0][1]))

print('Experiment 2')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp2[0][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp2[0][1]))
print('==============================')


print('Best Offense vs Medium Defense')
print('Average Yards by Strategy (on first drive)')
print('tdf average yards for first drive: {:.3f}'.format(outcomes_yds[1][0]))
print('fgf average yards for first drive: {:.3f}'.format(outcomes_yds[1][1]))
print('Experiment 1')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp1[1][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp1[1][1]))

print('Experiment 2')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp2[1][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp2[1][1]))
print('==============================')


print('Best Offense vs Bad Defense')
print('Average Yards by Strategy (on first drive)')
print('tdf average yards for first drive: {:.3f}'.format(outcomes_yds[2][0]))
print('fgf average yards for first drive: {:.3f}'.format(outcomes_yds[2][1]))
print('Experiment 1')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp1[2][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp1[2][1]))

print('Experiment 2')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp2[2][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp2[2][1]))
print('==============================')


print('Medium Offense vs Best Defense')
print('Average Yards by Strategy (on first drive)')
print('tdf average yards for first drive: {:.3f}'.format(outcomes_yds[3][0]))
print('fgf average yards for first drive: {:.3f}'.format(outcomes_yds[3][1]))
print('Experiment 1')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp1[3][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp1[3][1]))

print('Experiment 2')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp2[3][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp2[3][1]))
print('==============================')


print('Medium Offense vs Medium Defense')
print('Average Yards by Strategy (on first drive)')
print('tdf average yards for first drive: {:.3f}'.format(outcomes_yds[4][0]))
print('fgf average yards for first drive: {:.3f}'.format(outcomes_yds[4][1]))
print('Experiment 1')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp1[4][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp1[4][1]))

print('Experiment 2')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp2[4][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp2[4][1]))
print('==============================')


print('Medium Offense vs Bad Defense')
print('Average Yards by Strategy (on first drive)')
print('tdf average yards for first drive: {:.3f}'.format(outcomes_yds[5][0]))
print('fgf average yards for first drive: {:.3f}'.format(outcomes_yds[5][1]))
print('Experiment 1')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp1[5][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp1[5][1]))

print('Experiment 2')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp2[5][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp2[5][1]))
print('==============================')


print('Bad Offense vs Best Defense')
print('Average Yards by Strategy (on first drive)')
print('tdf average yards for first drive: {:.3f}'.format(outcomes_yds[6][0]))
print('fgf average yards for first drive: {:.3f}'.format(outcomes_yds[6][1]))
print('Experiment 1')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp1[6][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp1[6][1]))

print('Experiment 2')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp2[6][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp2[6][1]))
print('==============================')


print('Bad Offense vs Medium Defense')
print('Average Yards by Strategy (on first drive)')
print('tdf average yards for first drive: {:.3f}'.format(outcomes_yds[7][0]))
print('fgf average yards for first drive: {:.3f}'.format(outcomes_yds[7][1]))
print('Experiment 1')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp1[7][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp1[7][1]))

print('Experiment 2')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp2[7][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp2[7][1]))
print('==============================')


print('Bad Offense vs Bad Defense')
print('Average Yards by Strategy (on first drive)')
print('tdf average yards for first drive: {:.3f}'.format(outcomes_yds[8][0]))
print('fgf average yards for first drive: {:.3f}'.format(outcomes_yds[8][1]))
print('Experiment 1')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp1[8][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp1[8][1]))

print('Experiment 2')
print('tdf mean success rate: {:.3f}'.format(outcomes_exp2[8][0]))
print('fgf mean success rate: {:.3f}'.format(outcomes_exp2[8][1]))
print('==============================')
'''  