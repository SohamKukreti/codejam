def arrow():
    import pygame,sys
    import random,math
    from pygame import mixer


    
    #Initialising pygame and setting up window
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Arrow!")
    icon=pygame.image.load("assets\\target.png")
    pygame.display.set_icon(icon)
    background=pygame.image.load("assets\\arrowbackground.png")
    bowimage=pygame.image.load('assets\\bow128.png')
    arrowimage=pygame.image.load('assets\\arrow128.png')
    clock=pygame.time.Clock()
    appleimage=pygame.image.load('assets\\apple.png')
    mixer.music.load("assets\\arrowbgm.wav")
    mixer.music.play(-1)
    arrowsound=mixer.Sound("assets\\arrowshoot.mp3")
    def arrow(x,y):
        screen.blit(arrowimage,(x,y))
    def bow(x,y):
        screen.blit(bowimage,(x-20,y))
    def apple(x,y):
        screen.blit(appleimage,(x,y))
    bowY=250
    bowX=50
    arrowY=250
    arrowX=50
    bowYchange=3
    arrowYchange=3
    arrowXchange=0
    appleX=765
    appleY=random.randint(100,400)
    appleYspeed=0
    score=0
    textfont=pygame.font.Font("assets\\alagard.ttf",48)
    life=3
    userinfo=''
    gameoverimg=pygame.image.load('assets\\gameover.png')
    
    def show_score():
        score_text=textfont.render("Score : " + str(score),True,(255,255,255))
        screen.blit(score_text,(300,20))
        score_text=textfont.render("Lives : " + str(life),True,(255,255,255))
        screen.blit(score_text,(570,20))

        

        
    #Game Loop
    running=True
    while running:
        #screen.fill((255,255,255))
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    arrowsound.play()
                    arrowXchange=10
                    arrowYchange=0
                if event.key==pygame.K_ESCAPE:
                    running=False
                    mixer.music.load("assets\\arcadebackground.wav")
                    mixer.music.play(-1)
                if event.key==pygame.K_RETURN:
                    if life==0:
                        bowY=250
                        bowX=50
                        arrowY=250
                        arrowX=50
                        bowYchange=3
                        arrowYchange=3
                        arrowXchange=0
                        appleX=765
                        print(userinfo)
                        life=3
                        score=0
                if life == 0:
                    userinfo+=event.unicode
                    if event.key==pygame.K_BACKSPACE:
                        userinfo=userinfo[0:-2]
      
        arrowY+=arrowYchange
        arrowX+=arrowXchange
        bowY+=bowYchange
        arrow(arrowX,arrowY)
        bow(bowX,bowY)
        
        apple(appleX,appleY)

        #collision
        distance=math.sqrt((appleX-arrowX)**2 + (appleY-(arrowY+50))**2)
        if distance<=88:
            arrowX=bowX
            arrowY=bowY
            arrowXchange=0
            arrowYchange=bowYchange
            appleY=random.randint(100,400)
            score+=1
        if bowY<=0 or bowY>=472:
            bowYchange*=-1
        if arrowY<=0 or arrowY>=472:
            arrowYchange*=-1
        if arrowX>=672:
            arrowX=bowX
            arrowY=bowY
            arrowXchange=0
            arrowYchange=bowYchange
            life-=1
        show_score()
        if life == 0:
            screen.blit(gameoverimg,(0,0))
            arrowYchange=0
            bowYchange=0
            arrowXchange=0

        clock.tick(60)
        pygame.display.update()


