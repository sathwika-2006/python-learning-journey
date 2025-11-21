print("Welcome to the Math Quiz Game!!")
print("Your first question is")
score=0

ans=int(input("What is 9+6?\n "))
if ans==15:
    print("You have got it right!\nHere is your second question")
    score+=1
else:
    print("Oh No! It is 15")


ans2=int(input("What is 12-5? "))
if ans2==7:
    print("Yayyy!Keep going\nHere is your third question")
    score+=1
else:
    print("Sorry! It is 7")


ans3=int(input("What is 7*4?\n"))
if ans3==28:
    print("You are rocking\nHere is your fourth question")
    score+=1
else:
    print("Sorry! It is 28")


ans4=int(input("What is 18/3?\n "))
if ans4==6:
    print("Amazing!!\nHere is your last question")
    score+=1
else:
    print("Sorry! It is 6")


ans5=int(input("What is 5*5+2\n"))
if ans5==27:
    print("Great!!")
    score+=1
else:
    print("Oh No! It is 27")

print("Your Score:",score,"/5")
if score==5:
    print("You go 5 in a row!Great")
if score==4:
    print("Good!!")
if score<=3:
    print("Try again")