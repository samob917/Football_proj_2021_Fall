
import BAL_vs_PHI as BP
import numpy as np
import Dice as dice
'''
Outcomes: 
    LOSE- turnover
    PI- pass interference
    OFFX- Penalty on the offense
    DEFX- penalty on the defense
    TD-Touchdown
    0- incomplete pass or 0 yard gain
    #- gain of that many yards

'''

def play():
    oPlay = np.random.randint(3)
    #pick a random number, 0 is medium pass, 1 is long pass, 2 is sideline pass
    dPlay = np.random.randint(3)
    #1 is std, 2 is nickel, 3 is dime
    
    
    #define the team and the result- results depend on dice roll
    oRoll = dice.oDice() - 10
    ravens = BP.Ravens()
    if oPlay == 0:
        oResult = ravens.medium_pass[oRoll]
        
    elif oPlay == 1:
        oResult= ravens.long_pass[oRoll]
    else:
        oResult = ravens.sideline_pass[oRoll]
        
    
    
    #define team on defense and result- result depends on dice roll and offense play chosen
    dRoll = dice.dDice()-1
    eagles = BP.Eagles()
    if dPlay == 0:
        dResult = eagles.std[dRoll][oPlay]
        
    elif dPlay == 1:
        dResult = eagles.pass_nickel[dRoll][oPlay]
    
    else:
        dResult = eagles.pass_dime[dRoll][oPlay]
        
    print(oResult)
    print(dResult)
    print('------------')
# Now we have 2 results let us analyze them:
    if ('INT' in str(oResult) or 'INT' in str(dResult)) and ('(' not in str(dResult)):
        #print('int happened')
        return 'LOSE'
    
    
    elif 'QT' in str(oResult) or 'QT' in str(dResult):
        #print('QT happened')
        oRoll2 = dice.oDice()-10
        oQT = ravens.QT[oRoll2]
        if 'F' in str(oQT):
            return 'LOSE'
        else:
            dRoll2 = dice.dDice()-1
            dQT = eagles.QT_contain[dRoll2]
            
            return oQT + dQT
    elif 'PI' in str(oResult) or 'PI' in str(dResult):
        #print('PI happened')
        return 'PI'
    
    elif 'OFF' in str(oResult) or 'DEF' in str(oResult):
        #print('penalty occured')
        return oResult
    
    elif '(' in str(oResult) or '(' in str(dResult):
        #print('parenthesis happened')
        if 'TD' in str(dResult):
            return 'TD'
        else:
            dResult = dResult.replace('(','')
            dResult = dResult.replace(')','')
            dResult = int(dResult)
            return dResult
    elif 'B' in str(oResult) or 'B' in str(dResult):
        #print('incomplete')
        return 0
    
    else:
        #print('normal')
        return oResult + dResult
'''
Outcomes: 
    LOSE- turnover
    PI- pass interference
    OFFX- Penalty on the offense
    DEFX- penalty on the defense
    TD-Touchdown
    0- incomplete pass or 0 yard gain
    #- gain of that many yards

'''  
#Take five parameters, update each of the last 4 based on play_result
def updateDrive(play_result,down, yards_to_first, distance, time):
    #IF turnover, return lose and game over
    if play_result == 'LOSE':
        down = 0
        yards_to_first = 100
        distance = 100
        time = 0
        return 'LOSE'
    
    elif play_result == 'PI':
        #Pass interference, for standardization we will say PIs are 20 yards
        #for PI within 20 yards, takes 8 seconds, over 20 takes 10 seconds
        down = 1
        
        if distance <= 20:
            distance = 1
            yards_to_first = 1
            time = time - 8
        else:
            distance = distance-20
            time = time -10
            if distance >= 10:
                yards_to_first = 10
            else:
                yards_to_first = distance
        
    elif 'OFF' in str(play_result):
        #5 seconds for an offensive penalty
        pen_yards = int(play_result.replace('OFF',""))
        yards_to_first = yards_to_first + pen_yards
        distance = distance + pen_yards
        time = time - 5
        
    elif 'DEF' in str(play_result):
        #5 second run off and handle all posibilities
    
        time = time - 5
        if 'X' not in str(play_result):
            pen_yards = int(play_result.replace('DEF',""))
        else:
            down = 1
            pen_yards = int(play_result.replace('DEF',"").replace('X',""))
        if pen_yards >= 10:
            down = 1
            if pen_yards >= distance:
                distance = 1
                yards_to_first = 1
            else:
                distance = distance-pen_yards
                if distance < 10:
                    yards_to_first = distance
                else:
                    yards_to_first = 10
                
        elif pen_yards >= yards_to_first and pen_yards < distance:
            down = 1
            distance = distance - pen_yards
            if distance < 10:
                yards_to_first = distance
            else:
                yards_to_first = 10
        elif pen_yards >= yards_to_first and pen_yards >= distance:
            if yards_to_first == distance:
                distance = 1
                yards_to_first = 1
            else:
                down = 1
                distance = 1
                yards_to_first = 1
        elif pen_yards < yards_to_first:
            distance = distance - pen_yards
            yards_to_first = yards_to_first - pen_yards
                
        
    elif 'TD' in str(play_result):
        time = time - 10
        #return 'TD'
    
    elif play_result == 0:
        time = time - 8
        down = down + 1
    
    else:
        #print('ELSE RAN')
        time = time - 10
        if play_result < yards_to_first:
            down = down + 1
            yards_to_first = yards_to_first - play_result
            distance = distance - play_result
        elif play_result > yards_to_first and play_result < distance:
            down = 1
            distance = distance - play_result
            if distance <= 10:
                yards_to_first = distance
            else:
                yards_to_first = 10
        elif play_result > distance:
            #return 'TD'
            distance = -1
            yards_to_first = -1
            down = -1
        
    return down,yards_to_first,distance,time
        
                
            
    
    
    
    
if __name__ == "__main__":
    outcomes = []
    distance = 75
    yards_to_first = 10
    time = 200
    down = 1
    #print(updateDrive(100,2,10,25,100))
    # for i in range(10):
    #     outcomes.append(play())
    # print(outcomes)
    
    # for play in outcomes:
    #     if "TD" in str(play):
    #         print('TD')
    #         break
    #     elif 'LOSE' in str(play):
    #         print('LOSE')
    #         break
    #     else:    
    #         down,yards_to_first,distance,time = updateDrive(play,down, yards_to_first, distance, time)
    #     print('NEW GAME STATE:')
    #     print('{} yards to first, {} distance, {}down, {}time'.format(yards_to_first, distance,down,time))
            
    '''
    Now I will try to simulate a signel drive
    '''
    while (time>0) and (distance>0) and (down <5):
        play1 = play()
        if "TD" in str(play):
            print('TD')
            break
        elif 'LOSE' in str(play):
            print('LOSE')
            break
        else:  
            own,yards_to_first,distance,time = updateDrive(play,down,yards_to_first,distance,time)
        print('NEW GAME STATE:')
        print('{} yards to first, {} distance, {}down, {}time'.format(yards_to_first, distance,down,time))
    