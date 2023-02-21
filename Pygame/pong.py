import pygame, time

WIDTH = 800
HEIGHT = 600


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# the game_goes_on variable will keep the game loop running as long as it is True
game_goes_on = True


racket_A = {'x':40, 'y':270,'speed':0.5}
racket_B = {'x':750, 'y':270,'speed':0.5}

ball = {'x':400, 'y':300, 'radius':7, 'dx':0.25, 'dy':0.25}

myfont = pygame.font.SysFont('Arial', 60)
show_text = False
while game_goes_on:

    # INPUT PROCESSING
    # pygame.event.get() returns a list of unprocessed events
    for event in pygame.event.get():

        # this will only serve to see what events can occur and to see their characteristics
#         print(event)

        # one of the possible events is pygame.QUIT, which occurs when the user closes the window
        # e.g. by clicking the close button or pressing Alt+F4
        if event.type == pygame.QUIT:
            game_goes_on = False
        
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        racket_A['y'] -=racket_A['speed']
    if keys[pygame.K_s]:
        racket_A['y'] +=racket_A['speed']
    if keys[pygame.K_UP]:
        racket_B['y'] -=racket_B['speed']
    if keys[pygame.K_DOWN]:
        racket_B['y'] +=racket_B['speed']
    
    
    if ball['y']>=600 or ball['y']<=0:
        ball['dy'] = -ball['dy']
    

        
        
    
    
    
            

    # CURRENT STATE UPDATE
    ball['x'] +=ball['dx']
    ball['y'] +=ball['dy']

    # RENDERING
    screen.fill((0, 0, 0))
    if ball['x']>=800:
        text = myfont.render(f"Win!", True, (255,255,255), (0,0,0))
        text_rectangle = text.get_rect(center = (200, 40))
        screen.blit(text, text_rectangle)
        show_text = True
    if ball['x']<=0:
        text = myfont.render(f"Win!", True, (255,255,255), (0,0,0))
        text_rectangle = text.get_rect(center = (200, 40))
        screen.blit(text, text_rectangle)
        show_text = True
    pygame.draw.rect(screen, (255,255,255), (racket_A['x'], racket_A['y'], 10, 60))
    pygame.draw.rect(screen, (255,255,255), (racket_B['x'], racket_B['y'], 10, 60))
    pygame.draw.rect(screen, (255,255,255), (WIDTH/2-2.5,0, 2.5, HEIGHT))
    
    pygame.draw.circle(screen, (255,255,255),(ball['x'],ball['y']),ball['radius'])
    
    pygame.display.update()
    
    if show_text:
        time.sleep(2)
        ball['x'] = 400
        show_text = False


pygame.quit()