import random
import pygame 
import math
import time



WIDTH = 1920
HEIGHT = 1080

        

class Food:
    def __init__(self):
        self.pos = [random.randint(-WIDTH, WIDTH), random.randint(-HEIGHT,HEIGHT)]
        self.size = 10
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
    def draw(self, main):
        
        screen_x = self.pos[0] - main.pos[0] + WIDTH // 2
        screen_y = self.pos[1] - main.pos[1] + HEIGHT // 2
        
        pygame.draw.circle(screen, self.color, [int(screen_x), int(screen_y)], self.size)


class Vorog:
    def __init__(self):
        self.pos = [random.randint(-WIDTH//2, WIDTH//2), random.randint(-HEIGHT//2,HEIGHT//2)]
        self.speed = 1
        self.size = 25
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

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
        
        pygame.draw.circle(screen, self.color, [int(screen_x), int(screen_y)], self.size)



    def check_colide(self, other):
        distance = math.sqrt((self.pos[0]- other.pos[0])**2 + (self.pos[1]- other.pos[1])**2)
        if distance < self.size-2:
            self.size += 2
            return False
        return True

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True 
main_hero = Main_hero()
select = 1 
bgr_color = (250,250,250) 
food_lst = [Food() for i in range(500)]
enemy_lst = [Vorog() for a in range(20)]
start = time.time()

while running:
    pygame.time.Clock().tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

    screen.fill(bgr_color)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        select = 1
    if keys[pygame.K_e]:
        select = 2
    if keys[pygame.K_r]:
        bgr_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

 

    main_hero.live(keys)
    
    main_hero.draw()
    for enemy in enemy_lst:
        enemy.live(random.choice(["w",'a','s','d']))
        enemy.draw(main_hero)
    for food in food_lst:
        if main_hero.check_colide(food):
            food.draw(main_hero)
        else:
            food_lst.remove(food)
        
        if food:
            for enemy in enemy_lst:
                if enemy.check_colide(food):
                    food.draw(main_hero)
                else:
                    food_lst.remove(food)
    
    if time.time() > start+0.1:
        food_lst.append(Food())        
        start = time.time()


    pygame.display.flip()
