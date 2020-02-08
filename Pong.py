def pong():
    global possession
    import random
    import pygame


    def background():
        pygame.draw.rect(screen,(225,225,225),(0,0,800,5))
        pygame.draw.rect(screen,(225,225,225),(0,495,800,5))
        for mids in range (0,500,40):#[0,40,80,120,160,200,240,280,400]:
            pygame.draw.rect(screen,(225,225,225),(395,mids,10,20))
                         
                         
    pygame.init()
    screen = pygame.display.set_mode((800,500))


    p1y=0             
    p2y=0
    p1w=100
    p2w=100
    bally = 400     # y position
    ballx = 400     # x position
    ballvel = 5  #velocity in x direction
    ballvely = -1  #velocity in y direction
    powerupstat = False
    possession = 'p1'

    running = True
    start_ticks2=pygame.time.get_ticks()
    start_ticks=pygame.time.get_ticks()
    while running == True:
      pygame.time.delay(10)
      screen.fill((0,0,0))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False


      if ballvel < 0:
        possession = 'p2'
      elif ballvel > 0:
        possession = 'p1'
      #p1 controls
      keys = pygame.key.get_pressed()
      if keys[pygame.K_w] and p1y > 0:
        p1y-=10
      if keys[pygame.K_s] and p1y < 400:
        p1y+=10

      pygame.draw.rect(screen,(225,225,225),(0,p1y,30,p1w))
      
      #p2 controls
      keys = pygame.key.get_pressed()
      if keys[pygame.K_UP] and p2y > 0:
        p2y-=10
      if keys[pygame.K_DOWN] and p2y < 400:
        p2y+=10

      pygame.draw.rect(screen,(225,225,225),(770,p2y,30,p2w))


      if ballx <= 30 and ballx > 0 and bally > p1y and bally < p1y + p1w and possession == 'p2':
        ballvel=int(ballvel*-1.2)
        possession = 'p1'
        ballvely = int(((bally+10)-(p1y + 50))/5)


      if ballx >= 770 and  ballx < 800 and  bally > p2y and bally < p2y + p2w and possession == 'p1':
        ballvel=int(ballvel*-1.2)
        possession = 'p2'
        ballvely = int(((bally+10)-(p2y + 50))/5)
        
      if bally < 0 or bally > 500:
        ballvely *= -1


      if ballx < 0 or ballx >800:
        if possession == 'p1':
          print ('player 1 wins (left side)')
          #p1win == True
        elif possession == 'p2':
          print ('player 2 wins (right side')
        print('Game Over!')
        running = False



      seconds=(pygame.time.get_ticks()-start_ticks2)/1000
      if seconds>3: # if more than 5
        start_ticks2+=5000
        powerupstat = True
        power = random.randint(1,3)
        randposx=(random.randint(50,750))
        randposy=(random.randint(0,400))

      if powerupstat == True:

        if power == 1: 
          pygame.draw.rect(screen,(0,0,225),(randposx,randposy,100,100))
          if ((randposx+50)-(ballx))<50 and ((randposx+50)-(ballx)) >-50 and (randposy-(bally+20) < 0 and (randposy + 50) - bally >0):
            if possession == 'p1':
                p1w += 20
            if possession == 'p2':
                p2w += 20
            powerupstat = False
            print('slow down')


        if power == 2:
          pygame.draw.rect(screen,(225,225,225),(randposx,randposy,6,100))
          if ((randposx+3)-(ballx))<10 and ((randposx+3)-(ballx)) >-10 and (randposy-(bally+20) < 0 and (randposy + 100) - bally >0):
            ballvel*=-1
            powerupstat = False
            print ('wall')

        if power == 3: 
          pygame.draw.rect(screen,(225,0,0),(randposx,randposy,100,100))
          if ((randposx+50)-(ballx))<10 and ((randposx+50)-(ballx)) >-10 and (randposy-(bally+20) < 0 and (randposy + 50) - bally >0):
            if possession == 'p1':
                p1w -= 20
            if possession == 'p2':
                p2w -= 20
            powerupstat = False
            print ('speed up')

      


       
      pygame.draw.circle(screen,(225,225,225),(ballx,bally),10)
      ballx += int(ballvel)
      bally += int(ballvely)
      

      background()
      print(ballvel)

      pygame.display.update()
      #pygame.mouse.set_pos(-10,-10)
    #pygame.quit()
#pong()

    

