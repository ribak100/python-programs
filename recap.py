'''
def naira_dollar(naira):
    amount = naira / 365
    print(amount)


naira_dollar(5000)
'''
'''
def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age

kabir_limit_to_date = allowed_dating_age(23)
print("kabir can date a", kabir_limit_to_date , "girl and older")
'''


'''
my_wallet = "medium"

if my_wallet is "full":
    print("wow men, i need to flex a bit")
elif my_wallet is "medium":
    print("need to manage a bit, and flex a bit")
else:
    print("need more cash lol, wallet is red!")
'''
'''
# slicing string

kabir = "lack of electricity makes me have to retype my programs because of long breaks between learning period "

print(kabir[2:32])
print("The above words are",len(kabir[2:32]),"letters")

#breakfast = [water, banana, orange, bread, egg, milk]
#breakfast[1:3]

'''
'''
import random 
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0EEBt1_IoZlFnDHAIHmgC3LAnh5lxQs6ZdJ9AiDCxU2zTvbS_")    
'''
'''
file_write = open("learning.txt", "w")
file_write.write("i have not been able to progress in my python learning\n")
file_write.write("there are a lot of problems\n")
file_write.write("i am actually going back to retry the codes i've already learned\n")
file_write.write("am forgetting how to write it because of lack of practice\n")
file_write.write("i feel sorry for myself, cause i have a lot to learn\n")
file_write.write("anyways i will try my best and manage my time and resources\n")
file_write.close()


file_read = open("learning.txt", "r")
print_file = file_read.read()
print(print_file)
file_read.close()
'''
grocery_list = ["rice", "beans", "tomatoes", "garri", "spagetti"]
print("what i need to buy for school is", grocery_list)
print("---------------------------------------")
grocery_list.append("gino")
print(grocery_list)
grocery_list.insert(2, "semovita")
grocery_list.sort()
del grocery_list[3]
print("---------------------------------------")
print(grocery_list)
print("---------------------------------------")
print(grocery_list)
print("---------------------------------------")

other_events = ["exercise", "bussiness", "eat", "play tennis"]
todo_list = [other_events + grocery_list]
print(todo_list) 
print(todo_list[0][2]) 















































