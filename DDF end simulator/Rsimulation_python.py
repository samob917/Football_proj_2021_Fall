'''
Simulation using NFL Fast R data for both drives

if drive does not take up whole time, pick another drive


'''
import pandas as pd
import numpy as np
import gameClass as gc
import statistics

Drive1 = pd.read_csv('Drive1.csv')
#312 rows 12 cols

Drive1b = pd.read_csv('Drive1b.csv')

Drive2_Need_TD = pd.read_csv("Drive2_Need_TD.csv")
Drive2_Need_FG = pd.read_csv("Drive2_Need_FG.csv")



    

def pick_rand_drive(Drive_num):
    #turnover = 1 if occured, 0 else
    turnover = 0
    
    
    #get size of drive chart
    num_rows, num_cols = Drive_num.shape
    #pick play
    picker = np.random.randint(0, num_rows-1)
    drive_data = Drive_num[picker:picker+1]
    
    #compute time left at end of drive in seconds
    time_at_end = str(drive_data['drive_game_clock_end'].item())
    minutes, seconds = time_at_end.split(':')
    time_left = int(minutes)*60 + int(seconds)
    
    #compute amount of time the drive took
    time_taken = int(drive_data['game_seconds_remaining'].item()) - time_left
    
    
    #determine whether there was a turnover or if yards were gained
    if drive_data['fixed_drive_result'].item() == 'Touchdown':
        yards_gained = int(drive_data['yardline_100'].item())
    
    elif drive_data['fixed_drive_result'].item() == "Turnover":
        turnover = 1
        yards_gained = 0
        
    else:
        yard_begin = int(drive_data['yardline_100'].item())
        drive_end_yards = drive_data['drive_end_yard_line'].item()
        if drive_end_yards == '50':
            yard_end = 50
        else:
            team, yard_end = drive_end_yards.split()
        
        yards_gained = yard_begin - int(yard_end)
        
    
    return yards_gained, time_taken, turnover
    



#this function sims the outcome of a full drive
#strat says whether we go for TD or FG
def sim_drive(Drive_num, game1, goal_yards, strat):
    success = 1000000
    yds = 10000
    time = 10000
    
    
    #this picks plays
    while game1.time_left > 0 and game1.possession and game1.ball_on > 0:
        
            yards, time, turnover = pick_rand_drive(Drive_num)
            
            game1.ball_on -= yards
            game1.time_left -= time
            
            if turnover == 1:
                game1.possession = not game1.possession
                
    '''
         Possibilities: time left = -x. possession = false, ball on = -y
         IF time left -x, end
         pos, end
         ball -, win
         
    '''
   
    #check what happens            
    if game1.ball_on <= 0 and game1.time_left >= 0 and game1.possession:
        if strat == 0:
            game1.score1 += 7
            yds = goal_yards
            time = game1.time_left
            success = 1
            
        elif strat ==1:
            game1.score1 += 3
            yds = goal_yards
            time = game1.time_left
            success = 1
            
    elif game1.time_left <= 0 and game1.ball_on > 0 and game1.possession:
        yds = goal_yards-game1.ball_on
        time = 0
        success = 0
        
    
    elif game1.possession == False:
        yds = goal_yards-game1.ball_on
        time = 0
        success = 0
    elif game1.time_left > 0 and game1.ball_on > 0:
        yds = goal_yards-game1.ball_on
        time = 0
        success = 0
        
    elif game1.time_left <= 0 and game1.ball_on < 0:
        if strat == 1:
            success = 1
            time = 0
            yds = goal_yards
        else:
            success = 0
            time = 0
            yds = yards
        
    return success, yds, time
    
'''    
goal_yards = 50   
game1 = gc.game(0,10,120, 3, 3, True, goal_yards, 1, 10)

x,y,z = sim_drive(Drive1, game1, goal_yards,0)
print(x,y,z)
'''    
#TDF is 1 if td first, 0 otherwise
def sim_game(num_sims, TDF):
    yards_per_drive = []
    successes = []
    for i in range(num_sims):
        if TDF == 1:
            goal_yards = 50
            game1 = gc.game(0,10,120, 3, 3, True, goal_yards, 1, 10)
        
            success,yards,time = sim_drive(Drive1b, game1, goal_yards, 0)
            #print(success, yards, time)
            yards_per_drive.append(yards)
            
            if success == 1:
                goal_yards == 25
                game1 = gc.game(7,10, time, 3, 3, True, goal_yards, 1, 10)
                
                success, yards, time = sim_drive(Drive2_Need_FG, game1, goal_yards, 1)
                if success == 1:
                    successes.append(1)
                else:
                    successes.append(0)
            else: 
                successes.append(0)
            
        if TDF == 0:
            goal_yards = 20
            game1 = gc.game(0,10,120, 3, 3, True, goal_yards, 1, 10)
        
            success, yards, time = sim_drive(Drive1b, game1, goal_yards, 1)
            yards_per_drive.append(yards)
            #print(success, yards, time)
            if success == 1:
                goal_yards == 55
                game1 = gc.game(3,10, time, 3, 3, True, goal_yards, 1, 10)
            
                success,yards,time = sim_drive(Drive2_Need_TD, game1, goal_yards, 0)
                if success == 1:
                    successes.append(1)
                else:
                    successes.append(0)
            else: 
                successes.append(0)
        
    return successes, yards_per_drive




def driver3(sims):
    
    tdf_success, tdf_yards = sim_game(sims, 1)
    fgf_success, fgf_yards = sim_game(sims, 0)
    
    
    tdf_suc_rate = statistics.mean(tdf_success) * 100
    fgf_suc_rate = statistics.mean(fgf_success) * 100
    
    return tdf_suc_rate, fgf_suc_rate
        

print(driver3(10000))

    

        
        
  
    
    

    
        
        