#Ravens playcharts as proof of concept
class Ravens:
    def __init__(self):
        self.medium_pass = [56,'DEF5X', 'OFF10',18,20,'B','DEF5',10,19,
                            'INT15','PI13','B',11,12,'B',14,24,'OFF5',25,
                            'QT',"B",'QT',16,'B','B','B',13,17,'B',21]
        self.long_pass = ['DEF15', 'INT29',26,'OFF5','B',44,'B','DEF5','TD','B',
                          29,28,'PI19',21,'QT','B','B','PI30','OFF10',
                          26,'B','B','B','B','B','B','B','B','B',74]
        self.sideline_pass = ['PI16',3,14,19,12,'DEF5X',13,'PI7',20,
                              'DEF5',4,9,'OFF5','B','B','B','B','QT','OFF10',
                              'OFF17',5,11,'B','B','B',8,17,7,6,'OFF10']
        
        self.QT = [-11,14,24,14,-10,2,22,-7,-2,2,'F',3,-8,2,-5,11,1,-3,'F',0,2,'F',
                   -1,0,-7,-4,-6,4,2,6]



class Eagles:
    def __init__(self):
        self.std = [[0,0,'(18)'],[-2,3,0],[0,'B',-4],
                    ['INT22','(39)','B'],['INT20','QT','INT14']]
        self.pass_nickel = [[0,5,0],['B',0,0],[0,-10,'QT'],
                            [20,'B','B'],['INT22','(TD)',7]]
        self.pass_dime = [[0,3,0],['QT','QT','(10)'],[0,'B',-5],
                          ['B','(37)',0],['INT16','QT','B']]
        self.QT_contain = [5,0,-5,0,0]
if __name__ == "__main__":
    ravens1 = Ravens()
    print(len(ravens1.medium_pass))
    print(len(ravens1.long_pass))
    print(len(ravens1.sideline_pass))