import random
import pygame


class MainHero:
    def __init__(self):
        self.speed = 1
        self.pos = [300,300]
        self.color = (255,0,255)
        self.size = 1
        

    def live_cycle(self, keys):
        if self.size < 10:
            self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if self.size > 100:
            self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        if keys[pygame.K_w]:
            self.pos[1] -= 10
        if keys[pygame.K_a]:
            self.pos[0] -= 10 
        if keys[pygame.K_s]:
            self.pos[1] += 10  
        if keys[pygame.K_d]:
            self.pos[0] += 10
        self.size += self.speed
        if self.size > 100:
            self.speed = -1
        
        if self.size < 1:
            self.speed = 1


    def draw(self):
        pygame.draw.circle(screen,self.color,self.pos,self.size)



pygame.init()
screen = pygame.display.set_mode((1920,1080))
running = True 
main_hero = MainHero()
main_hero2 = MainHero()
main_hero.pos = [500,500]
selected = 1
while running:
    pygame.time.Clock().tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    screen.fill((0,70,0))

    if keys[pygame.K_g]:
        
        selected = 1
        
    if keys[pygame.K_h]:
        selected = 2
    
    if selected == 1:

        main_hero.live_cycle(keys)
    if selected == 2:
        main_hero2.live_cycle(keys)
    main_hero.draw()
    main_hero2.draw()
    pygame.display.flip()
