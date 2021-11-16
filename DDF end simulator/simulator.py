'''
This puts together the other files and begins to run a drive
'''
import Dice as dice
import simulator_with_charts as sim
import gameClass as gc
import numpy as np
import after_drive1 as ad
import matplotlib.pyplot as plt
import statistics

def sim_games(off_chart,def_chart, goal_yards, num_games, strategy,seconds_to_go):
    data_chart = []
    time_remaining= []
    yards_gained = []
    
    
    win_prob = 0
    for z in range(num_games):
#define the game
        game1 = gc.game(0,10,seconds_to_go, 3, 3, True, goal_yards, 1, 10)


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
    #edited to pick from 4,10 to include runs
            oUPCID = np.random.randint(4,10) #include this assumption in the paper
            if oUPCID == 4:
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
                outcome = ad.prob_of_winning(game1.time_left, strategy)
                print("success")
                break
    #do a two point coversion
            if game1.down == 4:
                if game1.ball_on > 5 and game1.ball_on < 45 and game1.dist_to_first > 5:
                    #fieldgoal
                    game1.score1 += 3
                    
                    #prob of winning
                    outcome = ad.prob_of_winning(game1.time_left, 1)
                    break
                else:
                    continue

#play by play included
#final fg does it matter 


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
                    outcome = ad.prob_of_winning(game1.time_left, strategy)
                    print("success")
                
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
        win_prob += outcome
        data_chart.append(outcome)
        
        #chart for time remaining
        time_remaining.append(game1.time_left)
        
        
        if outcome == 1 and game1.score1 == 7:
            yards_gained_drive = goal_yards
        else:
            yards_gained_drive = goal_yards - game1.ball_on
        
        yards_gained.append(yards_gained_drive)
        
        
        
    
    return data_chart, time_remaining, yards_gained


'''
#pick teams
off_chart,def_chart = sim.pick_teams()
data_strat0,ok = sim_games(off_chart,def_chart, 50, 1000, 0)
data_strat1,ok2 = sim_games(off_chart, def_chart, 20, 1000, 1)
data = [data_strat0,data_strat1]
plt.boxplot(data)


a = statistics.mean(data_strat0)
b = statistics.stdev(data_strat0)
c = np.max(data_strat0)

x = statistics.mean(data_strat1)
y = statistics.stdev(data_strat1)
z = np.max(data_strat1)

print("Usual strategy:")
print("mean: {:.3f}".format(a))
print("standard deviation {:.3f}".format(b))
print("max: {:.3f}".format(c))
print("New strategy:")
print("mean: {:.3f}".format(x))
print("standard deviation {:.3f}".format(y))
print("max: {:.3f}".format(z))
    

w = statistics.mean(ok)
t = statistics.stdev(ok)
s = np.max(ok)
print(w,t,s)

d = statistics.mean(ok2)
e = statistics.stdev(ok2)
f = np.max(ok2)
print(d,e,f)
'''



'''
random teams picked by matlab:
    1st set of 9 is 2015, 2nd is 2016... 5th is 2019
    Offense: 
            1 7 5 21 19 15 32 25 24
            3 10 5 11 19 17 24 31 30 
            7 1  2 14 18 16 30 23 25 
            6 4 1 18  13 12 30 26 27 
            5 2  7 20 18 14 30 24 28
    Defense: 
            10 4 1 14 11 17 31 27 32 
            1 2 3 19 13 14 30 24 23 
            2 10 7 13 16 19 31 29 23 
            9 3 2 12 13 18 29 24 26 
            4 2 3 19 22 17 23 32 26
        
'''