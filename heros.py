WIDTH = 1920
HEIGHT = 1080
import pygame
import math
import random


class Entity:

    def check_colide(self, other):
        distance = math.sqrt((self.pos[0]- other.pos[0])**2 + (self.pos[1]- other.pos[1])**2)
        if distance < self.size-2:
            if isinstance(other, Food):

                self.size += 2
                return False
            if isinstance(other, Vorog):
                if self.size > other.size:
                    self.size += other.size
                    return 'ми зїли'
                elif self.size <other.size:
                    other.size += self.size
                    return 'нас зїли'
                else:
                    return 'не доторкаємося'
        return True

class Main_hero(Entity):
    def __init__(self, screen):
        self.pos = [WIDTH // 2, HEIGHT // 2]
        self.speed = 1
        self.size = 25
        self.color = (100,0,180)
        self.screen = screen

    def live(self,keys):
        if keys[pygame.K_w]:
            self.pos[1] -= 10
        if keys[pygame.K_a]:
            self.pos[0] -= 10 
        if keys[pygame.K_s]:
            self.pos[1] += 10  
        if keys[pygame.K_d]:
            self.pos[0] += 10
    
    
    def draw(self):
         pygame.draw.circle(self.screen,self.color,[WIDTH//2,HEIGHT//2],min(self.size,500))   
    
    
    



class Food:
    def __init__(self, screen):
        self.pos = [random.randint(-WIDTH, WIDTH), random.randint(-HEIGHT,HEIGHT)]
        self.size = 10
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.screen = screen
        
    def draw(self, main):
        
        screen_x = self.pos[0] - main.pos[0] + WIDTH // 2
        screen_y = self.pos[1] - main.pos[1] + HEIGHT // 2
        
        pygame.draw.circle(self.screen, self.color, [int(screen_x), int(screen_y)], self.size)


class Vorog(Entity):
    def __init__(self, screen):
        self.pos = [random.randint(-WIDTH//2, WIDTH//2), random.randint(-HEIGHT//2,HEIGHT//2)]
        self.speed = 1
        self.size = 25
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.screen = screen

    def live(self,key):
        
        if key == "w":
            self.pos[1] -= 10
        if key == "a":
            self.pos[0] -= 10 
        if key == "s":
            self.pos[1] += 10  
        if key == "d":
            self.pos[0] += 10
    
    
    def draw(self, main):
        
        screen_x = self.pos[0] - main.pos[0] + WIDTH // 2
        screen_y = self.pos[1] - main.pos[1] + HEIGHT // 2
        
        pygame.draw.circle(self.screen, self.color, [int(screen_x), int(screen_y)], self.size)



    