import random
import pygame 
class Main_hero:
    def __init__(self):
        self.pos = [230,230]
        self.speed = 1
        self.size = 1
        self.color = (100,0,180)

    
    

    def live(self,keys):
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
main_hero = Main_hero()
main_hero2 = Main_hero()
select = 1 
bgr_color = (0,0,0) 
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

    if select == 1:

        main_hero.live(keys)
    if select == 2:
        main_hero2.live(keys)

    main_hero.draw()
    main_hero2.draw()





    pygame.display.flip()