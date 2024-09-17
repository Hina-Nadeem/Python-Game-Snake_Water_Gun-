import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([1,-1,0])
you_str=input("Enter your Choice : ")
print("******************")
youdict={"s":1,"w":-1,"g":0}
reverse_dict={1:"Snake",-1:"Water",0:"Gun"}
you=youdict[you_str]
print(f"You choose :{reverse_dict[you]}\nComputer choose :{reverse_dict[computer]}")
if(computer==you):
    print("It's a draw")
else:
    if(computer==-1 and you==1 ):
        print("You Win!Congratulations")    
    elif(computer==-1 and you==0 ):
        print("You lose!Try again")    
    elif(computer==1 and you==-1 ):
        print("You lose!Try again")    
    elif(computer==1 and you==0 ):
        print("You Win!Congratulations")    
    elif(computer==0 and you==-1 ):
        print("You Win!Congratulations")    
    elif(computer==0 and you==1 ):
        print("You lose!Try again") 
    else:
        print("Something Went Wrong! Try Again")       