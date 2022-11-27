# an instant variable
'''
class sport:

    def __init__(self):
        print("i play lawn tennis")

    def others(self):
        print("i also do calisthenics")

    def others2(self):
        print("i do train basketball, gymnanstics and yoga somtimes")       



sport1 = sport()

sport1.others()
'''
'''
# class with instant variable 
class Enemy_energy:
    

    def __init__(self, x):
        self.energy = x 
       

   
 
    def get_energy(self):
        z = "Energy left"
        print(self.energy,":", z)

    

    

class Enemy_magic:
    def __init__(self, y):
         self.magic = y

    def get_magic(self):
        m = "magic left"
        print(self.magic, ":", m)








enemy_gun1_energy = Enemy_energy(5)
enemy_gun1_magic = Enemy_magic(5)
enemy_gun2_energy = Enemy_energy(6)
enemy_gun2_magic = Enemy_magic(7)

enemy_sword1_energy = Enemy_energy(10)
enemy_sword1_magic = Enemy_magic(13)
enemy_sword2_energy = Enemy_energy(12)
enemy_sword2_magic = Enemy_magic(15)

boss_energy = Enemy_energy(40)
boss_magic = Enemy_magic(100)


enemy_gun1_energy()
enemy_gun1_magic()
enemy_gun2_energy()
enemy_gun2_magic()
enemy_sword1_energy()
enemy_sword1_magic()
enemy_sword2_energy()
enemy_sword2_magic()

boss_energy()
boss()




'''
