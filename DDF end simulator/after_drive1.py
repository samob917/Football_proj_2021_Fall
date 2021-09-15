import pandas as pd

win_down_td = pd.read_csv("down_by_td15_sec.csv") #strat 1
win_down_fg = pd.read_csv("down_by_fg15_sec.csv") #strat 0
def prob_of_winning(time_left, strategy):
    if strategy == 0:
        time_buckets = win_down_fg["time1"]
        for time in time_buckets:
            if time_left > time and time_left <= time+15:
                get_prob = win_down_fg[win_down_fg["time1"] == time]
                prob = get_prob["prob_of_winning"].item()
                return prob
    elif strategy == 1:
        time_buckets = win_down_td["time1"]
        for time in time_buckets:
            if time_left > time and time_left <= time+15:
                get_prob = win_down_td[win_down_td["time1"] == time]
                prob = get_prob["prob_of_winning"].item()
                return prob
            
            
#print(prob_of_winning(35, 1))