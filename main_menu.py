import pygame,sys
import random
from pygame import mixer
from ponggame import pong
from arrowusingpygame import arrow
from space_shooter import space
pygame.init()
screen=pygame.display.set_mode((800,600))
icon=pygame.image.load("assets\\arcade.png")
pygame.display.set_icon(icon)
mixer.music.load("assets\\arcadebackground.wav")
mixer.music.play(-1)
buttonsound=mixer.Sound("assets\\buttonsound.mp3")
buttonsound.set_volume(0.2)

def mainmenu():
    image=pygame.image.load("assets\\arrowtext.png")
    image2=pygame.image.load("assets\\pongtext.png")
    image3=pygame.image.load("assets\\spaceshootertext.png")
    imageold=image
    image2old=image2
    image3old=image3
    background=pygame.image.load("assets\\arcadebackground.png")
    pygame.display.set_caption("Main Menu")
    click=False
    button1 = pygame.Rect(50, 250, 200, 75)
    button2 = pygame.Rect(520, 250, 200, 75)
    button3 = pygame.Rect(290, 400, 250, 100)
    while True:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        mx,my=pygame.mouse.get_pos()
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit

            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True


        if button1.collidepoint((mx,my)):
            imagenew = pygame.transform.scale(image, (215, 90))
            image=imagenew
            if click:
                buttonsound.play()
                arrow()

        if button2.collidepoint((mx,my)):
            image2new = pygame.transform.scale(image2, (215, 90))
            image2=image2new

            if click:
                buttonsound.play()
                pong()
        if button3.collidepoint((mx,my)):
            image3new=pygame.transform.scale(image3,(265,115))
            image3=image3new

            if click:
                buttonsound.play()
                space()

 
                
        screen.blit(image, button1)
        screen.blit(image2, button2)
        screen.blit(image3, button3)
        image=imageold
        image2=image2old
        image3=image3old

        #pygame.draw.rect(screen, (255,255,255), button1)
        #pygame.draw.rect(screen, (255, 255, 255), button2)
        #pygame.draw.rect(screen, (255, 255, 255), button3)

        pygame.display.update()
mainmenu()
