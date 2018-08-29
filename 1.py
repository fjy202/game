import time
import random
import pygame as pg
screen=pg.display.set_mode([800,600],pg.NOFRAME)
a='探秘'
pg.display.set_caption('探秘')
i=0
door=30
while True:
    for e in pg.event.get():
        if e.type==pg.QUIT:
            pygame.quit()
        if e.type===pg.KEYDOWN:
            if e.key==pg.K_UP:
                i+=random.randint(1,9)
                if i>door:
                    pg.display.set_caption('探秘(你死了)')
                    pygame.quit()
                    exit()
            pg.draw.circle(screen,(0,255,0),(10,i),7)
            
