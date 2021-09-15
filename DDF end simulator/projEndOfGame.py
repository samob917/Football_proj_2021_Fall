#simulator pseudocode
import numpy as np
"""
pick leading team
pick losing team

define gamestate (time left, ball position, timeouts)

scenario 1:
If ball position is in fieldgoal range, kick fieldgoal
else:
    run play to get in field goalrange.
        run pass play: randomly pick from a few
    take time off clock after play
    move ball position
    repeat the above until in field goal range
    
    kick field goal

then
    Kickoff regular 
    or
    onside kick
    
    if regular
        randomly pick defense plays aimed at stopping run
        run plays
        call timeouts 
        
        if first down, game end
        if 4th down 
            punt 
            
            then run random plays until touchdown or timeruns out
            
    same if onside
    
"""

def passPlay(time, yards_to_go):
    play_result_yards = 0
    if time > 60:
        #randomly pick 1,2,3
        pick = np.random.randint(1,3)
        if pick == 1:
            #run medium pass play
            time = time - 8
        if pick == 2:
            #run long pass play
            time = time - 10
        if pick == 3:
            #run side line pass
            time = time - 6
            
        yards_to_go = yards_to_go - play_result_yards
        if yards_to_go <= 0:
            return #touchdown
        pass
        
    #defensive side:
    #defense can run std or one of the 2 passing defenses
    #after randomly picking a defense, do the above
def runPlay(time, yards_to_go,Dteam):
    #do same as in pass play, run this less frequently
    pass
def fieldgoal():
    #kick a field goal, return 1 if good, 0 else
    pass
    
def onsideKick():
    pass

def kickoff():
    pass

def punt():
    pass

def endOfGame1():
    time = 120
    time_out = 3
    yards_to_go = 50
    yard_line_for_fg = 35
    
    
    #pass or run play
    #check if in fg range
    
    if yards_to_go <= yard_line_for_fg:
        a = fieldgoal()
        
        if a == 0:
            return 0
    
    if a == 1:
        kickoff()
        #update game state
        #run run plays
        #use time outs
        
    punt()
    
    while yards_to_go > 0 and time > 0:
        passPlay(time, yards_to_go)
        
    if yards_to_go == 0:
        return 1
    else: 
        return 0
    
        
    
    

