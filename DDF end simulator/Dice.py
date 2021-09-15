import numpy as np
#this is where dice rolls occur
def oDice():
    #this rolls offenseie dice, probabilities seem correct
    BlackDie = [3,3,3,2,2,1]
    Black = BlackDie[np.random.randint(6)]
    
    YellowDie = [0,0,1,2,3,4]
    Yellow = YellowDie[np.random.randint(6)]
    
    WhiteDie = [0,1,2,3,4,5]
    White = WhiteDie[np.random.randint(6)]
    
    return (10 * Black) + Yellow + White
    
    
    
def dDice():
    #this rolls defense dice, probabilities seem correct
    RedDie = [1,1,1,2,2,3]
    Red = RedDie[np.random.randint(6)]
    
    GreenDie = [0,0,0,0,1,2]
    Green = GreenDie[np.random.randint(6)]
    
    return Red + Green

#if __name__ == "__main__":
    # probs = []
    # for i in range(10000):
    #     probs.append(dDice())
        
        
    # x = probs.count(5)
    # y = x/len(probs)
    # print(x,y)