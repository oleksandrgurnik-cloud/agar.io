import random
import pygame 
import time
import random
from heros import Main_hero, Food, Vorog,WIDTH,HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True 
main_hero = Main_hero(screen)
select = 1 
bgr_color = (250,250,250) 
food_lst = [Food(screen) for i in range(500)]
enemy_lst = [Vorog(screen) for a in range(20)]
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

    new_food_lst = []
    new_enemy_lst = []
    for food in food_lst:
        if main_hero.check_colide(food):
            food.draw(main_hero)
            new_food_lst.append(food)
            for enemy in enemy_lst:
                if enemy.check_colide(food):
                    food.draw(main_hero)
                
                else:
                    new_food_lst.remove(food)
                
    for enemy in enemy_lst:
        if main_hero.check_colide(enemy) is True:
            new_enemy_lst.append(enemy)
        elif main_hero.check_colide(enemy) == 'нас зїли':
            running = False


    food_lst = new_food_lst
    enemy_lst = new_enemy_lst   
    if time.time() > start+0.1:
        food_lst.append(Food(screen))        
        start = time.time()


    pygame.display.flip()