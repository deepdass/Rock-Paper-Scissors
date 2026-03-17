##rock,paper,scissor
import random
p = None
comp= 0
pla = 0
while True:
     x = "rock"
     y = "paper"
     z ="scissor"
     a = ["rock","paper","scissor"]
     c = random.choice(a)

     b = None
     while b not in a:
         b = input("Rock,Paper or Scissor: ").lower()
     print("Computer Choose ",c )

     if b == c:
        print("Draw")
        
     if c == z and b == y:
        print("Computer win")
        comp+=1
     if c == y and b == x:
        print("Computer win")
        comp+=1
     if c ==x and b == z:
        print("Computer win")
        comp+=1


     if c == y and b == z:
        print("Player win")
        pla+=1
     if c == x and b == y:
        print("Player win")
        pla+=1
     if c ==z and b==x:
        print("Player win")
        pla+=1

     print("\nComputer:",comp,"| Player :",pla)
     p = input("Want To Retry:\nyes or no(Y/N) ").lower()
     print("********************************************")
     if p == "n" or p=="no":
         break
     else:
         pass
        
     
