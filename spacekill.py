import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from pygame import mixer
pygame.init()


class gametest:
    WIDTH , HEIGHT = 700 , 700
    win = pygame.display.set_mode((WIDTH,HEIGHT))
    x0=0
    y0=0
    width = 10
    height = 10
    ufo = pygame.image.load('ufo (1).png')
    player = pygame.image.load('rocket-launch (1).png')
    x=0
    y=300
    v=2
    run=True
    h=1
    x1 = 600
    y1 = random.randint(0,600)
    back = pygame.image.load('spaceback.jpg')
    bullet = pygame.image.load('bullet.png')
    inc=0
    st = 0
    h1=0
    score = 0
    life = 1
    x0=0
    y0=0
    sc=0
    mixer.music.load('8-bit-Indigestion.wav')
    mixer.music.play(-1)
    blast = mixer.Sound('mixkit-falling-hit-757.wav')
    while run:
        pygame.time.delay(20)
        for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run=False
        win.fill((0,0,0))
        win.blit(back,(0,0))
        
        #pygame.draw.rect(win , (255,0,0) , (x,y,width,height))   
        win.blit(player,(x,y))
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x>v:
            x-=4*v
        if keys[pygame.K_RIGHT] and x<700-width-v:
            x+=4*v
        if keys[pygame.K_UP] and y>v:
            y-=4*v
        if keys[pygame.K_DOWN] and y<700-height-v:
            y+=4*v
        if keys[pygame.K_h]:
            bullet_sound=mixer.Sound('mixkit-short-laser-gun-shot-1670.wav')
            bullet_sound.play()
            if inc==0:
                inc=1
                st=y
                h1=0

        if h1==40:
            h1=0
            inc=0
            x0=x
            y0=y

        if inc==1:
            x0=x+40*h1
            y0=st
            win.blit(bullet,(x0,y0+20))
            
        x1-=2
        win.blit(player,(x,y))
        if (x1>=1):
            win.blit(ufo,(x1-h/2048,y1))
        else:
            x1 = 600
            y1 = random.randint(1,600)
            h=0
            life-=1
        h+=1
        h1+=1

        if (((x0-x1)**2+(y0-y1)**2)**0.5 <=50 and x0>=x+2):
            x1=700
            y1=random.randint(1,600)
            h=0
            score=score+1
            sc=1
            blast.play()

    
        if life==0:
            run=False
            
            
        pygame.display.update()
    subject = "Game Over"
    content = ("Score:",score)
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    root.destroy()

pygame.quit()

    
    
                