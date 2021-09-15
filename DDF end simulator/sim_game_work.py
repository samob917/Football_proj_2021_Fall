'''
This puts together the other files and begins to run a drive
'''
import Dice as dice
import simulator_with_charts as sim
import gameClass as gc
import numpy as np


#define the game
game1 = gc.game(0,10,120,3,3,True,80,1,10)

#pick teams
off_chart,def_chart = sim.pick_teams()

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
    #went to 4,10 to include run play
    oUPCID = np.random.randint(4,10) #alter these
    if oUPCID == 4:
        oUPCID == 2
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
        game1.score1 += 8
        break
    #do a two point coversion
    if game1.down == 4:
        if game1.ball_on > 5 and game1.ball_on < 45 and game1.dist_to_first > 5:
            #fieldgoal
            game1.score1 += 3
            break
        else:
            continue

#play by play included
#final fg does it matter 


if game1.time_left <= 0:
    print("lose")
if game1.down > 4:
    print("lose")
if not game1.possession:
    print("lose")
    

print("-----------------------------------------------")
print('result of drive')
print('{} seconds left, {} score differential'.format(game1.time_left, (game1.score2-game1.score1)), end="")
print(', ball on the {} yardline, {} down, {} yards to go'.format(game1.ball_on, game1.down, game1.dist_to_first))
print('It is {} that the team maintained possession'.format(game1.possession))
print(num_plays)