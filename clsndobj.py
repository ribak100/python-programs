'''
class Enemy:
    
    def __init__(self , x):
        self.life = x


    def attack(self):
        print("ouch nooo ")
        self.life -= 1


    def life_check(self):
        if self.life <= 0:
            print("i am dead")
        else:
            print(str(self.life) + " lives remain" )    

enemy1 = Enemy(4)
enemy2 = Enemy(3)
enemy3 = Enemy(2)
enemy4 = Enemy(2)


enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy2.attack()
enemy2.attack()
enemy2.attack()
enemy3.attack()

enemy1.life_check()
enemy2.life_check()
enemy3.life_check()
enemy4.life_check()




'''
class Human: 
    f = 'famale'
    m = 'male'
    def __init__(self, name):
        self.name = name
      # print(self.name) if i remove this comment it will print the name first as an initial variable


r = Human("rasheedat")
b = Human("bisola")
a = Human("aishat")
q = Human('ridwan')
w = Human('rasheed')



print(r.f)
print(r.name)
print(b.f)
print(b.name)
print(a.f)
print(a.name)
print(q.m)
print(q.name)
print(w.m)
print(w.name)

'''

# inheritance, this program i will inherit my dads surname 

class parent():

    def print_surname(self):
        print("Adekanye")



class child(parent):


    def print_last_name(self):
        print("herdeykhanyhe")

    def print_first_name(self):
        print("Abdulkabir")    


my_name = child()

my_name.print_first_name()
my_name.print_last_name()
my_name.print_surname()
'''





















































