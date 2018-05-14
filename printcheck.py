def printcheck(word,ltr,guessword):

 locword=list(word)
 
 for x in range(len(locword)):
     if ltr.isalpha():
         
         if ltr==locword[x]:
             guessword[x]=ltr
     
 c=locword.count(ltr)
 for ele in guessword:
     print(ele,end=' ')
 print("\nThe letter occurs ",c,"times")
 return guessword



 



