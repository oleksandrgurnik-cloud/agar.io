import pygame



pygame.init()

screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
running = True
y = 0
x = 0
dx = 1
dy = 1
while running:
    y+=dy
    x+=dx
    clock.tick(120)
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255,0,0), (y,x,40,40))
   
    if y >= 360:
        dy = -1
    if x >= 360:
        dx = -1
    if x < 0:
        dx = 1
    if y < 0:
        dy = 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()   