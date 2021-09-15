import drive_simulator as dr



try:
    outcomes = []
    
    for i in range(100):
        result = dr.fullDrive(1,10,75,120)
        outcomes.append(result[0])
        print(result[0])
        print(result[1])
    
    #print(outcomes)
    wins = sum(outcomes)
    win_percentage = wins/ len(outcomes)
    print(win_percentage)
except:
    print('error')
    
    
'''
Working simulator, gets caught up at some point but simulates a drive from any starting point
GIVES: outcome and time at the end of the drive
ISSUES: time is much quicker than expected, should add about 10-15 seconds between each play
create histogram and number of plays
'''
==============================
THE RESULTS ARE
==============================
Best Offense vs Best Defense
Average Yards by Strategy (on first drive)
tdf average yards for first drive: 31.788
fgf average yards for first drive: 18.300
Experiment 1
tdf mean success rate: 8.510
fgf mean success rate: 10.250
Experiment 2
tdf mean success rate: 9.400
fgf mean success rate: 5.900
==============================
Best Offense vs Medium Defense
Average Yards by Strategy (on first drive)
tdf average yards for first drive: 34.571
fgf average yards for first drive: 20.331
Experiment 1
tdf mean success rate: 9.626
fgf mean success rate: 11.177
Experiment 2
tdf mean success rate: 10.800
fgf mean success rate: 10.900
==============================
Best Offense vs Bad Defense
Average Yards by Strategy (on first drive)
tdf average yards for first drive: 36.309
fgf average yards for first drive: 21.225
Experiment 1
tdf mean success rate: 10.239
fgf mean success rate: 10.888
Experiment 2
tdf mean success rate: 12.300
fgf mean success rate: 12.200
==============================
Medium Offense vs Best Defense
Average Yards by Strategy (on first drive)
tdf average yards for first drive: 26.000
fgf average yards for first drive: 17.015
Experiment 1
tdf mean success rate: 6.011
fgf mean success rate: 9.982
Experiment 2
tdf mean success rate: 6.000
fgf mean success rate: 6.400
==============================
Medium Offense vs Medium Defense
Average Yards by Strategy (on first drive)
tdf average yards for first drive: 31.733
fgf average yards for first drive: 19.265
Experiment 1
tdf mean success rate: 8.417
fgf mean success rate: 10.413
Experiment 2
tdf mean success rate: 7.600
fgf mean success rate: 7.500
==============================
Medium Offense vs Bad Defense
Average Yards by Strategy (on first drive)
tdf average yards for first drive: 33.563
fgf average yards for first drive: 20.551
Experiment 1
tdf mean success rate: 9.401
fgf mean success rate: 10.737
Experiment 2
tdf mean success rate: 9.800
fgf mean success rate: 7.800
==============================
Bad Offense vs Best Defense
Average Yards by Strategy (on first drive)
tdf average yards for first drive: 21.711
fgf average yards for first drive: 14.516
Experiment 1
tdf mean success rate: 4.537
fgf mean success rate: 9.838
Experiment 2
tdf mean success rate: 5.200
fgf mean success rate: 4.000
==============================
Bad Offense vs Medium Defense
Average Yards by Strategy (on first drive)
tdf average yards for first drive: 27.222
fgf average yards for first drive: 17.551
Experiment 1
tdf mean success rate: 6.817
fgf mean success rate: 9.898
Experiment 2
tdf mean success rate: 5.400
fgf mean success rate: 4.900
==============================
Bad Offense vs Bad Defense
Average Yards by Strategy (on first drive)
tdf average yards for first drive: 29.635
fgf average yards for first drive: 18.999
Experiment 1
tdf mean success rate: 7.826
fgf mean success rate: 10.048
Experiment 2
tdf mean success rate: 6.500
fgf mean success rate: 6.100
==============================
