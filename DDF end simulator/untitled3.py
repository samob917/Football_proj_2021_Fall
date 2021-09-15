#su_proj
'''
1000 runs:
0   229   254   246   238    33

2000 runs:
0   478   505   479   480    58
'''

onek_runs = [0, 229,  254,   246,   238,  33]
twok_runs = [0, 478,   505,   479,   480,    58]

print(sum(onek_runs), sum(twok_runs))
threek_total = []
for i in range(len(onek_runs)):
    threek_total.append(onek_runs[i]+twok_runs[i])
    
print(threek_total)

dub_perm = threek_total[1]+threek_total[2]
sing_perm = threek_total[3]+threek_total[4]

print(dub_perm, sing_perm)