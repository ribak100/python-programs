# a simple function of subjects and printing each 
def subjects():
    print("Mat121")
    print("Phy126")
    print("Sta127")
    print("Imt123")

subjects()

#a simple function that converts naira to dollar
def naira_to_dollar(naira):
    amount = naira / 367
    print(amount)    

#a simple funtion that convert bitcoin to dollar
def bitcoin_to_dollar(bitcoin):
    amount= bitcoin * 6475.22
    print(amount)

#a simple funtion that convert bitcoin to naira. cool isn't it 

def bitcoin_to_naira(bitcoin):
    amount = bitcoin * 2331079.2
    print(amount)

def dollar_to_naira(dollar):
    amount= dollar * 367
    print(amount)    


naira_to_dollar(10000)
dollar_to_naira(99)
bitcoin_to_dollar(4)
bitcoin_to_naira(4)


#the return function, and how to call it as a variable
#this program calculates the age of the girls you can date, i will soon write the one for girls

def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age

abdulkabir_limit_to_date = allowed_dating_age(24)
lado_limit_to_date = allowed_dating_age(30)
print("abdulkabir can date a girl of" , abdulkabir_limit_to_date , "or older")
print("lado can date a girl of" , lado_limit_to_date , "or older")
print(allowed_dating_age(40))

'''default argument
   it sets the default sex as undefined
'''
def get_gender(sex="undefined"):
    if sex is "m":
        sex = "male"
    elif sex is "f":
        sex = "female"
    print(sex)

get_gender("m")
get_gender("f")
get_gender()



# key word argument

def cool_stuff(sport="calisthenics" , course="cyber security" , proglang="python" , goals="white hat"):   
    print(sport , course , proglang , goals  )

cool_stuff()
cool_stuff("gymnastics" , "web hacking" , "java" , "workout" )
cool_stuff("java" , "workout" )
cool_stuff(course= "java" ,sport= "workout" )


# flexible arguments to add numbers that is unlimited
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)  

add_numbers(2,3,4,1)      


# some little program about set 

food_stuffs = {"rice", "beanse", "potato", "spagetti", "semovita"}
print(food_stuffs)
if "rice" in food_stuffs:
    print("you already have rice")
else:
    print("dude you need to buy rice")    
if "garrri" in food_stuffs:
    print("you have garri, thats good")
else:
    print("what the fu*k, dont you know that garri is first aid, you gotta buy it")        



















