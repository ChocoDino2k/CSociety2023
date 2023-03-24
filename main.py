import pygame
import time

if __name__ == "__main__":
    pygame.init()

screen = pygame.display.set_mode((1000, 500))
screen.fill((27, 27, 27))
pygame.display.flip()
time.sleep(20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running == False
        elif event.type == QUIT:
            running = False