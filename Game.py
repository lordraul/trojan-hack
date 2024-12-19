import pygame
from pygame import Color
from soldier import Soldier
from soldier import Direction

pygame.init()

WIDTH = 1280
HEIGHT = 720

SSIZE = 50
SSPEED = 200 / 60.0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bgcolor = Color(130, 72, 17)

x = (WIDTH - SSIZE) / 2
y = (HEIGHT - SSIZE) / 2
soldiers = [Soldier(pygame.Rect(x+(i*2*SSIZE), y, SSIZE, SSIZE), Direction(i)) for i in range(4)]

moving_soldier = -1

running = True
while running:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if moving_soldier == -1:
                for i in range(len(soldiers)):
                    soldier = soldiers[i]
                    if soldier.rect.collidepoint(mouse):
                        moving_soldier = i

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    if moving_soldier != -1:
            soldiers[moving_soldier].rect.x += soldiers[moving_soldier].direction.X() * SSPEED
            soldiers[moving_soldier].rect.y += soldiers[moving_soldier].direction.Y() * SSPEED

            x = soldiers[moving_soldier].rect.x
            y = soldiers[moving_soldier].rect.y

            print((x,y))

            if x < -SSIZE or x >= WIDTH or y < -SSIZE or y >= HEIGHT:
                if x >= WIDTH: soldiers[moving_soldier].rect.x += 5
                moving_soldier = -1

            for i in range(len(soldiers)):
                if i != moving_soldier and soldiers[moving_soldier].rect.colliderect(soldiers[i].rect):
                    soldiers[moving_soldier].rect.x -= soldiers[moving_soldier].direction.X() * SSPEED
                    soldiers[moving_soldier].rect.y -= soldiers[moving_soldier].direction.Y() * SSPEED
                    moving_soldier = -1
                    break

    screen.fill(bgcolor)

    for soldier in soldiers:
        pygame.draw.rect(screen, Color(0, int(255 * (soldier.direction.value / 3.0)), 0), soldier.rect)
    
    pygame.display.flip()
    clock.tick(60)
