from src import createData, readData, removeData, setData
import os
import time
import random

#createData.createData("data")

local = os.path.exists("cache/data/python/data.txt")



setData.setData(f"cache/data/python/data", "points: load", "w")

#createData.createData("points")

with open("cache/data/points.txt") as fl:
    pol = fl.read()

pol2 = int(pol)

points = pol2

pointsStr = str(points)

setData.setData("cache/data/points", pointsStr or "0", "w")

pointsStr = str(points)

setData.setData(f"cache/data/points", f"{pointsStr}", "w")

with open("cache/data/wins.txt") as up:
    tr = up.read()
tr2 = int(tr)

with open("cache/data/coins.txt") as co:
    rt = co.read()
rt2 = int(rt)

shopFolder = ("cache/data/shop")

coins = rt2
coinsStr = str(rt2)
wins = tr2
winsStr = str(wins)
if wins == 0:
      X = ["yes", "+1", "+1", "+1", "-1", "+5"]
      de = random.choice(X)
if wins >= 1:
      X = ["yes", "+1", "+1", "+1", "+1", "-1", "-1", "+5", "+5"]      
      de = random.choice(X)      

menuGUI = '''
----------------WELCOME----------------
1. Play
2. Shop
3. Stats
4. Restart Stats
5. Info
0. Exit
THE GAME CONTAIN ERRORS AND BUGS (Beta Phase)
---------------------------------------
'''

shopGUI = '''
-----------------SHOP------------------
The shop is not avaliable
---------------------------------------
'''

statsGUI = f'''
-----------------STATS-----------------
Wins: {winsStr}
Coins: {coinsStr}
---------------------------------------
'''

infoGui = '''
-----------------INFO------------------
Name: "Points collecter"
Version: 0.1.9 [BETA PHASE]
Dev: Thiago Stilo (Stilo.tvl)
Dev lang: Python, TXT
---------------------------------------
'''

menuDisplay = print(menuGUI) 
menu = input("Input: ")
if menu == "2":
    print(shopGUI)
    exit()
else:
    if menu == "3":
         print(statsGUI)    
         exit()
    else: 
         if menu == "4":
             resstats = input("Are you sure? Your wins and coins will be reset to 0 and your points will be 1 S/N: ")
             if resstats == "S":
                 setData.setData("cache/data/wins", "0", "w")
                 setData.setData("cache/data/points", "1", "w")
                 setData.setData("cache/data/coins", "0", "w")
                 points = 1
                 pointsStr = str(points)
                 print("Restored...")
                 exit()

             else: 
                 if resstats == "N":
                     exit()
                 else: 
                    print("The option not found, stats were not restored")    
                    exit()


         else:
            if menu == "0":
                 exit()     
            else:
                if menu == "5":
                    print(infoGui)
                    exit()
                else:    
                   if not menu == "1":
                     print("The option was not found")
                     exit()
                         



if de == "+1":
    points = points + 1
    pointsStr = str(points)
    print(f"+1\nPoints: {pointsStr}")

if de == "+5":
    points = points + 5
    pointsStr = str(points)
    print(f"+5\nPoints: {pointsStr}")

if de == "yes":
    points = points - 5
    pointsStr = str(points)
    print(f"-5\nPoints: {pointsStr}")

if de == "-1":
    points = points - 1
    pointsStr = str(points)
    print(f"-1\nPoints: {pointsStr}")

setData.setData("cache/data/points", f"{pointsStr}", "w")

if points <= 0:
    print("Game Over!")
    points = 1
    pointsStr = str(points)

if points >= 20 and wins == 0:
    print("You Win! +1 Win +5 Coins")
    points = 1
    pointsStr = str(points)    
    wins = wins + 1
    winsStr = str(wins) 
    coins = coins + 5
    coinsStr = str(coins)
    setData.setData("cache/data/wins", f"{winsStr}", "w")
    setData.setData("cache/data/coins", f"{coinsStr}", "w")

if points >= 30 and wins >= 1:
    print("You Win! +1 Win +5 Coins")
    points = 1
    pointsStr = str(points)    
    wins = wins + 1
    winsStr = str(wins) 
    coins = coins + 5
    coinsStr = str(coins)
    setData.setData("cache/data/wins", f"{winsStr}", "w")
    setData.setData("cache/data/coins", f"{coinsStr}", "w")

setData.setData("cache/data/points", f"{pointsStr}", "w")
