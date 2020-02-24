#MatchAnalysis.txt
from random import random
def printInfo():
    print("这是一个关于运动员能力值程序")
    print("通过两运动员的能力值来模拟比赛，看看他们输赢的概率。")
def inputInfo():
    a = eval(input("请输入选手A的能力值："))
    b = eval(input("请输入选手B的能力值:"))
    n = eval(input("请输入比赛场次"))
    return a,b,n
def printSummary(winsA,winsB):
    n=winsA+winsB 
    print("共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))
def simNgames(n,proA,proB):
    winsA,winsB =0,0
    for i in range(n):
        scoreA,scoreB = oneGame(proA,proB)
        if scoreA>scoreB:
            winsA +=1
        else:
            winsB +=1
    return winsA,winsB
def oneGame(proA,proB):
    scoreA = 0
    scoreB = 0
    serving = 'A'
    while not gameOver(scoreA,scoreB):
        if serving =='A':
            if random() < proA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() <proB:
                scoreB +=1
            else:
                serving = 'A'
    return scoreA,scoreB
def gameOver(a,b):
    return a==15 or b==15
def main():
    printInfo()
    proA,proB,n=inputInfo()
    winsA,winsB = simNgames(n,proA,proB)
    printSummary(winsA,winsB)
main()
    
    
    
    
