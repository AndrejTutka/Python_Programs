import pygame, time

WIDTH = 800
HEIGHT = 600


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# the game_goes_on variable will keep the game loop running as long as it is True
game_goes_on = True
x = 200
y = 200
dx = 1
fx = 1
while game_goes_on:

    # INPUT PROCESSING
    # pygame.event.get() returns a list of unprocessed events
    for event in pygame.event.get():

        # this will only serve to see what events can occur and to see their characteristics
        print(event)

        # one of the possible events is pygame.QUIT, which occurs when the user closes the window
        # e.g. by clicking the close button or pressing Alt+F4
        if event.type == pygame.QUIT:
            game_goes_on = False


    # CURRENT STATE UPDATE
    
    if x +60 >= WIDTH or x <=0:
        dx = -dx
    
    x += dx # rate of change for x ='speed'
    y += fx
    
    if y+30 >= HEIGHT or y<=0:
        fx = -fx
        

    # RENDERING
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,0,0), (x, y, 60, 30))
    pygame.display.update()


pygame.quit()
