import pygame
import os
import const
WHITE = (255, 255, 255)
ORANGE = (248, 173, 24)

(wid, ht) = (540, 960)
WIN = pygame.display.set_mode((wid, ht))
pygame.display.set_caption("Palocale")

FPS = 60
font = pygame.font.SysFont('calibri.ttf', 24)
img = font.render('alocale', True, ORANGE)
WIN.blit(img, (270, 300))
WIN.fill(WHITE)
pygame.display.flip()

run = True
clock = pygame.time.Clock()
while run:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


