import pygame, sys
from pygame.locals import *
import numpy

pygame.init()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption('Drawing with Pygame')

colors = numpy.random.randint(0, 255, size=(4, 3))

WHITE = (255, 255, 255)

# make screen white
screen.fill(WHITE)
# Circle in the center of the window
pygame.draw.circle (screen, colors[0], (200, 200), 25, 0)

# Half diagonal from the upper-left corner to the center
pygame.draw.line (screen, colors[1], (0, 0), (200, 200), 3)

pygame.draw.rect(screen, colors[2], (200,50,  100,  100))
pygame.draw.ellipse(screen, colors[3],(200, 100, 100, 150), 2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
