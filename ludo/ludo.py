import random, pygame, sys
from pygame.locals import *


FPS = 30
windowHeight = 750
windowWidth = 1200

boardWidth = 600 


BLACK =         (  0,  0,  0)
WHITE =         (255,255,255)
BRIGHTBLUE =    (  0, 50,255)
DARKGREY =      ( 30, 30, 30)
DARKTURQUOISE = (  3, 54, 73)
GREEN =         ( 34,139, 34)
LIGHTGREEN =    (154,205, 50)
RED =           (178, 34, 34)
LIGHTRED =      (205, 92, 92)
PURPLE =        (255,  0,255)
GREY = 		(205,201,201)
NEW =           (  3,150,100)
NORMALGREY =    (105,105,105)
ORANGERED =     (255, 69,  0)
MAROON =        (176, 48, 96)
DEEPPINK =      (255, 20,147)
DARKVIOLET =    (148,  0,211)
LIGHTYELLOW =   (255,215,  0)
YELLOW =    	(255,165,  0)
HOTPINK =       (255,105,180)
PERU =          (205,133, 65)
BLUE =          (  0,  0,128)
LIGHTBLUE =     (  0,  0,205)



HilightColor = WHITE
openBgColor = WHITE
bgcolor = BLACK
bgColor = BLACK
forthWindowColor = (255, 218, 165)
basicfontsize = 20

x = 40

mainboard = [(200 + x, x,'GREEN'),(200 + 4*x,x,'GREEN'),(200 + x,4*x,'GREEN'),(200 + 4*x,4*x,'GREEN'),(200 + 10*x,x,'YELLOW'),(200 + 13*x,x,'YELLOW'),(200 + 10*x,4*x,'YELLOW'),(200+13*x,4*x,'YELLOW'),(200 + 10*x,10*x,'BLUE'),(200 + 10*x,13*x,'BLUE'),(200 + 13*x,10*x,'BLUE'), (200 + 13*x,13*x,'BLUE'),(200 + x, 10*x,'RED'),(200 + 4*x,10*x,'RED'),(200 + 4*x,13*x,'RED'),(200+x,13*x,'RED')]
     

greenBox = [(1,200 + x,x),(1,200 + 4*x,x),(1,200 + x,4*x),(1,200+4*x,4*x)]
yellowBox = [(1,200 + 10*x,x),(1,200 + 13*x,x),(1,200 + 10*x,4*x), (1,200 + 13*x,4*x)]
redBox = [(1,200 + x, 10*x),(1,200 + 4*x,10*x),(1,200 + x,13*x),(1,200+ 4*x,13*x)]
blueBox = [(1,200 + 10*x,10*x),(1,200 + 13*x,10*x),(1,200 + 13*x,13*x),(1,200 + 10*x,13*x)]

  
greenDead = [(0,200 - (3*x) / 2, x),(0,200 - (3*x) / 2, 2*x),(0,200 - (3*x) / 2, 3*x),(0,200 - (3*x) / 2, 4*x)]
yellowDead = [(0,200 +15*x + x/ 2, x),(0,200 +15*x+ (x) / 2, 2*x),(0,200 +15*x+ (x) / 2, 3*x), (0,200 +15*x+ (x) / 2, 4*x)]
redDead = [(0,200 - (3*x) / 2, 13*x),(0,200 - (3*x) / 2, 10*x),(0,200 +15*x + (x) / 2, 12*x),(0,200 - (3*x) / 2, 12*x)]
blueDead = [(0,200 +15*x + (x) / 2, 10*x),(0,200 +15*x + (x) / 2, 11*x),(0,200 + 13*x,13*x),(0,200 +15*x + (x) / 2, 13*x)]


newboard = [(200 + x, x,'GREEN'),(200 + 4*x,x,'GREEN'),(200 + x,4*x,'GREEN'),(200 + 4*x,4*x,'GREEN'),(200 + 10*x,x,'YELLOW'),(200 + 13*x,x,'YELLOW'),(200 + 10*x,4*x,'YELLOW'),(200+13*x,4*x,'YELLOW'),(200 + 10*x,10*x,'BLUE'),(200 + 10*x,13*x,'BLUE'),(200 + 13*x,10*x,'BLUE'), (200 + 13*x,13*x,'BLUE'),(200 + x, 10*x,'RED'),(200 + 4*x,10*x,'RED'),(200 + 4*x,13*x,'RED'),(200+x,13*x,'RED')]


greenArr = [(200 - (3*x) / 2, x),(200 - (3*x) / 2, 2*x),(200 - (3*x) / 2, 3*x),(200 - (3*x) / 2, 4*x)]
yellowArr = [(200 +15*x + x/ 2, x),(200 +15*x+ (x) / 2, 2*x),(200 +15*x+ (x) / 2, 3*x), (200 +15*x+ (x) / 2, 4*x)]
redArr = [(200 - (3*x) / 2, 13*x),(200 - (3*x) / 2, 10*x),(200 +15*x + (x) / 2, 12*x),(200 - (3*x) / 2, 12*x)]
blueArr = [(200 +15*x + (x) / 2, 10*x),(200 +15*x + (x) / 2, 11*x),(200 + 13*x,13*x),(200 +15*x + (x) / 2, 13*x)]
 
greenArr1 = [(200 - (3*x) / 2, x),(200 - (3*x) / 2, 2*x),(200 - (3*x) / 2, 3*x),(200 - (3*x) / 2, 4*x)]
yellowArr1 = [(200 +15*x + x/ 2, x),(200 +15*x+ (x) / 2, 2*x),(200 +15*x+ (x) / 2, 3*x), (200 +15*x+ (x) / 2, 4*x)]
redArr1 = [(200 - (3*x) / 2, 13*x),(200 - (3*x) / 2, 10*x),(200 +15*x + (x) / 2, 12*x),(200 - (3*x) / 2, 12*x)]
blueArr1 = [(200 +15*x + (x) / 2, 10*x),(200 +15*x + (x) / 2, 11*x),(200 + 13*x,13*x),(200 +15*x + (x) / 2, 13*x)]


leaveList = []
d = (0,"None")
  
   
logList = []

numberOfPlayers = 4

wonList = []

Exit = 0
def main():
     
     global FPSCLOCK, displaySurf, BASICFONT, x, fullBoard, greenBox, yellowBox, blueBox, redBox, mainboard, moves, d, newboard, second, namePlayer, wonList, logList, leaveList
     

     pygame.init()
     FPSCLOCK = pygame.time.Clock()
     displaySurf = pygame.display.set_mode((windowWidth,windowHeight))
     pygame.display.set_caption('      LUDO                                               STUPEFY CORPORATIONS')

     BASICFONT = pygame.font.Font('freesansbold.ttf', basicfontsize)
     
     pygame.mixer.music.load('ludo.mp3')
     pygame.mixer.music.play(0)

     opening()
     
     second = secondWindow()
     
     numberOfPlayers, mode = thirdWindow()
     
     if mode == "offline":
          namePlayer1 = nameWindow("1")
          namePlayer2 = nameWindow("2")
          namePlayer3 = nameWindow("3")
          namePlayer4 = nameWindow("4")
          #iconPlayer1 = iconWindow(1)
          #iconPlayer2 = iconWindow(2)
          #iconPlayer3 = iconWindow(3)
          #iconPlayer4 = iconWindow(4)
          namePlayer = [namePlayer1,namePlayer2, namePlayer3,namePlayer4]
          #iconPlayer = [iconPlayer1, iconPlayer2, iconPlayer3, iconPlayer4]


     #thirdWindow()

     #numberOfPlayers = selectNumberOfPlayer()
     if numberOfPlayers == 4:
           k = 1
     elif numberOfPlayers == 2:
           k = 2
           mainboard = []
           for i in newboard:
                if i[2] == 'GREEN' or i[2] == 'BLUE':
                     mainboard.append(i)
                     #newboard.remove(i)
           newboard = []
           for i in mainboard:
                newboard.append(i)









     img1 = pygame.image.load('grey.jpg')
     displaySurf.blit(img1,(0,0))
     img1 = pygame.image.load('home.png')
     displaySurf.blit(img1,(440,240))

     
     
     
     #newboard = mainboard
     player = 0
     moves = 0
     Exit = 0
     while True:
          

          player = revisedPlayer(k,player)

          drawboard(player)
          drawDice(moves, player)
		
          drawLine(moves, player)
		
          if player == None:
               wonAnimation()
          if Exit == 1:
               pygame.quit()
               sys.exit()
          ifquit()
          
          #moves = 1
          color = getColor(player)
          if moves > 0 and checkNoMove(moves, color):
               logListUpdate("P"+str(player+1), moves,0)
               time = pygame.time.get_ticks() + 1000
               while time >= pygame.time.get_ticks():
                    drawDice(moves,player)
                    pygame.display.update()
               moves = 0
               player = (player + k) % 4
               
               
          else :
          	for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                             
               	     spotx, spoty = event.pos[0], event.pos[1]
               	     centerx, centery = getCenter(spotx, spoty)
               	   
               	     if (centerx, centery) != (None, None) and Valid(centerx, centery, color, moves) :
               	        
                        
               	          if isValid(centerx, centery, moves, color) :
               	              drawHighlightBox(centerx, centery, moves, color)
                              
                         

                    if event.type == MOUSEBUTTONUP:
               	     spotx, spoty = event.pos[0], event.pos[1]
               	     centerx, centery = getCenter(spotx, spoty)
               	     if ifleave(centerx,centery):
                              performLeave(player)
                              player = (player + k) % 4
                              moves = 0 
             #            elif ifexit(centerx,centery):
             #                Exit = 1
             # elif ifreset(centerx,centery):
             #     performReset()
               	     elif (centerx, centery) != (None, None) and Valid( centerx, centery, color, moves):
               	          if isValid(centerx, centery, moves, color) :
               	              
               	               
               	              if moves == 0:
               	                    pygame.mixer.music.load('dice2.WAV')
               	                    pygame.mixer.music.play(0)
               	                    moves = getRandom()
               	              else : 
                                        logListUpdate("P"+str(player+1), moves,1)
                                        newx, newy = getNew(centerx, centery, moves, color)
                                        if (newx, newy) != (None, None):
               	                         shiftAnimation(newx, newy ,color)
               	                         mainboard.append((newx, newy, color))
               	                         if (newx == 200+x or newx == 200+4*x or newx == 200+10*x or newx == 200+13*x) and (newy == x or newy == 4*x or newy == 10*x or newy == 13*x):
               	                                 pygame.mixer.music.load('splat.mp3')
               	                                 pygame.mixer.music.play(0)
               	                         else :
               	                                 pygame.mixer.music.load('button.mp3')
               	                                 pygame.mixer.music.play(0)
                                             mainboard.remove((centerx,centery,color))
                                             player = (player+k)%4
                                             moves = 0
               	     	
                    	
                     
                 	
          pygame.display.update()
          FPSCLOCK.tick(FPS)




def ifexit(centerx,centery):
     if (centerx == 40) and (centery == 640) : 
          return True

     return False
     
def ifleave(centerx,centery):
     if (centerx == 1040 or centerx == 1080 or centerx == 1120) and (centery == 640) : 
          return True

     return False



def ifreset(centerx,centery):
     if (centerx == 1040 or centerx == 1080 or centerx == 1120) and (centery == 680) : 
          return True

     return False


def performLeave(player):
     if player == 0:
          leaveList.append(1)
          for tup in mainboard:
               if tup[2] == 'GREEN':
                    mainboard.remove(tup)
          for tup in greenDead:
               
               tup[0] = 1
          for tup in greenBox:
               
               tup[0] = 0
          greenArr = []
     if player == 0:
          leaveList.append(2)
          for tup in mainboard:
               if tup[2] == 'YELLOW':
                    mainboard.remove(tup)
          for tup in yellowDead:
               
               tup[0] = 1
          for tup in yellowBox:
               
               tup[0] = 0
          yellowArr = []
     if player == 2:
          leaveList.append(3)
          for tup in mainboard:
               if tup[2] == 'BLUE':
                    mainboard.remove(tup)
          for tup in blueDead:
               
               tup[0] = 1
          for tup in blueBox:
               
               tup[0] = 0
          blueArr = []
     if player == 3:
          leaveList.append(4)
          for tup in mainboard:
               if tup[2] == 'RED':
                    mainboard.remove(tup)
          for tup in redDead:
               
               tup[0] = 1
          for tup in redBox:
               
               tup[0] = 0
          redArr = []
    

def performReset():
     mainboard = [(200 + x, x,'GREEN'),(200 + 4*x,x,'GREEN'),(200 + x,4*x,'GREEN'),(200 + 4*x,4*x,'GREEN'),(200 + 10*x,x,'YELLOW'),(200 + 13*x,x,'YELLOW'),(200 + 10*x,4*x,'YELLOW'),(200+13*x,4*x,'YELLOW'),(200 + 10*x,10*x,'BLUE'),(200 + 10*x,13*x,'BLUE'),(200 + 13*x,10*x,'BLUE'), (200 + 13*x,13*x,'BLUE'),(200 + x, 10*x,'RED'),(200 + 4*x,10*x,'RED'),(200 + 4*x,13*x,'RED'),(200+x,13*x,'RED')]


     greenBox = [(1,200 + x,x),(1,200 + 4*x,x),(1,200 + x,4*x),(1,200+4*x,4*x)]
     yellowBox = [(1,200 + 10*x,x),(1,200 + 13*x,x),(1,200 + 10*x,4*x), (1,200 + 13*x,4*x)]
     redBox = [(1,200 + x, 10*x),(1,200 + 4*x,10*x),(1,200 + x,13*x),(1,200+ 4*x,13*x)]
     blueBox = [(1,200 + 10*x,10*x),(1,200 + 13*x,10*x),(1,200 + 13*x,13*x),(1,200 + 10*x,13*x)]

  
     greenDead = [(0,200 - (3*x) / 2, x),(0,200 - (3*x) / 2, 2*x),(0,200 - (3*x) / 2, 3*x),(0,200 - (3*x) / 2, 4*x)]
     yellowDead = [(0,200 +15*x + x/ 2, x),(0,200 +15*x+ (x) / 2, 2*x),(0,200 +15*x+ (x) / 2, 3*x), (0,200 +15*x+ (x) / 2, 4*x)]
     redDead = [(0,200 - (3*x) / 2, 13*x),(0,200 - (3*x) / 2, 10*x),(0,200 +15*x + (x) / 2, 12*x),(0,200 - (3*x) / 2, 12*x)]
     blueDead = [(0,200 +15*x + (x) / 2, 10*x),(0,200 +15*x + (x) / 2, 11*x),(0,200 + 13*x,13*x),(0,200 +15*x + (x) / 2, 13*x)]

     newboard = [(200 + x, x,'GREEN'),(200 + 4*x,x,'GREEN'),(200 + x,4*x,'GREEN'),(200 + 4*x,4*x,'GREEN'),(200 + 10*x,x,'YELLOW'),(200 + 13*x,x,'YELLOW'),(200 + 10*x,4*x,'YELLOW'),(200+13*x,4*x,'YELLOW'),(200 + 10*x,10*x,'BLUE'),(200 + 10*x,13*x,'BLUE'),(200 + 13*x,10*x,'BLUE'), (200 + 13*x,13*x,'BLUE'),(200 + x, 10*x,'RED'),(200 + 4*x,10*x,'RED'),(200 + 4*x,13*x,'RED'),(200+x,13*x,'RED')]


     greenArr = [(200 - (3*x) / 2, x),(200 - (3*x) / 2, 2*x),(200 - (3*x) / 2, 3*x),(200 - (3*x) / 2, 4*x)]
     yellowArr = [(200 +15*x + x/ 2, x),(200 +15*x+ (x) / 2, 2*x),(200 +15*x+ (x) / 2, 3*x), (200 +15*x+ (x) / 2, 4*x)]
     redArr = [(200 - (3*x) / 2, 13*x),(200 - (3*x) / 2, 10*x),(200 +15*x + (x) / 2, 12*x),(200 - (3*x) / 2, 12*x)]
     blueArr = [(200 +15*x + (x) / 2, 10*x),(200 +15*x + (x) / 2, 11*x),(200 + 13*x,13*x),(200 +15*x + (x) / 2, 13*x)]
 
     greenArr1 = [(200 - (3*x) / 2, x),(200 - (3*x) / 2, 2*x),(200 - (3*x) / 2, 3*x),(200 - (3*x) / 2, 4*x)]
     yellowArr1 = [(200 +15*x + x/ 2, x),(200 +15*x+ (x) / 2, 2*x),(200 +15*x+ (x) / 2, 3*x), (200 +15*x+ (x) / 2, 4*x)]
     redArr1 = [(200 - (3*x) / 2, 13*x),(200 - (3*x) / 2, 10*x),(200 +15*x + (x) / 2, 12*x),(200 - (3*x) / 2, 12*x)]
     blueArr1 = [(200 +15*x + (x) / 2, 10*x),(200 +15*x + (x) / 2, 11*x),(200 + 13*x,13*x),(200 +15*x + (x) / 2, 13*x)]


     leaveList = []
     d = (0,"None")
  
   
     logList = []

     player = 0
     moves = 0

     wonList = []


def logListUpdate(playerName, moves,isMoved):
     if len(logList) == 14:
          for i in range(13):
               logList[i] = logList[i+1]
          logList[13] = (playerName, moves, isMoved)
     else:
          logList.append((playerName, moves, isMoved))



def maketext(text, color, backcolor, top, left):
     textsurf = BASICFONT.render(text, True, color, backcolor)
     textrect = textsurf.get_rect()
     textrect.topleft = (top, left)
     return (textsurf, textrect)


def drawNameWindow(player,strng):
     displaySurf.fill(forthWindowColor)
     textsurf, textrect = maketext("PLAYER" + player + "   ENTER NAME", BLACK, forthWindowColor, 350+120, 100)
     displaySurf.blit(textsurf, textrect)

     #pygame.draw.rect(displaySurf, WHITE, (350, 350, 200, 50))
     textsurf, textrect = maketext(strng, BLACK, WHITE, 450+120, 350)
     displaySurf.blit(textsurf, textrect)


def nameWindow(player):
     strng = ""
     drawNameWindow(player,strng)
     while True:
        ifquit()
        drawNameWindow(player,strng)
        for event in pygame.event.get():
         if event.type == KEYUP:
          if event.key == K_a:
               strng += "A"
          elif event.key == K_b:
               strng += "B"
          elif event.key == K_c:
               strng += "C"
          elif event.key == K_d:
               strng += "D"
          elif event.key == K_e:
               strng += "E"
          elif event.key == K_f:
               strng += "F"
          elif event.key == K_g:
               strng += "G"
          elif event.key == K_h:
               strng += "H"
          elif event.key == K_i:
               strng += "I"
          elif event.key == K_j:
               strng += "J"
          elif event.key == K_k:
               strng += "K"
          elif event.key == K_l:
               strng += "L"
          elif event.key == K_m:
               strng += "M"
          elif event.key == K_n:
               strng += "N"
          elif event.key == K_o:
               strng += "O"
          elif event.key == K_p:
               strng += "P"
          elif event.key == K_q:
               strng += "Q"
          elif event.key == K_r:
               strng += "R"
          elif event.key == K_s:
               strng += "S"
          elif event.key == K_t:
               strng += "T"
          elif event.key == K_u:
               strng += "U"
          elif event.key == K_v:
               strng += "V"
          elif event.key == K_w:
               strng += "W"
          elif event.key == K_x:
               strng += "X"
          elif event.key == K_y:
               strng += "Y"
          elif event.key == K_z:
               strng += "Z"
          elif event.key == K_SPACE:
               if strng != "" :
                    return strng
          elif event.key == K_BACKSPACE:
               strng = strng[0:len(strng)-1]


        pygame.display.update()



    
     

     
     
     
def revisedPlayer(k,player):
     for i in range(4):
         if player == 0 and greenArr == []:
              player = (player+k)%4
         elif player == 1 and yellowArr == []:
              player = (player+k)%4
         elif player == 2 and blueArr == []:
              player = (player + k ) %4
         elif player == 3 and redArr == []:
              player = (player + k) % 4
         else :
              return player

     return None 




def checkNoMove(moves, color):
	
     for tup in mainboard:
          if tup[2] == color and isValid(tup[0], tup[1], moves, tup[2]):
               #pygame.draw.rect(displaySurf,BLACK,(tup[0],tup[1],x,x))
               #pygame.display.update()
               return False
          	
     return True




def drawLine(moves, player):
     if moves == 0 and player == 0:
          pygame.draw.line(displaySurf, BLACK, (10, 5*x+10), (10+100,5*x+10),8)
     elif moves == 0 and player == 1:
          pygame.draw.line(displaySurf, BLACK, (890,5*x+10), (890+100,5*x+10),8)
     elif moves == 0 and player == 2:
          pygame.draw.line(displaySurf, BLACK, (890,5*x+10+9*x), (890+100,5*x+10+9*x),8)
     elif moves == 0 and player == 3:
          pygame.draw.line(displaySurf, BLACK, (10,5*x+10+9*x), (10+100,5*x+10+9*x),8)
	



def shiftDead(color):
     if color == 'GREEN':
          for tup in greenDead:
                 if i[0] == 0:
                      greenDead.append((1,i[1],i[2]))
                      greenDead.remove((0,i[1],i[2]))
                      return (i[1], i[2])
     if color == 'YELLOW':
          for tup in yellowDead:
                 if i[0] == 0:
                      yellowDead.append((1,i[1],i[2]))
                      yellowDead.remove((0,i[1],i[2]))
                      return (i[1], i[2])
     if color == 'BLUE':
          for tup in blueDead:
                 if i[0] == 0:
                      blueDead.append((1,i[1],i[2]))
                      blueDead.remove((0,i[1],i[2]))
                      return (i[1], i[2])
     if color == 'RED':
          for tup in redDead:
                 if i[0] == 0:
                      redDead.append((1,i[1],i[2]))
                      redDead.remove((0,i[1],i[2]))
                      return (i[1], i[2])
                      
     return (None, None) 

def shiftAnimation(newx, newy, color):
     for tup in mainboard:
          if tup[0] == newx and tup[1] == newy and tup[2] != color:
               lol1, lol2 = findEmpty(tup[2])
               mainboard.append((lol1,lol2,tup[2]))
               mainboard.remove((newx,newy,tup[2]))

               return
     return

     
def findEmpty(color):
     if color == 'GREEN':
          for i in greenBox:
               if i[0] == 0:
                    greenBox.remove((0,i[1],i[2]))
                    greenBox.append((1,i[1],i[2]))
                    return (i[1], i[2])
     if color == 'YELLOW':
          for i in yellowBox:
               if i[0] == 0:
                    yellowBox.remove((0,i[1],i[2]))
                    yellowBox.append((1,i[1],i[2]))
                    return (i[1], i[2])
     if color == 'RED':
          for i in redBox:
               if i[0] == 0:
                    redBox.remove((0,i[1],i[2]))
                    redBox.append((1,i[1],i[2]))
                    return (i[1], i[2])
     if color == 'BLUE':
          for i in blueBox:
               if i[0] == 0:
                    blueBox.remove((0,i[1],i[2]))
                    blueBox.append((1,i[1],i[2]))
                    return (i[1], i[2])
     return (None,None)





def drawHighlightBox(boxx, boxy, moves , color):
     
     if moves > 0:
     	pygame.draw.circle(displaySurf, HilightColor, (boxx+20,boxy+20),23, 4)


def getNew(a, b, moves, color):
     

     
     if a < 440 and b == 7*x and color == 'GREEN':
          if a + moves*x < 440:
                return (a + moves*x, 7*x)
          elif a+moves*x == 440:
                for tup in greenArr:
                     greenArr.remove(tup)
                     if greenArr == []:
                          wonList.append(1)
                     return (tup[0],tup[1])
          else:
                return (None, None)
 
     elif a == 440 + x and b < 6*x and color == 'YELLOW':
          if b + moves*x < 6*x:
                return (a, b + moves*x)
          elif b +moves*x == 6*x :
                for tup in yellowArr:
                     
                     yellowArr.remove(tup)
                     if yellowArr == []:
                          wonList.append(2)
                     return (tup[0],tup[1])
          else:
                return (None, None)

     elif a >= 440 + 3*x and b == 7*x and color == 'BLUE':
          if a - moves*x >= 440+3*x:
                return (a - moves*x, 7*x)
          elif a - moves*x == 440 + 2*x:
                for tup in blueArr:
                     blueArr.remove(tup)
                     if blueArr == []:
                          wonList.append(3)
                     return (tup[0],tup[1])
          else:
                return (None, None)
   
     elif a == 440+x and b >= 9*x and color == 'RED':
          if b - moves*x >= 9*x:
                return (a, b-moves*x)
          elif b - moves*x == 8*x:
                for tup in redArr:
                     redArr.remove(tup)
                     if redArr == []:
                          wonList.append(4)
                     return (tup[0],tup[1])
          else:
                return (None, None)




     elif b == 240 and a < 440:
          if a + x*moves > 400:
               return getNew(440, 5*x, moves - (400 - a)/x - 1, color)
          else:
               return (a + x*moves, 240)

     elif a == 440 and b < 240:
          if b - x*moves < 0:
               return getNew(440 + x,0 , moves - (b)/x - 1, color)
          else:
               return (440, b - moves*x)

     elif a == 440 + x and b == 0:
          if moves > 0:
               return getNew(440 + 2*x, 0, moves - 1, color)
          else:
               return (a, b)

     elif a == 440 + 2*x and b < 240:
          if b + x*moves > 200:
               return getNew(440 + 3*x, 240, moves - (200 - b)/x - 1, color)
          else:
               return (a, b + x*moves)
    
     elif a >= 440 + 3*x and b == 240:
          if a + x*moves > 760:
               return getNew(200 + 14*x, 240+x, moves - (760 - a)/x - 1, color)
          else:
               return (a + x*moves, b)
     
     
     elif a == 200 + 14*x and b == 240+x:
          if moves > 0:
               return getNew(a, 240 + 2*x, moves - 1, color)
          else:
               return (a, b)
 

     elif b == 240+2*x and a >= 440 + 3*x:
          if a - x*moves < 440 + 3*x:
               return getNew(440 + 2*x, 9*x, moves - (a - 440 - 3*x)/x - 1, color)
          else:
               return (a - x*moves, 240 + 2*x)

     elif a == 440 + 2*x and b >= 9*x:
          if b + x*moves > 14*x:
               return getNew(a-x, 14*x, moves - (14*x - b)/x - 1, color)
          else:
               return (a, b + x*moves)

     elif a == 440 + x and b == 14*x:
          if moves > 0:
               return getNew(a-x, 14*x, moves - 1, color)
          else:
               return (a, b)

     elif a == 440 and b >= 9*x:
          if b - moves*x < 9*x:
               return getNew(a - x, 240 + 2*x, moves - ( b - 9*x) / x - 1, color)
          else:
               return (a, b - moves*x)

     
     elif b == 240+2*x and a < 440:
          if a - x*moves < 200:
               return getNew(200, 7*x, moves - (a - 200)/x - 1, color)
          else:
               return (a - x*moves, 240 + 2*x)

     elif a == 200 and b == 7*x:
          if moves > 0:
               return getNew(200, 6*x, moves - 1, color)
          else:
               return (a, b)

     else:
          for tup in newboard:
               if tup[0] == a and tup[1] == b and tup[2] == color:
                    checkHome(a,b,color)
                    return findOpen(color)
     

  
def checkHome(a, b, color):
     if color == 'GREEN':
          for i in greenBox:
               #pygame.draw.rect(displaySurf, WHITE, (a,b,40,40))
               #pygame.time.wait(500)
               #pygame.draw.rect(displaySurf, RED, (i[0],i[0],40,40))
               #pygame.time.wait(1000)
               if i[0] == 1 and i[1] == a and i[2] == b:
                    #pygame.draw.rect(displaySurf, WHITE, (a,b,40,40))
                    greenBox.remove((1,i[1],i[2]))
                    greenBox.append((0,i[1],i[2]))

     elif color == 'YELLOW':
          for i in yellowBox:
               if i[0] == 1 and i[1] == a and i[2] == b:
                    yellowBox.remove((1,i[1],i[2]))
                    yellowBox.append((0,i[1],i[2]))
     elif color == 'RED':
          for i in redBox:
               if i[0] == 1 and i[1] == a and i[2] == b:
                    redBox.remove((1,i[1],i[2]))
                    redBox.append((0,i[1],i[2]))
     elif color == 'BLUE':
          for i in blueBox:
               if i[0] == 1 and i[1] == a and i[2] == b:
                    blueBox.remove((1,i[1],i[2]))
                    blueBox.append((0,i[1],i[2]))


 
           
def findOpen(color):
     if color == 'GREEN':
    
          return (240,240)
     elif color == 'YELLOW':
          return (440+2*x,40)

     elif color == 'BLUE':
          return (200 + 13*x, 240+2*x)
     else:
          return (440, 13*x)


def isValid(a, b, moves, color):
     if moves == 0:
          return True
     elif moves > 0:
          for tup in newboard:
               if tup[0] == a and tup[1] == b and tup[2] == color and moves != 1:
                    #pygame.draw.rect(displaySurf,WHITE,(tup[0],tup[1],x,x))
                    #pygame.display.update()
                    return False

          if color == 'GREEN' and ((a < 440 and b == (240+x)  and ((440 - a)/40) < moves) or ((a,b) in greenArr1)):
               return False

          elif color == 'YELLOW' and ((b < 240 and a == (440+x) and ((240 - b)/40) < moves) or ((a,b) in yellowArr1)):
               return False

          elif color == 'BLUE' and ((a >= 200 + 9*x and b == (240+x) and ((a - (200+8*x))/40) < moves) or ((a,b) in blueArr1)):
               return False

          elif color == 'RED' and ((b >= 9*x and a == (440+x) and ((b - (240+2*x))/40) < moves) or ((a,b) in redArr1)):
               return False

          else:
               return True


def Valid(a,b,color, moves):
     if moves == 0 and color == 'GREEN' and ((a,b) == (0, 160) or (a,b) == (40, 160) or (a,b) == (80, 160)):
     	return True
     elif moves == 0 and color == 'YELLOW' and ((a,b) == (880, 160) or (a,b) == (920, 160) or (a,b) == (960, 160)):
          return True
     elif moves == 0 and color == 'BLUE' and ((a,b) == (880, 520) or (a,b) == (920, 520) or (a,b) == (960, 520)):  
          return True
     elif moves == 0 and color == 'RED' and ((a,b) == (0, 520) or (a,b) == (40, 520) or (a,b) == (80, 520)):
          return True
     elif moves > 0:
     	for tup in mainboard:
          	if tup[0] == a and tup[1] == b and tup[2] == color:
          	     return True

     return False


def getCenter(a, b):
     for i in range(0,1000,40):
          for j in range(0, 600, 40):
               tilerect = pygame.Rect(i, j, 40, 40)
               if tilerect.collidepoint(a,b):
                    return (i,j)

     return (None, None)


     
def ifquit():
     for event in pygame.event.get(QUIT):
          pygame.quit()
          sys.exit()
     for event in pygame.event.get(KEYUP):
          if event.key == K_ESCAPE:
               pygame.quit()
               sys.exit()
          pygame.event.post(event)


def getRandom():
     return random.randint(1,6)


def getColor(player):
     if player == 0:
          return 'GREEN'
     elif player == 1:
          return 'YELLOW'
     elif player == 2:
          return 'BLUE'
     elif player == 3:
          return 'RED'


def drawboard(player):
     img1 = pygame.image.load('grey.jpg')
     displaySurf.blit(img1,(0,0))
     img1 = pygame.image.load('home.png')
     displaySurf.blit(img1,(440,240))

     drawOuterRect()

     drawInnerRect()
     drawGrids()
	    #drawDice() 	     
     #drawCoins()
     drawDeadCoins()
     drawCoins()
     drawLowerRect()
     for i in range(4):
          if i == 0:
               textsurf, textrect = maketext(namePlayer[i], WHITE, GREEN,200 , 0)
               displaySurf.blit(textsurf, textrect)
          elif i == 1:
               textsurf, textrect = maketext(namePlayer[i], WHITE, YELLOW,560 , 0)
               displaySurf.blit(textsurf, textrect)
          elif i == 2:
               textsurf, textrect = maketext(namePlayer[i], WHITE, BLUE,560 , 360)
               displaySurf.blit(textsurf, textrect)
          elif i == 3:
               textsurf, textrect = maketext(namePlayer[i], WHITE, RED,200 , 360)
               displaySurf.blit(textsurf, textrect)

     pygame.draw.rect(displaySurf, BLACK, (1000, 0, 200, 600))
     textsurf, textrect = maketext("MOVE LOGS", WHITE, BLACK, 1040, 20)
     displaySurf.blit(textsurf, textrect)

     drawLogs()
     #pygame.draw.rect(displaySurf, WHITE, (200, 0, 600, 600), 8)
     #pygame.draw.rect(displaySurf, BLACK, (206, 6, 588, 588), 2)
     pygame.display.update()

  
  

def drawLowerRect():
     pygame.draw.rect(displaySurf, BLACK, (0,600, 1200, 150))
     img1 = pygame.image.load('exit.png')
     displaySurf.blit(img1,(40,640))

     img1 = pygame.image.load('leave.png')
     displaySurf.blit(img1,(1040,640))

     img1 = pygame.image.load('reset.png')
     displaySurf.blit(img1,(1040,680))
     
     
     
 

def drawLogs():
     cnt = 40
     for tup in logList:
          textsurf, textrect = maketext(tup[0], WHITE, BLACK, 1000, cnt)
          displaySurf.blit(textsurf, textrect)
          textsurf, textrect = maketext(str(tup[1]), WHITE, BLACK, 1000+2*x, cnt)
          displaySurf.blit(textsurf, textrect) 
          #textsurf, textrect = maketext(str(tup[2]), WHITE, BLACK, 1000+4*x, cnt)
          #displaySurf.blit(textsurf, textrect)
          if tup[2] == 0:
               img1 = pygame.image.load('cross.png')
               displaySurf.blit(img1,(1000+4*x, cnt)) 
          else:
               if tup[0] == "P1":
                    img1 = pygame.image.load('green.png')
                    displaySurf.blit(img1,(1000+4*x, cnt))
               elif tup[0] == "P2":
                    img1 = pygame.image.load('yellow.png')
                    displaySurf.blit(img1,(1000+4*x, cnt)) 
               elif tup[0] == "P3":
                    img1 = pygame.image.load('blue.png')
                    displaySurf.blit(img1,(1000+4*x, cnt)) 
               elif tup[0] == "P4":
                    img1 = pygame.image.load('red.png')
                    displaySurf.blit(img1,(1000+4*x, cnt))   
          cnt = cnt + 40

        
def drawDeadCoins():
     pygame.draw.rect(displaySurf, LIGHTGREEN, (200 - (3*x) / 2, x, 40, 40))
     pygame.draw.rect(displaySurf, GREEN, (200 - (3*x) / 2, 2*x, 40, 40))
     pygame.draw.rect(displaySurf, LIGHTGREEN, (200 - (3*x) / 2, 3*x, 40, 40))
     pygame.draw.rect(displaySurf, GREEN, (200 - (3*x) / 2, 4*x, 40, 40))
     pygame.draw.rect(displaySurf, LIGHTYELLOW, (200 +15*x + x/ 2, x, 40, 40))
     pygame.draw.rect(displaySurf, YELLOW, (200 +15*x+ (x) / 2, 2*x, 40, 40))
     pygame.draw.rect(displaySurf, LIGHTYELLOW, (200 +15*x+ (x) / 2, 3*x, 40, 40))
     pygame.draw.rect(displaySurf, YELLOW, (200 +15*x+ (x) / 2, 4*x, 40, 40))
     pygame.draw.rect(displaySurf, RED, (200 - (3*x) / 2, 13*x, 40, 40))
     pygame.draw.rect(displaySurf, LIGHTRED, (200 - (3*x) / 2, 10*x, 40, 40))
     pygame.draw.rect(displaySurf, RED, (200 - (3*x) / 2, 11*x, 40, 40))
     pygame.draw.rect(displaySurf, LIGHTRED, (200 - (3*x) / 2, 12*x, 40, 40))
     pygame.draw.rect(displaySurf, LIGHTBLUE, (200 +15*x + (x) / 2, 10*x, 40, 40))
     pygame.draw.rect(displaySurf, BLUE, (200 +15*x + (x) / 2, 11*x, 40, 40))
     pygame.draw.rect(displaySurf, LIGHTBLUE, (200 +15*x + (x) / 2, 12*x, 40, 40))
     pygame.draw.rect(displaySurf, BLUE, (200 +15*x + (x) / 2, 13*x, 40, 40))
    

     
def drawOuterRect():
     pygame.draw.rect(displaySurf, GREEN, (200, 0, 240, 240))
     pygame.draw.rect(displaySurf, YELLOW, (560, 0, 240, 240))
     pygame.draw.rect(displaySurf, BLUE, (560,360, 240, 240))
     pygame.draw.rect(displaySurf, RED, (200,360, 240, 240))


def drawInnerRect():
     
     #GREEN
     pygame.draw.rect(displaySurf, LIGHTGREEN, (200 + x,   x, 160, 160))
 
     #YELLOW
     pygame.draw.rect(displaySurf, LIGHTYELLOW, (200 + 10*x,   x, 160, 160))
     
     #BLUE
     pygame.draw.rect(displaySurf, LIGHTBLUE, (200 + 10*x, 10*x, 160, 160))
          
     #RED
     pygame.draw.rect(displaySurf, LIGHTRED, (200 + x,   10*x, 160, 160))
     
     
     #BLACK BORDERS
     
     
     img1 = pygame.image.load('down.png')
     displaySurf.blit(img1,(240 , 200))
     
     img1 = pygame.image.load('left.png')
     displaySurf.blit(img1,(560 , 40))
     
     img1 = pygame.image.load('up.png')
     displaySurf.blit(img1,(720, 360))
     
     img1 = pygame.image.load('right.png')
     displaySurf.blit(img1,(400, 520))
     
     pygame.draw.rect(displaySurf, BLACK, (200-80,0,80,600))
     pygame.draw.rect(displaySurf, BLACK, (800,0,80,600))
     
     #img1 = pygame.image.load('button_leave.png')
     #displaySurf.blit(img1,(5, 120))
     img1 = pygame.image.load('green_roll.png')
     displaySurf.blit(img1,(10, 160))
     
     #img1 = pygame.image.load('button_leave.png')
     #displaySurf.blit(img1,(885, 120))
     img1 = pygame.image.load('yellow_roll.png')
     displaySurf.blit(img1,(890, 160))
     
     #img1 = pygame.image.load('button_leave.png')
     #displaySurf.blit(img1,(5, 480))
     img1 = pygame.image.load('red_roll.png')
     displaySurf.blit(img1,(10, 520))
     
     #img1 = pygame.image.load('button_leave.png')
     #displaySurf.blit(img1,(885, 480))
     img1 = pygame.image.load('blue_roll.png')
     displaySurf.blit(img1,(890, 520))
     
     img1 = pygame.image.load('1.png')
     displaySurf.blit(img1,(280 , 80))
     
     img1 = pygame.image.load('2.png')
     displaySurf.blit(img1,(640 , 80))
     
     img1 = pygame.image.load('4.png')
     displaySurf.blit(img1,(280, 440))
     
     img1 = pygame.image.load('3.png')
     displaySurf.blit(img1,(640, 440))



def drawGrids():
     cnt = 0

     fullBoard = []
     for i in range(200,440,40):
          if cnt%2 == 0:
               pygame.draw.rect(displaySurf, WHITE, (i,240,40,40))
               #fullBoard.append(i,240,'WHITE')
          else:
               pygame.draw.rect(displaySurf, GREY, (i,240,40,40))
               #fullBoard.append(i,240,'GREY')

          cnt = cnt+1
     pygame.draw.rect(displaySurf,LIGHTGREEN,(200+40, 240, 40,40))
    # fullBoard.append(280,240,'LIGHTGREEN')
     cnt = 0

     for i in range(200,440,40):
          if cnt == 0:
               pygame.draw.rect(displaySurf, GREY, (i,280,40,40))
               #fullBoard.append(i,280,'GREY')
          elif cnt%2 == 0:
               
               pygame.draw.rect(displaySurf, LIGHTGREEN, (i,280,40,40))
               #fullBoard.append(i,280,'LIGHTGREEN')
          elif cnt%2 != 0:
               
               pygame.draw.rect(displaySurf, GREEN, (i,280,40,40))
               #fullBoard.append(i,280,'GREEN')
          cnt = cnt+1

     cnt = 0

     for i in range(200,440,40):
          if cnt%2 == 0:
               pygame.draw.rect(displaySurf, WHITE, (i,320,40,40))
               #fullBoard.append(i,320,'WHITE')
          else:
               pygame.draw.rect(displaySurf, GREY, (i,320,40,40))
               #fullBoard.append(i,320,'GREY')

          cnt = cnt+1

     
     cnt = 0

     for i in range(0,240,40):
          if cnt%2 == 0:
               pygame.draw.rect(displaySurf, WHITE, (440,i,40,40))
               #fullBoard.append(440,i,'WHITE')
          else:
               pygame.draw.rect(displaySurf, GREY, (440,i,40,40))
               #fullBoard.append(440,i,'GREY')

          cnt = cnt+1
     
     cnt = 0

     for i in range(0,240,40):
          if cnt == 0:
               pygame.draw.rect(displaySurf, GREY, (440+40,i,40,40))
               #fullBoard[440+40][i] = 'GREY'
          elif cnt%2 != 0:
               pygame.draw.rect(displaySurf, YELLOW, (440+40,i,40,40))
               #fullBoard[440+40][i] = 'YELLOW'
          elif cnt%2 == 0:
               pygame.draw.rect(displaySurf, LIGHTYELLOW, (440+40,i,40,40))
               #fullBoard[440+40][i] = 'LIGHTYELLOW'

          cnt = cnt+1

     cnt = 0

     for i in range(0,240,40):
          if cnt%2 == 0:
               pygame.draw.rect(displaySurf, WHITE, (440+80,i,40,40))
               #fullBoard[440+80][i] = 'WHITE'
          else:
               pygame.draw.rect(displaySurf, GREY, (440+80,i,40,40))
               #fullBoard[440+80][i] = 'GREY'

          cnt = cnt+1

     pygame.draw.rect(displaySurf,LIGHTYELLOW,(440+80, 40, 40,40))
     #fullBoard[440+80][40] = 'LIGHTYELLOW'
     cnt = 0

     for i in range(360,600,40):
          if cnt%2 == 0:
               pygame.draw.rect(displaySurf, GREY, (440,i,40,40))
               #fullBoard[440][i] = 'GREY'
          else:
               pygame.draw.rect(displaySurf, WHITE, (440,i,40,40))
               #fullBoard[440][i] = 'WHITE'

          cnt = cnt+1
     pygame.draw.rect(displaySurf,LIGHTRED,(440,520, 40,40))
    # fullBoard[440][520] = 'LIGHTRED'
     cnt = 0

     for i in range(360,600,40):
          if cnt == 5:
               pygame.draw.rect(displaySurf, GREY, (440+40,i,40,40))
               #fullBoard[440+40][i] = 'GREY'
          elif cnt % 2 == 0:
               pygame.draw.rect(displaySurf, RED, (440+40,i,40,40))
               #fullBoard[440+40][i] = 'RED'
          elif cnt % 2 != 0:
               pygame.draw.rect(displaySurf, LIGHTRED, (440+40,i,40,40))
               #fullBoard[440+40][i] = 'LIGHTRED'
          cnt = cnt+1

     cnt = 0

     for i in range(360,600,40):
          if cnt%2 == 0:
               pygame.draw.rect(displaySurf, GREY, (440+80,i,40,40))
               #fullBoard[440+80][i] = 'GREY'
          else:
               pygame.draw.rect(displaySurf, WHITE, (440+80,i,40,40))
               #fullBoard[440+80][i] = 'WHITE'

          cnt = cnt+1


     cnt = 0

     for i in range(560,800,40):
          if cnt%2 == 0:
               pygame.draw.rect(displaySurf, GREY, (i,240,40,40))
               #fullBoard[i][240] = 'GREY'
          else:
               pygame.draw.rect(displaySurf, WHITE, (i,240,40,40))
               #fullBoard[i][240] = 'WHITE'

          cnt = cnt+1
     
     cnt = 0

     for i in range(560,800,40):
          if cnt == 5:
               pygame.draw.rect(displaySurf, GREY, (i,240+40,40,40))
               #fullBoard[i][240+40] = 'GREY'
          elif cnt%2 == 0:
               pygame.draw.rect(displaySurf, BLUE, (i,240+40,40,40))
               #fullBoard[i][240+40] = 'BLUE'
          elif cnt%2 != 0:
               pygame.draw.rect(displaySurf, LIGHTBLUE, (i,240+40,40,40))
               #fullBoard[i][240+40] = 'LIGHTBLUE'
          cnt = cnt+1

     cnt = 0

     for i in range(560,800,40):
          if cnt%2 == 0:
               pygame.draw.rect(displaySurf, GREY, (i,240+80,40,40))
               #fullBoard[i][240+80] = 'GREY'
          else:
               pygame.draw.rect(displaySurf, WHITE, (i,240+80,40,40))
               #fullBoard[i][240+80] = 'WHITE'

          cnt = cnt+1

     pygame.draw.rect(displaySurf,LIGHTBLUE,(720,240+80, 40,40))
     #fullBoard[720][240+80] = 'LIGHTBLUE'




def drawCoins():
     for tup in mainboard:
          if tup[2] == 'RED':
               img1 = pygame.image.load('red.png')
               displaySurf.blit(img1,(tup[0],tup[1]))
          elif tup[2] == 'GREEN':
               img1 = pygame.image.load('green.png')
               displaySurf.blit(img1,(tup[0],tup[1]))
          elif tup[2] == 'YELLOW':
               img1 = pygame.image.load('yellow.png')
               displaySurf.blit(img1,(tup[0],tup[1]))
          else:
               img1 = pygame.image.load('blue.png')
               displaySurf.blit(img1,(tup[0],tup[1]))
          #pygame.draw.circle(displaySurf,clr, (tup[0],tup[1]),20,0)

def drawDice(moves,player):

     
         
     if player == 0:
         if moves == 1:
             img1 = pygame.image.load('dice1.png')
             displaySurf.blit(img1,(20,20))
         if moves == 2:
             img1 = pygame.image.load('dice2.png')
             displaySurf.blit(img1,(20,20))
         if moves == 3:
             img1 = pygame.image.load('dice3.png')
             displaySurf.blit(img1,(20,20))
         if moves == 4:
             img1 = pygame.image.load('dice4.png')
             displaySurf.blit(img1,(20,20))
         if moves == 5:
             img1 = pygame.image.load('dice5.png')
             displaySurf.blit(img1,(20,20))
         if moves == 6:
             img1 = pygame.image.load('dice6.png')
             displaySurf.blit(img1,(20,20)) 
            
             
     if player == 1:
         if moves == 1:
             img1 = pygame.image.load('dice1.png')
             displaySurf.blit(img1,(900,20))         
         if moves == 2:
             img1 = pygame.image.load('dice2.png')
             displaySurf.blit(img1,(900,20))
         if moves == 3:
             img1 = pygame.image.load('dice3.png')
             displaySurf.blit(img1,(900,20))
         if moves == 4:
             img1 = pygame.image.load('dice4.png')
             displaySurf.blit(img1,(900,20))
         if moves == 5:
             img1 = pygame.image.load('dice5.png')
             displaySurf.blit(img1,(900,20))
         if moves == 6:
             img1 = pygame.image.load('dice6.png')
             displaySurf.blit(img1,(900,20)) 

     if player == 2:
         if moves == 1:
             img1 = pygame.image.load('dice1.png')
             displaySurf.blit(img1,(900,380))         
         if moves == 2:
             img1 = pygame.image.load('dice2.png')
             displaySurf.blit(img1,(900,380))
         if moves == 3:
             img1 = pygame.image.load('dice3.png')
             displaySurf.blit(img1,(900,380))
         if moves == 4:
             img1 = pygame.image.load('dice4.png')
             displaySurf.blit(img1,(900,380))
         if moves == 5:
             img1 = pygame.image.load('dice5.png')
             displaySurf.blit(img1,(900,380))
         if moves == 6:
             img1 = pygame.image.load('dice6.png')
             displaySurf.blit(img1,(900,380)) 
     if player == 3:
         if moves == 1:
             img1 = pygame.image.load('dice1.png')
             displaySurf.blit(img1,(20,380))         
         if moves == 2:
             img1 = pygame.image.load('dice2.png')
             displaySurf.blit(img1,(20,380))
         if moves == 3:
             img1 = pygame.image.load('dice3.png')
             displaySurf.blit(img1,(20,380))
         if moves == 4:
             img1 = pygame.image.load('dice4.png')
             displaySurf.blit(img1,(20,380))
         if moves == 5:
             img1 = pygame.image.load('dice5.png')
             displaySurf.blit(img1,(20,380))
         if moves == 6:
             img1 = pygame.image.load('dice6.png')
             displaySurf.blit(img1,(20,380)) 

          


def opening():

       displaySurf.fill(openBgColor)
       
       arr = []
       cnt = 0
       for i in range(0, windowWidth+1, 100):
            for j in range(0, windowHeight+1, 100):
                 arr.append([i,j])
                 cnt += 1
       colors = []

       for i in range(100):
            a1 = random.randint(0,255)
            a2 = random.randint(0,255)
            a3 = random.randint(0,255)
            colors.append([a1,a2,a3])
       
       
       for i in range(cnt):
            
            color = random.choice(colors)
            left, top = random.choice(arr)  
            arr.remove([left,top])   
            pygame.draw.rect(displaySurf, color, (left, top, 100, 100))
            pygame.display.update()
            pygame.time.wait(30)
       
       img1 = pygame.image.load('ludo.png')
       displaySurf.blit(img1,(340+120,250))
     
       pygame.display.update()
       pygame.time.wait(2000)


    


def secondWindow():
     
     displaySurf.fill(BLACK) 
     img1 = pygame.image.load('rules.png')
     displaySurf.blit(img1,(335,0))
     
     while True:
          displaySurf.fill(DARKTURQUOISE) 
          
          img1 = pygame.image.load('rules.png')
          displaySurf.blit(img1,(335,0))
          
          img1 = pygame.image.load('agree.png')
          displaySurf.blit(img1,(529,540))
          ifquit()
          #pygame.display.update()
	     
          for event in pygame.event.get():
               if event.type == MOUSEBUTTONUP:
                   spotx, spoty = event.pos[0], event.pos[1]
                   centerx, centery = getCenter(spotx, spoty)
                   pygame.draw.rect(displaySurf, WHITE, (centerx,centery,40,40))
                   pygame.display.update()
                   if (centerx == 520 or centerx == 560 or centerx == 600) and (centery == 520 or centery == 560) :
                        return 1
                    
          pygame.display.update()




def thirdWindow():
     displaySurf.fill(BLACK)
     img1 = pygame.image.load('start1.jpg')
     displaySurf.blit(img1,(320, 0))
    
     selection = 0

     while True:
          displaySurf.fill(BLACK)
          
          img1 = pygame.image.load('start1.jpg')
          displaySurf.blit(img1,(320, 0))
          ifquit()
          pygame.display.update()
         
          for event in pygame.event.get():
               if event.type == MOUSEMOTION:

                    spotx, spoty = event.pos[0], event.pos[1]
                    centerx, centery = getCenter(spotx, spoty)
                    pygame.draw.rect(displaySurf, RED, (spotx-10,spoty-10,10,10))
                    pygame.display.update()
                    if (centerx >= 560 and centerx <= 690) :
                        
                         
                         if (centery >= 190 and centery <= 236) :
                              pygame.draw.line(displaySurf, BLACK, (560, 256), (690, 256),8)

                         elif (centery >= 270 and centery <= 312) :
                              pygame.draw.line(displaySurf, BLACK, (440+120, 332), (570+120, 332),8)
                                            
                         #elif (centery >= 440 and centery <= 520) :
                          #    pygame.draw.line(displaySurf, WHITE, (440, 520), (560, 520),8)
                    pygame.display.update()

               elif event.type == MOUSEBUTTONUP:
                    spotx, spoty = event.pos[0], event.pos[1]
                    centerx, centery = getCenter(spotx, spoty)
                   
                    if (centerx >= 440+120 and centerx <= 570+120) :
                        
                              
                         if (centery >= 210 and centery <= 256) :
                              selection = 2
                              pygame.draw.line(displaySurf, WHITE, (440+120, 256), (570+120, 256),8)
                                   

                         elif (centery >= 290 and centery <= 332) :
                              selection = 4
                              pygame.draw.line(displaySurf, WHITE, (440+120, 332), (570+120, 332),8)
                                   

                              
                   
                         elif (centerx >= 440+120 and centerx <= 570+120 and selection != 0) :
                                        
                              return (selection , "offline")
                         pygame.display.update()



def wonAnimation():
     displaySurf.fill(forthWindowColor)
     cnt = 0
     for i in wonList:
          cnt = cnt + 1
          textsurf, textrect = maketext(str(cnt) + ".   " + namePlayer[i], BLACK, forthWindowColor, 350, 100)
          displaySurf.blit(textsurf, textrect)
     
     for i in reversed(leaveList):

          cnt = cnt + 1
          textsurf, textrect = maketext(str(cnt) + ".   " + namePlayer[i], BLACK, forthWindowColor, 350, 100)
          displaySurf.blit(textsurf, textrect)
     pyagme.display.update()
     pygame.time.wait(5000)


if __name__ == '__main__':
       main()


















                    
