import random
print("ENTER GUYS NAME :-")
guName = input()
print("ENTER GIRLS NAME :-")
giName = input()
n = random.randint(0,100)
print(guName+" your love percentage if you marry "+giName+" is ", n, "%")
if n == 0:
    print("Paran ran pan pan")
elif n <= 10:

    print("Your village people is close by")
elif n <=20:

    print("Baba, go find another partner")
elif n <=30:
    print("Daily routine = fighting")
    
elif n <=40:
    
       print("Dating = True, Marriage = False")
    
elif n <=50:
    print("hmmm, una fit last few years")
    
elif n <=60:
        print("You tried, but i still cant support this marriage")
elif n <=70:
    
        print("hmmm, not bad not bad")
    
elif n <=80:
    
        print("You guys are pretty compatible") 
elif n <90:
    
        print("Am waiting to hear the word MARRIAGE")

elif n < 100:
    
        print("When are we starting the wedding preparation") 
elif n == 100:

        print("What God have joined together")

