import random
import os
def roll():
    return random.randint(1,6) #generates a value between 1 to 6
def chance(n,s,p): # n is target value,,, s is score of a person ,, p is name of person
    input(f"{p} enter to roll")
    dice=roll()  # value between 1 to 6 obtained
    print(f"{p} you rolled value ",dice)
    diff=n-s   #difference of target and score used to roll the dice until perfect target score is achived
    if(dice<=diff):  # the score should not exceed the given target
        s=s+dice
    else:
        #if our dice value obtained exceeds the targe, then again roll for a value that adds to exact target value
        print(f"{p} your entered value is more than target.. please roll for a lesser value")
    return s,p

n=10
p1=input("enter first player name :")
p2= input("enter second player name :")
#initialize scores to 0
score1=0
score2=0
p=True

while(p):
    score1,person=chance(n,score1,p1) #obtains score of player 1 after each round
    if(score1==n): #if score matches the targe, then loop breaks and winner will be announced
        break
    print(f" {person} score is : ", score1)
    score2,person2=chance(n,score2,p2)  #obtains scores of player 2 after each round
    if (score2 == n):
        break
    print(f"{person2} score is : ", score2)
    input("enter to go to next round play again ")
    # os.system('cls') will clear the console for every round
    # clearing console only in command prompt but not in pycharm console.
    os.system('cls')

print(f"final scores are {score1} : {score2} ")
if(score2>score1):
    print(f"{p2} you won the match")
else:
    print(f"{p1} you won the match")
