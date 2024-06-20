import pygame
import random
import time
wh = 500
w = 30
interval = 0.7
white = (255,255,255)
black = (0,0,0)
window = pygame.display.set_mode((500,500))
window.fill(white)
running = True
rectangle = pygame.draw.rect(window,black,(random.randint(0,wh - w),random.randint(0,wh - w),w,w))
currentTime = time.time()
scores = 0
while running:
    if time.time() - currentTime > interval:
        window.fill(white)
        rectangle = pygame.draw.rect(window,black,(random.randint(0,wh - w),random.randint(0,wh - w),w,w))
        currentTime = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rectangle.collidepoint(pygame.mouse.get_pos()):
                window.fill(white)
                rectangle = pygame.draw.rect(window,black,(random.randint(0,wh - w),random.randint(0,wh - w),w,w))
                currentTime = time.time()
                scores+=1
                pygame.display.set_caption(str(scores))
    pygame.display.update()