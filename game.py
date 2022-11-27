

# finding the largest or smallest item
'''
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



import heapq

green_life = [
    {"royal tea": 4200 , "point" : 15.0},
    {"black tea": 1800 , "point"  : 5},
    {"detoxin": 5000 , "point"  : 15},
    {"ash cold": 6200 , "point"  :17},
   
]


print(heapq.nsmallest(4, green_life , key =lambda green_life: green_life["point"]),(heapq.nlargest(4, green_life , key =lambda green_life: green_life["point"])))

'''
'''
from operator import attrgetter



class User:

    def __init__(self, x , y):
        self.point =x
        self.price = y


    def __repr__(self):
        return self.point + " : " + str(self.price)

    
    
    
product = [

    User("Rasheed", 48),
    User("Ahmed", 35),
    User("Rahman", 72),
    User("Qudir", 13),
    User("Naheem", 34),
    User("Isiak", 76),
    User("Yusasif", 43)
]

point = [

    User("Rasheed", 48),
    User("Ahmed", 35),
    User("Rahman", 72),
    User("Qudir", 13),
    User("Naheem", 34),
    User("Isiak", 76),
    User("Yusasif", 43)
]



def print_list(self):
    for Userp in sorted(product, key= attrgetter("point") ):   
        return Userp    


    for Usert in sorted(point, key= attrgetter("price") ):
        return Usert

    print(Userp, Usert)

print_list(user)

'''
'''
console= [
    {"Xbox 360 price": 400 , "game_disc" : 15},
    {"ps3 price": 400 , "game_disc"  : 20},
    {"ps4 price": 505 , "game_disc"  : 15},
    {"Xbox 1 price": 490 , "game_disc"  :30},
   
]




def my_max_by_weight(sequence):
    if not sequence:
        raise ValueError("empty sequence")

    
    maximum = sequence[0]
    for item in sequence:
        #compare element by their weight stored
        #in thier second element
        if item[1] > maximum[1]:
            maximum = item
        
    return maximum


my_max_by_weight(green_life)









