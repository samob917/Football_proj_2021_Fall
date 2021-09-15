'''
Game state class
'''
import Dice as dice
import simulator_with_charts as sim

class game:
    
    def __init__(self, score1, score2, time_left, to1, to2, possession,
                 ball_on, down, dist_to_first):
        
        self.score1 = score1 #losing team score
        self.score2 = score2
        self.time_left = time_left
        self.to1 = to1
        self.to2 = to2
        self.possession = possession
        self.ball_on = ball_on
        self.down = down
        self.dist_to_first = dist_to_first
        
        '''
        This function should update all necessary variables after a given play
        'outcome' will return the outcome of the play
        an example is a number 'x' which changes ball_on, and down if necessary
        a change of possession is another option
        
        '''
    def update_game(self,oResult,dResult,oYards,dYards,off_chart):
        if oYards == '5X' or dYards == '5X':
            if oYards == '5X':
                oYards = 5
            if dYards == '5X':
                dYards = 5
        
        oResult = int(oResult)
        dResult = int(dResult)
        oYards = int(oYards)
        dYards = int(dYards)
        
        #offsetting: 5/6, 6/5, 
        if (oResult == 6 or oResult == 8 or
            oResult == 25 or oResult == 26) and (dResult == 7 or
                                                 dResult == 21):
            print("offsetting penalties")
            pass
        
        elif (dResult == 6 or dResult == 8 or
            dResult == 25 or dResult == 26) and (oResult == 7 or
                                                 oResult == 21):
            print("offsetting penalties")
            pass
        
        elif (dResult == 6 or dResult == 8 or
            dResult == 25 or dResult == 26):
            if dResult != 6:
                self.dist_to_first = 10
                self.ball_on -= dYards
                self.down = 1
                
            else:
                self.dist_to_first -= dYards
                self.ball_on -= dYards
            
            print("defensive penalty, {} yards".format(dYards))
                
        elif (oResult == 6 or oResult == 8 or
            oResult == 25 or oResult == 26):
            if oResult != 6:
                self.dist_to_first = 10
                self.ball_on -= oYards
                self.down = 1
            else:
                self.dist_to_first -= oYards
                self.ball_on -= oYards
                
            print("defensive penalty, {} yards".format(oYards))
            
        elif (oResult == 7 or oResult == 21):
            if oResult == 21:
                self.down += 1
                self.ball_on += oYards
                self.dist_to_first += oYards
            else:
                self.ball_on += oYards
                self.dist_to_first += oYards
            
            print("offensive penalty, {} yards".format(oYards))
        elif (dResult == 7 or dResult == 21):
            if dResult == 21:
                self.down += 1
                self.ball_on += dYards
                self.dist_to_first += dYards
            else:
                self.ball_on += dYards
                self.dist_to_first += dYards
            print("offensive penatly, {} yards".format(dYards))
        
        
        elif dResult == 1 and oResult == 1:
            #add the results
            self.ball_on -= (oYards + dYards)
            if self.dist_to_first <= (oYards + dYards):
                self.down = 1
                if self.ball_on <= 10:
                    self.dist_to_first = self.ball_on
                else:
                    self.dist_to_first = 10
            else:
                self.down += 1
                self.dist_to_first -= (oYards + dYards)
            print("play goes for {} yards".format(oYards + dYards))
            pass
        elif dResult == 4 and (oResult != 9 and oResult != 5):
            #incomplete pass
            self.down += 1
            print("incomplete pass")
            pass
        elif dResult == 9 :
            #change possession - interception
            self.possession = not self.possession
            print("incomplete pass")
            pass
        elif dResult == 5:
            print("fumble")
            #FUMBLE
            #roll oDice
            rec = sim.off_play(off_chart,72)[0]
            if rec == 13:
                self.possession = not self.possession
                print('lost possession')
            else:
                self.ball_on -= dYards
                if self.dist_to_first <= (dYards):
                    self.down = 1
                else:
                    self.down += 1
                    self.dist_to_first -= dYards
                print("recovered by offense for {} yards".format(dYards))
            pass
    
        elif dResult == 14 and (oResult != 9 and oResult != 5):
            print("play goes for {} yards".format(dYards))
            #add yardage based only on defense
            self.ball_on -= dYards
            if self.dist_to_first <= (dYards):
                self.down = 1
            else:
                self.dist_to_first -= dYards
                self.down += 1
            pass
        ##########NEED TO COMPLETE########
        elif dResult == 16 and (oResult != 9 and oResult != 5):
            print("touchdown")
            #TD
            self.score1 += 7
            self.possession = not self.possession
            #work on change of possession mechanism
            pass
        elif dResult == 3 and (oResult != 9 and oResult != 5):
            print("QB Trapped")
            #check QT chart
            #roll die on QT chart
            play = sim.off_play(off_chart,71)
            oResult = play[0]
            oYards = play[1]
            self.update_game(oResult, 1, oYards, 0, off_chart)
            print("goes for {} yards".format(oYards))
            pass
    
        elif oResult == 2:
            print("touchdown")
            #TD 
            self.score1 += 7
            self.posession = not self.possession
            pass
        elif oResult == 3:
            print("QB Trapped")
            #check QT chart
            #roll die on QT chart
            play = sim.off_play(off_chart,71)
            oResult = play[0]
            oYards = play[1]
            self.update_game(oResult, 1, oYards, 0, off_chart)
            print("goes for {} yards".format(oYards))
            pass
        elif oResult == 4:
            #incomplete pass
            self.down += 1
            print("incomplete")
            
            pass
        elif oResult == 10 and dResult == 1:
            #check bold chart- update oYards
            play = sim.off_play(off_chart,70)
            oResult = play[0]
            oYards = play[1]
            self.update_game(oResult, 1, oYards, 0, off_chart)
            print("play goes for {} yards".format(oYards))
            pass
        elif oResult == 9 and (dResult == 1 or dResult == 3 or dResult == 4):
            #interception
            print("interception")
            self.possession = not self.possession
            pass
        elif oResult == 5 and (dResult == 1 or dResult == 3 or dResult == 4):
            #fumble - check fumble chart
            print("fumble")
            rec = sim.off_play(off_chart,72)[0]
            if rec == 13:
                self.possession = not self.possession
                print("lost fumble")
            else:
                print("recovered by offense")
                self.ball_on -= dYards
                if self.dist_to_first <= (dYards):
                    self.down = 1
                else:
                    self.down += 1
                    self.dist_to_first -= dYards
            pass
        elif oResult == 9 and (dResult == 16 or (dResult == 14 and dYards > 0)):
            print("incomplete")
            self.down += 1
            pass
        elif oResult == 5 and (dResult == 14 or dResult == 16):
            #fumble-check chart
            print("fumble")
            rec = sim.off_play(off_chart,72)[0]
            if rec == 13:
                self.possession = not self.possession
                print("lost possession")
            else:
                print('recovered by offense')
                self.ball_on -= dYards
                if self.dist_to_first <= (dYards):
                    self.down = 1
                else:
                    self.down += 1
                    self.dist_to_first -= dYards
            pass
        elif oResult == 9 and (dResult == 14 and dYards < 0 ): 
            #interception
            print("interception")
            self.possession = not self.possession
            pass
        else:
            print('PLAY COMBINATION NOT ACCOUNTED FOR')
        
        
    def update_time(self, off_UPCID, oResult, dResult):
        if (oResult in [6,7,8,21,25,26]) or (dResult in [6,7,8,21,25,26]):
            self.time_left -= 2
        elif int(off_UPCID) in [1,2,3,4]:
            self.time_left -= 7
        elif int(off_UPCID) in [5,6,7,8]:
            self.time_left -= 9
        elif int(off_UPCID) == 9:
            self.time_left -=8
            
    
    
        