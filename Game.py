import pygame
from pygame import Color

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bgcolor = Color(130, 72, 17)

screen.fill(bgcolor)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
    pygame.display.update()
