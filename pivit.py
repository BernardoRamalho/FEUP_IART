import pygame

pygame.init()

screen_size = 600

screen = pygame.display.set_mode((screen_size, screen_size))

run = True
paint = False

square_side = screen_size / 6

while run:
    pygame.time.delay(100)

    x = 0
    y = 0   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    for i in range(36):

        if (y == 0 or x == 0 or y == screen_size - square_side or x == screen_size - square_side) and (y != 0 and x != 0  y == screen_size - square_side and x == screen_size - square_side) :
            pygame.draw.circle(screen, (255, 207, 0), (int(x + 50), int(y + 50)), 40)

        if(paint):
            paint = False
            pygame.draw.rect(screen, (255, 255, 255), (x, y, square_side, square_side))
        else:
            paint = True

        
        x += square_side
        
        if (x > screen_size - square_side):
            y += square_side
            
            x = 0
            
            if(paint):
                paint = False
            else:
                paint = True

        
    pygame.display.update()
pygame.quit()