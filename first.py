
'''
# basic addition and print in pyhton
x = 9+5
r= 3 + 3 + 3 
print("hello world")
print(x)

# an if else statement of checking age to see maybe you can drink coke or not
age = 30
if age < 21:
    print("no drink for you boy :p")
elif age >= 22:
    print("you can have some drink")


'''
'''
# an if elif and else statement to check your religion and give you a compliment :)
religion = "islam"
if religion  is "islam":
    print("baraka llahu feqh") 
elif religion is "christianity":
    print("my brother go and make your self pure ")
elif religion is "traditional":
     print("ariwooya")
else:
     print("wow do you mean you dont have a religion, boy thats pretty bad")


'''
'''
# a list of food, printing it on screen and also writing the lenght of each value
food = ['rice','beans','garri','spagetti','yam']
for f in food[2:]:
    print(f)
    print(len(f))


# a for loop for number in range 2 to 10 with 2 increment value 
for number in range(2,10,2):
    print(number)

# a while loop to print out the value of buttcrack as long as it is less than or equal to 15
buttcrack = 5
while buttcrack <= 15:
    print(buttcrack)
    buttcrack += 1



''' #this is a simple programming loop to find the magic number and print it out


magicNumber = 30
for n in range(100):
    if n is magicNumber:
        print(n, "is the magic number")
        break
    else:
        print(n)    



