import time as time
import players as p
import teams as t
import leagues as l 
import match as m


print('Welcome to my League Simulator\n  Please enter the league you would like to simulate-')
n=0
while n not in ['1','2','3','4']:    
    print("""
    1 - La Liga
    2 - Premier League
    3 - Bundesliga
    4 - Seria A""")
    n=input()
    if n not in ['1','2','3','4']:
        print('Enter a Valid input')
pl=l.League(int(n))
# print(pl.showPlayers)
# print(pl.showStandings)

input()
# while s not in ['1','2','3','4','5','6','7','8','9','10','11','12']:

pl.simLeague()
