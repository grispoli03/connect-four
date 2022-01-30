import os
import pygame
import sys

pygame.init()

size = width, height = 320, 240
dx, dy = 2, 2
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ballpath = os.path.join("assets", "intro_ball.gif")
ball = pygame.image.load(ballpath)
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        dx = -dx
    if ballrect.top < 0 or ballrect.bottom > height:
        dy = -dy

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
