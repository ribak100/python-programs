''' this is for testing a multiple inheritance 
    i want to create an imaginary deadpool game 
    so guys follow along :)
'''
# Deadpool fighting
class Deadpool_Shoot():
    
    def pistol(self):
        print("how many bullets in your head so far")

    def ak47(self):
        print("brak braak braaaak,", "i aim because i care")

    def shotgun(self):
        print("if that hit you in the groin am sorry", "was actually aiming for your chest")

    def elect_gun(self):
        print("you are a lucky dude,", "that should rip most people head off")

class Deadpool_strike():

    def sword(self):
        print("shrin ! ", "men don't know you have this much blood in your head")

    def dagger(self):
        print("hey player, could you buy anything that might hit.... harder ")

    def hammer(self):
        print("deadpool smash!, deadpool smash!!, deadpool smaaaash!!!!")


class Deadpool_throw():

    def grenade(self):
        print("boooooooom,", "when i said blow me this was not what i meant ")

    def shine(self):
        print("don't tell me you can still move with these in your eyes")

    def hold_trap(self):
        print("this should suck the life outtaya")

    def flat_bomb(self):
        print("booooooom, i can say chimmi changa in seven languages :)")

class Deadpool_fight(Deadpool_Shoot, Deadpool_strike, Deadpool_throw):
    pass

# Deadpool movement class list 

#1 Deadpool walk

class Deadpool_walk():
    def forward(self):
        print("i am now moving forward")
    def backward(self):
        print("i am now moving backward")
    def left(self):
        print("will you shut up, trying to move to the right here, i mean left sowri")
    def right(self):
        print("am now going right, right!")

#2 Deadpool jump
    
class Deadpool_jump():

    def jump(self):
        print("i am now in the sky")
    
    def double_jump(self):
        print("i am now flying")

#3 Deadpool teleport

class Deadpool_teleport():    
    def teleport(self):
        print("hey am behind ya")

    def teleport_long(self):
        print("my handy dandy teleportation saved my ass")


class Deadpool_movement(Deadpool_walk, Deadpool_jump, Deadpool_teleport):
    pass

attack = Deadpool_fight()
moving = Deadpool_movement()


# attacking with gun

attack.pistol()
attack.ak47()
attack.shotgun()
attack.elect_gun()

# attacking with sword

attack.sword()
attack.dagger()
attack.hammer()

# attacking with throwing weapon

attack.grenade()
attack.shine()
attack.hold_trap()
attack.flat_bomb()

# moving 

moving.forward()
moving.backward()
moving.left()
moving.right()

#jumping

moving.jump()
moving.double_jump()

#teleport

moving.teleport()
moving.teleport_long()

















