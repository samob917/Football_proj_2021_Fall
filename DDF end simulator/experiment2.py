'''
experiment 2:
    run a drive
        if successful:
            take time remaining
            run drive with time remaining
            if successful:
                return 1
            else:
                return 0

'''
import teams_for_analysis_python as ta
import functions_for_experiment1 as fun
import Dice as dice
import simulator_with_charts as sim
import gameClass as gc
import numpy as np
import after_drive1 as ad
import matplotlib.pyplot as plt
import statistics
import pandas as pd

#situational makes a fieldgoal impossible if down by 7
def sim_game(off_chart,def_chart, goal_yards,seconds, situational):
    
#define the game
        game1 = gc.game(0,10,seconds, 3, 3, True, goal_yards, 1, 10)


# #pick play
# oUPCID = 0;
# dUPCID = 0;

# #run plays
# oResult,oYards,oUPCID = sim.off_play(off_chart, oUPCID)
# dResult,dYards = sim.def_play(def_chart, dUPCID)
# print(oResult,oYards)
# print(dResult,dYards)

# game1.update_game(oResult,dResult,oYards,dYards)
# game1.update_time(oUPCID, oResult, dResult)


        oUPCID_dict={1: "line plunge",2: "off tackle" , 3: "end run" ,4: "draw" ,
              5: "screen pass"  ,6: "short pass"  ,7: "medium pass" ,8: "long pass",9: "sideline pass"}

#Defense runs A,D,E 5 through 9: numbers: 14-18, 41-45, 50-54
        dUPCID_list = [14,15,16,17,18,41,42,43,44,45,50,51,52,53,54]
#NOW FOR A DRIVE:
        num_plays = 0
        
        while game1.time_left > 0 and game1.down <= 4 and game1.possession and game1.ball_on > 0:
            num_plays += 1
    #pick play
    
            '''
    oUPCID set at 4,10 if 1 run play is included (include off tackle)
            '''
            oUPCID = np.random.randint(4,10) #include this assumption in the paper
            if oUPCID ==4:
                oUPCID = 2
            dUPCID_picker = np.random.randint(1, len(dUPCID_list))
            dUPCID = dUPCID_list[dUPCID_picker]
            oResult,oYards,oUPCID = sim.off_play(off_chart, oUPCID)
            print(oResult,oYards)
            dResult,dYards = sim.def_play(def_chart, dUPCID)
            print(dResult,dYards)
    
            game1.update_game(oResult,dResult,oYards,dYards,off_chart)
        
            game1.update_time(oUPCID, oResult, dResult)
            print('{} seconds left, offense ran {}, defense ran {},'.format(game1.time_left, oUPCID_dict[oUPCID], dUPCID),end="")
            print('ball on the {} yardline, {} down, {} yards to go'.format(game1.ball_on, game1.down, game1.dist_to_first))
            print('It is {} that the team maintained possession'.format(game1.possession))
            print("---------------------------------")
    
            #need timeout logic
            if game1.to1 > 0 and game1.time_left - 25 <= 0:
                game1.to1 -= 1
            else:
                game1.time_left -= 15
    
            if game1.ball_on <= 0:
                game1.score1 += 7
                #outcome = ad.prob_of_winning(game1.time_left, strategy)
                print("success")
                outcome = 1
                break
            #do a two point coversion
            if game1.down == 4:
                if game1.ball_on > 5 and game1.ball_on < 45 and game1.dist_to_first > 5 and situational == 0:
                    #fieldgoal
                    game1.score1 += 3
                    outcome = 1
                    #prob of winning
                    #outcome = ad.prob_of_winning(game1.time_left, 1)
                    break
                else:
                    continue

        if game1.time_left <= 0:
            print("lose")
            outcome = 0
            
        if game1.down > 4:
            print("lose")
            outcome = 0
            
        if not game1.possession:
            if game1.score1 > 0:
                #basically if team scores a td
                if game1.time_left>0:
                    print("success")
                    outcome = 1
                
            else:
                print("lose")
                outcome = 0
                
            
        
    
        print(outcome)
        print("-----------------------------------------------")
        print('result of drive')
        print('{} seconds left, {} score differential'.format(game1.time_left, (game1.score2-game1.score1)), end="")
        print(', ball on the {} yardline, {} down, {} yards to go'.format(game1.ball_on, game1.down, game1.dist_to_first))
        print('It is {} that the team maintained possession'.format(game1.possession))
        print(num_plays)
        
        time_remaining = game1.time_left
        
        score = game1.score1
    
        return outcome, time_remaining, score
    
    
    

#DRIVER

def experiment2(strategy, num_sims, offense_list, defense_list, yardline_start,start_time):
    if strategy == 1:
        goal_end_yardline = 0
    elif strategy == 2:
        goal_end_yardline = 30
    
    goal_yards = yardline_start - goal_end_yardline
    success = []
    
    for i in range(num_sims):
    #need to pick teams
        off_chart, def_chart = fun.choose_opponents(offense_list, defense_list)
    
        if strategy == 1:
            outcome, time_remaining, score = sim_game(off_chart, def_chart, goal_yards, start_time, 0)
        
            if outcome == 1 and score == 3:
                outcome, time_remaining, score = sim_game(off_chart, def_chart, 55, time_remaining, 1)
                if outcome == 1:
                    success.append(1)
                else:
                    success.append(0)
            
            elif outcome == 1 and score == 7:
                outcome, time_remaining, score = sim_game(off_chart, def_chart, 25, time_remaining, 0)
                if outcome == 1:
                    success.append(1)
                else:
                    success.append(0)
            else:
                success.append(0)
        
        if strategy == 2:
            outcome, time_remaining, score = sim_game(off_chart, def_chart, goal_yards, start_time, 0)
        
            if outcome == 1:
                outcome, time_remaining, score = sim_game(off_chart, def_chart, 55, time_remaining, 1)
                if outcome == 1:
                    success.append(1)
                else:
                    success.append(0)
        
            else:
                success.append(0)
            
    return success
            



def driver2(offense_list, defense_list, sims, yardline_start,start_time):
#strategy 1
    data1 = experiment2(1, sims, offense_list, defense_list, yardline_start,start_time)

#strategy 2
    data2 = experiment2(2, sims, offense_list, defense_list, yardline_start,start_time)

    a = statistics.mean(data1) * 100
    b = statistics.mean(data2) * 100


    print("Usual strategy- prob of winning/tying:")
    print("mean: {:.3f}".format(a))

    print("New strategy- prob of winning/tying:")
    print("mean: {:.3f}".format(b))
    
    strat1_mean = a
    strat2_mean = b
    return strat1_mean, strat2_mean
