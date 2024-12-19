import pygame
from pygame import Color
from soldier import Soldier
from soldier import Direction
import Procedural

pygame.init()
pygame.font.init()

fontmar = pygame.font.SysFont('Comic Sans MS', 45)
win = fontmar.render("Everyone is out of the horse! Let's demolish Troy!", False, (255,255,255))

WIDTH = 1080
HEIGHT = 1080

SSIZE = 100
SSPEED = 700 / 60.0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

soldierIMG = pygame.image.load("soldier.png")
soldierIMG = pygame.transform.scale(soldierIMG, (3 * SSIZE, 3 * SSIZE))

plank = pygame.transform.rotate(pygame.image.load("wood.png"), 90)
plank.fill((0, 0, 0, 200), special_flags=pygame.BLEND_ADD)

winbg = pygame.image.load("win.png")

bg = plank

bgcolor = Color(130, 72, 17)

soldiers = []

SX = (WIDTH - (6 * SSIZE)) / 2.0
SY = (HEIGHT - (6 * SSIZE)) / 2.0

grid, e, r = Procedural.Generate((6,6))
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] is not None:
            print((r,c))
            rect = pygame.Rect(SX + c * SSIZE, SY + r * SSIZE, SSIZE, SSIZE)
            soldiers.append(Soldier(rect, grid[r][c]))

moving_soldier = -1

running = True
while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")
            if moving_soldier == -1:
                print("nomover")
                for i in range(len(soldiers)):
                    soldier = soldiers[i]
                    print(soldier.rect)
                    if soldier.rect.collidepoint(mouse):
                        print("mover")
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

            if moving_soldier != -1 and x < -SSIZE or x >= WIDTH or y < -SSIZE or y >= HEIGHT:
                if x >= WIDTH: soldiers[moving_soldier].rect.x += 5
                soldiers.remove(soldiers[moving_soldier])
                moving_soldier = -1
                continue

            for i in range(len(soldiers)):
                if i != moving_soldier and soldiers[moving_soldier].rect.colliderect(soldiers[i].rect):
                    soldiers[moving_soldier].rect.x -= soldiers[moving_soldier].direction.X() * SSPEED
                    soldiers[moving_soldier].rect.y -= soldiers[moving_soldier].direction.Y() * SSPEED
                    moving_soldier = -1
                    break

    screen.blit(bg, (0,0))

    if len(soldiers) == 0:
        screen.blit(win, (0,0))
        bg = winbg

    for soldier in soldiers:
        img = pygame.transform.rotate(soldierIMG, [180,0,-90,90][soldier.direction.value])
        rect = soldier.rect.copy()
        rect.x -= (img.get_size()[0] - rect.width) / 2.0
        rect.y -= (img.get_size()[1] - rect.height) / 2.0
        screen.blit(img, rect)
        # pygame.draw.rect(screen, Color(0, 0, 0, 0), soldier.rect)
    
    pygame.display.flip()
    clock.tick(60)
