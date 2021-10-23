import pygame
from random import *
def ball(posX,radius,color,maxi):
    pygame.init()
    
    pos=[posX,0]
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.draw.circle(screen, color, pos, radius)
    def cir(c,p,r):
        pygame.draw.circle(screen,c,p,r)
        pygame.display.update()
    def call():
        while(1==1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pos[0]-=10
                    elif event.key == pygame.K_d:
                        pos[0]+=10
            screen.fill((0, 0, 0))
            pos[1]+=1
            cir(color, tuple(pos),radius)
            if(pos[1]>=maxi):
                 break
   # Main loop
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

            # Add a new enemy?
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

    # Update enemy position
    enemies.update()
            
        while(1==1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pos[0]-=10
                    elif event.key == pygame.K_d:
                        pos[0]+=10
            screen.fill((0, 0, 0))
            pos[1]-=1
            cir(color, tuple(pos),radius)
            if(pos[1]<=0):
                break
    
    x=1
    while(1==1):
        call()

