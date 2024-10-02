import pygame
import random

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([237, 223, 247])

def random_mixed_circles_and_rects(num_objects):
    for i in range(num_objects):
        if random.randint(0, 1) == 0:
            # Draw a circle
            radius = random.randint(10, 100)
            x = random.randint(0, 640)  # Fixed typo
            y = random.randint(0, 480)
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            pygame.draw.circle(screen, color, [x, y], radius)
        else:
            # Draw a rectangle
            x = random.randint(0, 640)
            y = random.randint(0, 480)
            width = random.randint(20, 200)
            height = random.randint(20, 200)
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            pygame.draw.rect(screen, color, [x, y, width, height])

# Draw 200 random objects (circles and rectangles)
random_mixed_circles_and_rects(200)

# Update the display to show the drawn objects
pygame.display.flip()

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()