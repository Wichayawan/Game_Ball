import pygame


pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([237, 223, 224])
my_ball = pygame.image.load("images/beach_ball.png")

x_speed = 1
x = 0
y = 80
running = True
while running:
    screen.fill([237, 223, 224])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = x + x_speed
    if x > screen.get_width():
        x = 0
    
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

pygame.quit()
