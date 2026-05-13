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
                if self.size <200:

                    self.size += 2
                return False
            if isinstance(other, Vorog):
                if self.size > other.size:
                    if self.size < 200:
                       self.size += other.size
                    return 'ми зїли'
                elif self.size <other.size:
                    if other.size < 200:

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
        if keys[pygame.K_w] and self.pos[1] > WIDTH // 2 - 2000:
            self.pos[1] -= 10
        if keys[pygame.K_a] and self.pos[0] > WIDTH // 2 - 2000:
            self.pos[0] -= 10 
        if keys[pygame.K_s] and self.pos[1] < WIDTH // 2 + 2000:
            self.pos[1] += 10  
        if keys[pygame.K_d] and self.pos[0] < WIDTH // 2 + 2000:
            self.pos[0] += 10
    
    
    def draw(self):
         pygame.draw.circle(self.screen,self.color,[WIDTH//2,HEIGHT//2],min(self.size,500))   
    
    
    



class Food:
    def __init__(self, screen):
        self.pos = [random.randint(WIDTH // 2 - 2000, WIDTH // 2 + 2000), random.randint(WIDTH // 2 - 2000,WIDTH // 2 + 2000)]
        self.size = 10
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.screen = screen
        
    def draw(self, main):
        
        screen_x = self.pos[0] - main.pos[0] + WIDTH // 2
        screen_y = self.pos[1] - main.pos[1] + HEIGHT // 2
        
        pygame.draw.circle(self.screen, self.color, [int(screen_x), int(screen_y)], self.size)


class Vorog(Entity):
    def __init__(self, screen):
        self.pos = [random.randint(WIDTH // 2 - 2000, WIDTH // 2 + 2000), random.randint(WIDTH // 2 - 2000,WIDTH // 2 + 2000)]
        self.speed = 1
        self.size = 25
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.screen = screen
        self.timer = 0
        self.move =  (random.randint(-1,1), random.randint(-1,1))

    def live(self):
        
        dy,dx = self.move
       
            
        self.pos[0] +=dy*5
        self.pos[1] += dx*5

    
    def draw(self, main):
        
        screen_x = self.pos[0] - main.pos[0] + WIDTH // 2
        screen_y = self.pos[1] - main.pos[1] + HEIGHT // 2
        
        pygame.draw.circle(self.screen, self.color, [int(screen_x), int(screen_y)], self.size)



    