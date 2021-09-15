#passing offense
best_off = ["2015 NO", "2015 NYG", "2015 NE",
            "2016 ATL", "2016 SEA", "2016 IND",
            "2017 KC", "2017 LAC", "2017 NE",
            "2018 IND", "2018 ATL", "2018 TB",
            "2019 KC", "2019 DAL", "2019 NO"]

med_off = ["2015 CLE", "2015 MIA", "2015 CIN",
            "2016 DET", "2016 KC", "2016 NYG",
            "2017 SEA", "2017 MIA", "2017 OAK",
            "2018 OAK", "2018 MIN", "2018 NO",
            "2019 CAR", "2019 NYG", "2019 SEA"]

bad_off = ["2015 STL", "2015 TEN", "2015 CAR",
            "2016 PHI", "2016 LAR", "2016 BUF",
            "2017 IND", "2017 TEN", "2017 GB",
            "2018 MIA", "2018 JAX", "2018 SEA",
            "2019 IND", "2019 ARZ", "2019 DEN"]

#passing defense
best_def = ["2015 BAL", "2015 CHI", "2015 DEN",
            "2016 DEN", "2016 HOU", "2016 MIN",
            "2017 MIN", "2017 BAL", "2017 CHI",
            "2018 LAC", "2018 MIN", "2018 JAX",
            "2019 BUF", "2019 NE", "2019 PIT"]

med_def = ["2015 SD", "2015 CAR", "2015 NE",
            "2016 DET", "2016 PHI", "2016 SF",
            "2017 LAR", "2017 MIA", "2017 CLE",
            "2018 GB", "2018 DAL", "2018 CAR",
            "2019 PHI", "2019 ATL", "2019 NYJ"]

bad_def = ["2015 NO", "2015 SF", "2015 NYG",
            "2016 TEN", "2016 OAK", "2016 NYG",
            "2017 NYG", "2017 KC", "2017 GB",
            "2018 NO", "2018 NYJ", "2018 TB",
            "2019 IND", "2019 DET", "2019 MIA"]

"""
Simulator plan:
    1. chose two teams lists (ie bad_off, med_def)
    2. Randomly select 1 element from each list to be the offense and defense
    3. simulate a game scenario between them 
    4. repeat 2 and 3 10,000 times
    

"""