def pong():
    import pygame,sys
    import random
    from pygame import mixer

    
    #initialising pygame

    pygame.init()
    screen_width=800
    screen_height=600
    screen=pygame.display.set_mode((screen_width,screen_height))
    clock=pygame.time.Clock()
    pygame.display.set_caption("Pong!")
    icon=pygame.image.load("assets\\ping-pong.png")
    pygame.display.set_icon(icon)
    mixer.music.load("assets\\pongbmg.wav")
    mixer.music.play(-1)
    paddlesound=mixer.Sound("assets\\paddlesound.wav")
    wallsound=mixer.Sound('assets\\wallsound.wav')
    pointsound=mixer.Sound('assets\\pointsound.wav')
    pointsound.set_volume(0.3)
    wallsound.set_volume(0.3)
    paddlesound.set_volume(0.3)




    #Game objects
    game_state='playing'
    ball=pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,20,20)
    player=pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
    opponent=pygame.Rect(10,screen_height/2 - 70,10,140)
    gameover=pygame.image.load('assets\\gameover.png')
    playercolor=random.choice(((115,255,87),(255,255,255),(87,87,255),(255,245,87)))
    ballcolor=(235,35,35)
    playerscore=0
    opponentscore=0
    userinfo=''
    textfont=pygame.font.Font("freesansbold.ttf",24)
    userfont=pygame.font.Font("freesansbold.ttf",48)
    #movement

    ball_speed_x=5 * random.choice((1,-1))
    ball_speed_y=5 * random.choice((1,-1))

    player_speed=0
    opponent_speed=7
    #game loop

    running=True
    while running:
        screen.fill((23,23,23))
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    player_speed+=7
                if event.key==pygame.K_UP:
                    player_speed-=7
                if event.key==pygame.K_ESCAPE:
                    running=False
                    mixer.music.load("assets\\arcadebackground.wav")
                    mixer.music.play(-1)
                if event.key==pygame.K_RETURN:
                    if game_state=='over':
                        playerscore=0
                        opponentscore=0
                        ball_speed_x=5 * random.choice((1,-1))
                        ball_speed_y=5 * random.choice((1,-1))
                        player_speed=0
                        opponent_speed=7



                        
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_DOWN:
                    player_speed-=7
                if event.key==pygame.K_UP:
                    player_speed+=7
            
        
        #ball movement and collision
            
        ball.x+=ball_speed_x 
        ball.y+=ball_speed_y
        
        if ball.top<=0 or ball.bottom>=screen_height:
            ball_speed_y*=-1
            wallsound.play()
        if ball.left<=0:
            ball.y=screen_height/2
            ball.x=screen_width/2
            ball_speed_x=random.choice((5,-5))
            ball_speed_y=random.choice((5,-5))
            playerscore+=1
            pointsound.play()
        if ball.right>=screen_width:
            ball.y=screen_height/2
            ball.x=screen_width/2
            ball_speed_x=random.choice((5,-5))
            ball_speed_y=random.choice((5,-5))
            opponentscore+=1
            pointsound.play()
        if  ball.colliderect(opponent):
            ball_speed_x*=random.choice((-1,-2,-3,-4))
            paddlesound.play()
        if  ball.colliderect(player):
            ball_speed_x=-5
            paddlesound.play()
        if player.top<=0:
            player.top=0
            
        if player.bottom>=screen_height:
            player.bottom=screen_height
            
        if opponent.top<=0:
            opponent.top=0
            
        if opponent.bottom>=screen_height:
            opponent.bottom=screen_height
            
        if opponent.y-25<ball.y:
            opponent.top+=opponent_speed
            
        if opponent.y+25>ball.y:
            opponent.bottom-=opponent_speed

        player.y+=player_speed
            
        pygame.draw.rect(screen,playercolor,player)
        pygame.draw.rect(screen,playercolor,opponent)
        pygame.draw.ellipse(screen,ballcolor,ball)
        pygame.draw.aaline(screen,random.choice(("red","green","blue")),(screen_width/2,0),(screen_width/2,screen_height))

        if opponentscore==5:
            game_state='over'
            ball_speed_x=0
            ball_speed_y=0
            player_speed=0
            opponent_speed=0
            screen.blit(gameover,(0,0))
            screen.blit(usertext,(300,350))



        playertext=textfont.render(f"{playerscore}",False,(135,135,135))
        screen.blit(playertext,(410,290))
        opponenttext=textfont.render(f"{opponentscore}",False,(135,135,135))
        screen.blit(opponenttext,(380,290))
        usertext=userfont.render(f"{userinfo}",False,(255,255,255))
        
        #updating the window
        pygame.display.flip()
        clock.tick(60)

