import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Moja hra")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

test_surface = pygame.image.load('C:\\Users\\nahrada\\Desktop\\python\\pygame\\graphics\\Sky.png')
ground_surface = pygame.image.load('C:\\Users\\nahrada\\Desktop\\python\\pygame\\graphics\\ground.png')
text_surface = test_font.render("Moja hra", False, "black")


snail_surface = pygame.image.load('C:\\Users\\nahrada\\Desktop\\python\\pygame\\graphics\\snail\\snail1.png')
snail_x_pos = 600


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface, (0, 0))
    pygame.display.update()

    snail_x_pos = snail_x_pos - 1
    screen.blit(snail_surface, (snail_surface, 250))
    pygame.display.update()

    clock.tick(60)