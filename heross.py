from abc import ABC,abstractmethod
import os
import time
import random
class Cheracter(ABC):
    @abstractmethod
    def move():
        pass
    @abstractmethod
    def teleport():
        pass


class Hero(Cheracter):
    def __init__(self,age,name):
        self.x = 0
        self.y = 0
        self.age = age
        self.name = name
        self.hp = 100
        self.atack = 7
        self.image = "w"

    def move(self,direction):
        prev_x,prev_y = self.x,self.y
        self.x += direction[0]
        self.y += direction[1]
        return prev_x,prev_y
    
    def teleport(self,newCords):
        self.x = newCords[0]
        self.y = newCords[1]   
        print("персонаж перемістився на кординати",self.x,self.y)
    
class Game:
    def __init__(self):
        self.fild = [["_" for a in range(12)] for a in range(12)]
        self.players = []
        self.main_player = Hero(19,"aleksus")
        enemy = Hero(21,"tronos")
        enemy.y = random
        enemy.x

        self.players.append(enemy)
    def draw(self):
        os.system("cls")
        for g in self.fild:
            print(g)
    
    
    def update(self,old_x,old_y,player):
        self.fild[old_y][old_x] = "_"
        self.fild[player.y][player.x] = player.image
        


    def control(self):
        ward = input("w/a/s/d")
        if ward == 'd':
            prev_x,prev_y = self.main_player.move((1,0))
        if ward == 'w':
            prev_x,prev_y = self.main_player.move((0,-1)) 
        if ward == 'a':
            prev_x,prev_y = self.main_player.move((-1,0))
        if ward == 's':
            prev_x,prev_y = self.main_player.move((0,1))
        self.update(prev_x,prev_y,self.main_player)
    
    def main_loop(self):
        while True:
            self.draw()
            self.control()

Game().main_loop()
