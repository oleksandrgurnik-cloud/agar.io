import random
class Hero:
    def __init__(self,hp,attack,speed,y,x):
        self.hp = hp
        self.damage = attack
        self.speed = speed 
        self.y = y
        self.x = x
    
    def attack(self):
        print("ваш персонаж атакував з рандомним уроном",random.randint(0,self.damage))
hero = Hero(500,21,40,323,233)
hero.attack()
hero.attack()        