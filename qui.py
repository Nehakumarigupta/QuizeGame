# Rock Vs paper -> paper wins
# Rock Vs Scissor -> Rock wins
# Rock Vs Scissor -> Scissor wins
import random
l=["Rock","Scissor","paper"]
'''
Rock Vs paper -> paper wins
Rock Vs Scissor -> Rock wins
Rock Vs Scissor -> Scissor wins
'''
while True:
    Uc=int(input(''' 
    Game start-----
    1 yes
    2 Not Exist
    '''))
    if Uc==1:
        for a in range(1,6):
            user_input=int(input('''
            1 Rock
            2 Scissor
            3 paper
            '''))
    if user_input==1:
        Uchoice="Rock"
    elif user_input==2:
        Uchoice="Scissor"
    elif user_input==3:
        Uchoice="psper" 
    Cchoice=random.choice(l)
    print("Uchoice")
    print("Cchoice") 
    if Cchoice==Uchoice:
        print("Game Draw")
        print("computer value",Cchoice)
        print("user_value",Uchoice)
        Ucount=Ucount+1
        Ccount=Ccount+1
    elif(Uchoice=="Rock" and Cchoice=="Scissor")or(Uchoice=="paper" and Cchoice=="Rock")or(Uchoice=="Scissor" and Cchoice=="paper"):
        print("computer value",Cchoice)
        print("user_value",Uchoice)
        print("you win")
        Ucount=Ucount+1
    else:
        print("computer value",Cchoice)
        print("user_value",Uchoice)
        print("computer wins")  
    if Ucount==count:
        print("Final Game Draw...")
        print("user_score",Ucount)
        print("computer score",Ccount)
    elif Ucount>Ccount:
        print("Final you wins the Game...")
        print("Final computer win the Game...")
        print("user_score",Ucount)
        print("computer score",Ccount)
    else:
        break


