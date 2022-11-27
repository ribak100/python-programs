''' This is a dictionary
i will make another one below that will give the min,max,sorted values
follow along
'''
coursemate = {'paul': ' a tennis player', 'rotdung': ' likes to read at environmental', 'malik': ' we went to the same secondary school'}
print(coursemate)
print(coursemate['paul'])

for k, v in coursemate.items():
    print(k + ":")
    print(v)

# a flexible dictionary that can be sorted

phone = {
    "iPhone X " : 900.41,
    "samsung S9" : 879.43,
    "infinix note 6" : 300.32,
    "techno K7" : 120.24,
    "xiaomi MI" : 134.33,

}

print(sorted(zip(phone.keys(), phone.values())))
print(min(zip(phone.keys(), phone.values())))
print(max(zip(phone.keys(), phone.values())))
print(min(zip(phone.values(), phone.keys())))




import functions

functions.naira_to_dollar(500000)

import random

x = random.randrange(1, 1000)
print(x)



   