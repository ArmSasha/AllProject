#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT{
import pygame
import random
import time

# }

# ОСНОВА {
WIDTH = 500
HEIGHT = 500
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
BLUE = (2, 26, 252)
ORANGE = (254, 89, 0)
SALAD = (175, 255, 0)
BROWN = (139, 79, 57)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
way = 'C:/Program Files (x86)/PythonFiles/KESHA/Дурачество/Пик-Клик/'
clock = pygame.time.Clock()
cookie = pygame.image.load(way + 'Печенька.png')
cookie2 = pygame.image.load(way + 'Печенька2.png')
cookie3 = pygame.image.load(way + 'Печь.png')
background = pygame.image.load(way + 'Фон.jpg')
cook = pygame.image.load(way + 'Печенье.png')
heart1 = pygame.image.load(way + 'Сердце.png')
heart2 = pygame.image.load(way + 'Сердце2.png')
heart3 = pygame.image.load(way + 'Сердце3.png')
heart4 = pygame.image.load(way + 'Сердце4.png')
shop = pygame.image.load(way + 'add.gif')
heart = pygame.image.load(way + 'Сердце.png')
strelca = pygame.image.load(way + 'Стрелка2.0.jpg')
# }

shrift = pygame.font.SysFont('Time New Romans', 48)
shrift2 = pygame.font.SysFont('Time New Romans', 24)
shrift3 = pygame.font.SysFont('Time New Romans', 20)
shrift4 = pygame.font.SysFont('Time New Romans', 17)

score = 0
gamemode = "MENU"
hearthp = 90  # 90,60,30,0 -30
slovo = []
slovocords = []
sena = str(200)

while True:

    # MENU{
    screen.fill(BROWN)

    if gamemode == "MENU":
        pygame.draw.rect(screen, (244, 164, 96), (25, 100, 100, 75))
        pygame.draw.rect(screen, (244, 164, 96), (25, 200, 100, 75))
        pygame.draw.rect(screen, (244, 164, 96), (25, 300, 100, 75))
        screen.blit(cook, (200, 95))

        textPoints = shrift.render("Пик-Клик", 0, (214, 107, 0))
        screen.blit(textPoints, (155, -5))

        text1 = shrift2.render("PLAY", 0, (214, 107, 0))
        screen.blit(text1, (41, 120))

        text2 = shrift3.render("AUTHOR", 0, (214, 107, 0))
        screen.blit(text2, (28, 225))

        text3 = shrift3.render("SETTING", 0, (214, 107, 0))
        screen.blit(text3, (28, 325))

        for i in pygame.event.get():

            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > -20 and i.pos[0] < 150 \
                    and i.pos[1] > -20 and i.pos[1] < 150:
                    gamemode = "GAME"

            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > -130 and i.pos[0] < 150 \
                    and i.pos[1] > 150 and i.pos[1] < 250:
                    gamemode = "AUTHOR"

            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > -330 and i.pos[0] < 150 \
                    and i.pos[1] > 280 and i.pos[1] < 350:
                    gamemode = "SETTING"

            if i.type == pygame.QUIT:
                pygame.quit()
                exit

        # pygame.display.update()
        # }

    # PLAY {

    if gamemode == "GAME":
        screen.fill(BROWN)

        screen.blit(strelca, (100, -5))

        textPoints = shrift.render(score, 0, (222, 111, 0))
        screen.blit(textPoints, (240, -5))
        pygame.draw.rect(screen, (244, 164, 96), (20, 400, 100, 50))
        pygame.draw.rect(screen, (244, 164, 96), (130, 400, 100, 50))
        pygame.draw.rect(screen, (244, 164, 96), (240, 400, 100, 50))
        pygame.draw.rect(screen, (244, 164, 96), (360, 400, 100, 50))
        textPoints = shrift4.render("Авто клик", 0, (222, 111, 0))
        screen.blit(textPoints, (18, 400))
        textPoints = shrift4.render("Цена" + sena, 0, (222, 111, 0))
        screen.blit(textPoints, (18, 420))
        pygame.display.update()

        screen.blit(cookie3, (200, 200))
        # СЕРДЦЕ{
        screen.blit(heart, (100, 100))
        if hearthp == 90:
            heart = heart1

        elif hearthp == 60:
            heart = heart2

        elif hearthp == 30:
            heart = heart3

        elif hearthp == 0:
            heart = heart4

        if hearthp == 0:
            hearthp += 90
            score += 2
        # }
        for i in pygame.event.get():

            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > -20 and i.pos[0] < 350 \
                        and i.pos[1] > -300 and i.pos[1] < 350:
                    score += 1
                    screen.fill(BROWN)
                    textPoints = shrift.render(score, 0, (222, 111, 0))
                    screen.blit(textPoints, (240, -5))
                    screen.blit(cookie3, (200, 200))

                    hearthp -= 30
                    # pygame.display.update()

            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > 0 and i.pos[0] < 200 \
                        and i.pos[1] > 0 and i.pos[1] < 100:
                    gamemode = "MENU"

            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > 20 and i.pos[0] < 120 \
                        and i.pos[1] > 400 and i.pos[1] < 450:
                    # gamemode = "MENU"
                    pass
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > 130 and i.pos[0] < 230 \
                        and i.pos[1] > 400 and i.pos[1] < 450:
                    # gamemode = "MENU"
                    pass

            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > 240 and i.pos[0] < 340 \
                        and i.pos[1] > 400 and i.pos[1] < 450:
                    # gamemode = "MENU"
                    pass
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > 350 and i.pos[0] < 450 \
                        and i.pos[1] > 400 and i.pos[1] < 450:
                    # gamemode = "MENU"
                    pass

            if score == 9 or score == 13 or score == 14 or score == 103:
                score += 30

        # Стова{
        # textPoints=shrift2.render("Вы выполнили задани и получили награду", 0, (222,111,0))
        # screen.blit(textPoints,(200,100))

        # }

        # }

        # AUTHOR {
    if gamemode == "AUTHOR":
        screen.fill(BROWN)
        screen.blit(strelca, (100, -5))

        textPoints = shrift.render("Бадикян Саша", 0, (237, 119, 0))
        screen.blit(textPoints, (55, 200))
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > 0 and i.pos[0] < 200 \
                        and i.pos[1] > 0 and i.pos[1] < 100:
                    gamemode = "MENU"

        # pygame.display.update()

    # }

    # SETTING {
    if gamemode == "SETTING":
        screen.fill(BROWN)
        screen.blit(strelca, (100, -5))

        textPoints = shrift2.render("Ну что-то должно было быть", 0, (237, 119, 0))
        screen.blit(textPoints, (55, 200))

        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and i.pos[0] > 0 and i.pos[0] < 200 \
                        and i.pos[1] > 0 and i.pos[1] < 100:
                    gamemode = "MENU"

        # pygame.display.update()
        # }

    # END{
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit
            pygame.display.update()
            clock.tick(FPS)
    # }
    pygame.display.update()
    clock.tick(FPS)


