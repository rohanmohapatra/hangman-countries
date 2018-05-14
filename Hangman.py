from random import randrange
def checksingle(ltr):
    if len(ltr)==1:
        return True

from printcheck import *
from check import *


print("Welcome to Hangman v1.0".rjust(50))
print("COUNTRIES".rjust(43))
choice=input("\nDo you want to play(y/n)")
words=['Australia','India','Pakistan','England','Wales','Bangladesh','South Africa','Afghanistan','United Arab Emirates','Indonesia','Malaysia','Singapore','Canada',
       'Kenya','Nepal','Maldives','Brazil','Argentina','Germany','Portugal','Spain','Netherlands','Italy','Ireland','Iceland','Greece','Sri Lanka',
       'Zimbabwe','France','New Zealand','Bangladesh','Russia','Iraq','United States of America','Belgium','Azerbaijan','China','Japan']
if choice=='y':
    s=words[randrange(0,len(words))]
    s=s.casefold()
    guessword=[]
    slist=list(s)
    for sl in slist:
     if sl.isspace():
         guessword.append(' ')
     else:
         guessword.append('_')
    print("The No of Blanks:")
    for ele in guessword:
        
        print(ele,end=' ')
    
    turns=5
    while turns>0:
        
        guess=input("\nEnter a letter to guess:")
        if checksingle(guess):
            if check(s,guess):
                a=printcheck(s,guess,guessword)
                if a==slist:
                    break
                
            else:
                print("Wrong Guess!Number of turns left:",turns-1)
                turns-=1
        else:
            print("Please enter one character only")
    if turns==0:
        print("\n\n\t\t\tGame Over!")
        print("\n\t\t   Better Luck Next time")
    else:
        finalans=''
        for fl in slist:
            finalans+=fl
        print("\n\n\t\t\tThe Correct Word is :",finalans.upper())
        print("\n\n\t\t\tYour Guess is Right Congratulations!!\n")
        print("\t\t\t\tThank you For playing")
elif choice=='n':
    print("\t\t\tThe Game has been terminated!")
else:
    print("Wrong choice given!!The Game is terminated")
