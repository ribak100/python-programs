'''
from struct import *

# how computer store data
packed_data = pack("iiif", 45, 34, 1, 424.45)

print(packed_data)

print(calcsize("i"))
print(calcsize("f"))
print(calcsize("iiif"))

# how to get back the original data
original_data = unpack("iiif", packed_data)
print(original_data)
print(unpack("iiif", b'-\x00\x00\x00"\x00\x00\x00\x01\x00\x00\x00\x9a9\xd4C'
))
'''
'''
# a map function that can be used to ......... pls read the code below can't really explain this shit
my_income = [5, 10, 13, 15, 17, 28]

def salary(dollars):
    double_salary = dollars * 2
    return double_salary

print(list(map(salary, my_income)
))

for item in my_income:
    double = item * 2
    print(double)
'''
'''
# finding the largest or smallest item

import heapq

phone = [
    {"phone": "iPhone X ", "price" : 900.41},
    {"phone": "samsung S9", "price"  : 879.43},
    {"phone": "infinix note 6", "price"  : 300.32},
    {"phone": "techno K7", "price"  : 299.24},
    {"phone": "xiaomi MI", "price"  : 134.99},
    {"phone": "nokia M6", "price"  : 144.98},
    {"phone": "LG G4", "price"  : 200.73},
    {"phone": "leagoo M8 pro", "price"  : 122.46},
    {"phone": "sony ericson", "price"  : 243.85},
    {"phone": "motorola", "price"  : 300.27},
    {"phone": "sony", "price"  : 450.13},
    {"phone": "huawei", "price"  : 50.65},
]


print(heapq.nlargest(4, phone , key =lambda phone: phone["price"]))

'''

'''
# finding most frequently occured item

from collections import Counter

cali_post = "Hi guys, I have been a little bit off calisthenics and workouts these days, and that" \
" was because of my schooling and stuffs, so I was pretty busy, but am on holiday now and am back at" \
"home, and I want to get serious with my training and also get motivated. I need you guys help with" \
"that. I felt very rusty when I first did my first workout, so guys I want you to help me out with" \
"my workout plan. I will post the workout i have done so that you guys can analyze it if its good" \
"enough and help me adjust it if it’s not. I will also be posting some short clip to help me" \
"analyze my form. Thanks" 

individual = cali_post.split()
count = Counter(cali_post)

top_ten = count.most_common(10)

print(top_ten)
#print(individual)
'''
'''
# sorting a dictionary to get the first name and last name in an alphabetical order
#this will take 2 arguments, lol

from operator import itemgetter

full_name = [

    {"fname": "Adekanye", "lname": "Ibrahim"},
    {"fname": "Adekanye", "lname": "Abdulkabir"},
    {"fname": "Adekanye", "lname": "Sulaiman"},
    {"fname": "Adeniyi", "lname": "Aramide"},
    {"fname": "Adeniyi", "lname": "Badirat"},
    {"fname": "Adeniyi", "lname": "Bashira"},
    {"fname": "Adeniyi", "lname": "Aisha"},
    {"fname": "olayemi", "lname": "Hanif"}

]

for name in (sorted(full_name , key= itemgetter("fname", "lname"))):
    print(name)

print("---------------------------------------")

for fname in (sorted(full_name , key= itemgetter("fname"))):
    print(name)

'''

from operator import attrgetter



class User:

    def __init__(self, x , y):
        self.name =x
        self.user_id = y


    def __repr__(self):
        return self.name + " : " + str(self.user_id)

    
    
    
users = [

    User("Rasheed", 48),
    User("Ahmed", 35),
    User("Rahman", 72),
    User("Qudir", 13),
    User("Naheem", 34),
    User("Isiak", 76),
    User("Yusasif", 43)
]

for user in users:
    print(user)

print("----------------------------")

for User in sorted(users, key= attrgetter("name")):
    print(User)    

print("----------------------------")

for User in sorted(users, key= attrgetter("user_id")):
    print(User) 







