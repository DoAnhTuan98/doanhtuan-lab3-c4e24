from random import randint, choice
from calc import evaluate

#1.sinh bieu thuc
x= randint(0,9)
y= randint(0,9)
pt = choice(["+","-","*","/"])
error = randint(-1,1)


r = evaluate(x,y,pt) + error

print(f"{x} {pt} {y} = {r}")




user_answer  =input("(Y?N)?").upper()

if user_answer == "Y":
    if error == 0:
        print("yay")
    elif error != 0: # co the dung ham else luon
        print("wrong")
elif user_answer == "N":
    if error == 0:
        print("wrong")
    elif error != 0:
        print("yay")



    
