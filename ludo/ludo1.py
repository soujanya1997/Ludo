#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame
import sys
from pygame.locals import *

FPS = 30
windowHeight = 750
windowWidth = 1200

boardWidth = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKGREY = (30, 30, 30)
DARKTURQUOISE = (3, 54, 73)
GREEN = (34, 139, 34)
LIGHTGREEN = (154, 205, 50)
RED = (178, 34, 34)
LIGHTRED = (205, 92, 92)
PURPLE = (255, 0, 255)
GREY = (205, 201, 201)
NEW = (3, 150, 100)
NORMALGREY = (105, 105, 105)
ORANGERED = (255, 69, 0)
MAROON = (176, 48, 96)
DEEPPINK = (255, 20, 147)
DARKVIOLET = (148, 0, 211)
LIGHTYELLOW = (255, 215, 0)
YELLOW = (255, 165, 0)
HOTPINK = (255, 105, 180)
PERU = (205, 133, 65)
BLUE = (0, 0, 128)
LIGHTBLUE = (0, 0, 205)

HilightColor = WHITE
openBgColor = WHITE
bgcolor = BLACK
bgColor = BLACK
forthWindowColor = DARKTURQUOISE
basicfontsize = 20
bigfontsize = 40
x = 40

greenAvatarCnt = 0
blueAvatarCnt = 0
yellowAvatarCnt = 0
redAvatarCnt = 0

mainboard = [
    (200 + x, x, 'GREEN'),
    (200 + 4 * x, x, 'GREEN'),
    (200 + x, 4 * x, 'GREEN'),
    (200 + 4 * x, 4 * x, 'GREEN'),
    (200 + 10 * x, x, 'YELLOW'),
    (200 + 13 * x, x, 'YELLOW'),
    (200 + 10 * x, 4 * x, 'YELLOW'),
    (200 + 13 * x, 4 * x, 'YELLOW'),
    (200 + 10 * x, 10 * x, 'BLUE'),
    (200 + 10 * x, 13 * x, 'BLUE'),
    (200 + 13 * x, 10 * x, 'BLUE'),
    (200 + 13 * x, 13 * x, 'BLUE'),
    (200 + x, 10 * x, 'RED'),
    (200 + 4 * x, 10 * x, 'RED'),
    (200 + 4 * x, 13 * x, 'RED'),
    (200 + x, 13 * x, 'RED'),
    ]

greenBox = [(1, 200 + x, x), (1, 200 + 4 * x, x), (1, 200 + x, 4 * x),
            (1, 200 + 4 * x, 4 * x)]
yellowBox = [(1, 200 + 10 * x, x), (1, 200 + 13 * x, x), (1, 200 + 10
             * x, 4 * x), (1, 200 + 13 * x, 4 * x)]
redBox = [(1, 200 + x, 10 * x), (1, 200 + 4 * x, 10 * x), (1, 200 + x,
          13 * x), (1, 200 + 4 * x, 13 * x)]
blueBox = [(1, 200 + 10 * x, 10 * x), (1, 200 + 13 * x, 10 * x), (1,
           200 + 13 * x, 13 * x), (1, 200 + 10 * x, 13 * x)]

greenDead = [(0, 200 - 3 * x / 2, x), (0, 200 - 3 * x / 2, 2 * x), (0,
             200 - 3 * x / 2, 3 * x), (0, 200 - 3 * x / 2, 4 * x)]
yellowDead = [(0, 200 + 15 * x + x / 2, x), (0, 200 + 15 * x + x / 2, 2
              * x), (0, 200 + 15 * x + x / 2, 3 * x), (0, 200 + 15 * x
              + x / 2, 4 * x)]
redDead = [(0, 200 - 3 * x / 2, 10 * x), (0, 200 - 3 * x / 2, 11 * x),
           (0, 200 - 3 * x / 2, 12 * x), (0, 200 - 3 * x / 2, 13
           * x)]
blueDead = [(0, 200 + 15 * x + x / 2, 10 * x), (0, 200 + 15 * x + x
            / 2, 11 * x), (0, 200 + 15 * x + x/2, 12 * x), (0, 200 + 15 * x
            + x / 2, 13 * x)]

newboard = [
    (200 + x, x, 'GREEN'),
    (200 + 4 * x, x, 'GREEN'),
    (200 + x, 4 * x, 'GREEN'),
    (200 + 4 * x, 4 * x, 'GREEN'),
    (200 + 10 * x, x, 'YELLOW'),
    (200 + 13 * x, x, 'YELLOW'),
    (200 + 10 * x, 4 * x, 'YELLOW'),
    (200 + 13 * x, 4 * x, 'YELLOW'),
    (200 + 10 * x, 10 * x, 'BLUE'),
    (200 + 10 * x, 13 * x, 'BLUE'),
    (200 + 13 * x, 10 * x, 'BLUE'),
    (200 + 13 * x, 13 * x, 'BLUE'),
    (200 + x, 10 * x, 'RED'),
    (200 + 4 * x, 10 * x, 'RED'),
    (200 + 4 * x, 13 * x, 'RED'),
    (200 + x, 13 * x, 'RED'),
    ]

greenArr = [(200 - 3 * x / 2, x), (200 - 3 * x / 2, 2 * x), (200 - 3
            * x / 2, 3 * x), (200 - 3 * x / 2, 4 * x)]
yellowArr = [(200 + 15 * x + x / 2, x), (200 + 15 * x + x / 2, 2 * x),
             (200 + 15 * x + x / 2, 3 * x), (200 + 15 * x + x / 2, 4
             * x)]
redArr = [(200 - 3 * x / 2, 10 * x), (200 - 3 * x / 2, 11 * x), (200 - 3 * x / 2, 12 * x), (200 - 3 * x / 2, 13 * x)]
blueArr = [(200 + 15 * x + x / 2, 10 * x), (200 + 15 * x + x / 2, 11
           * x), (200 + 15 * x + x/2, 12 * x), (200 + 15 * x + x / 2, 13 * x)]

greenArr1 = [(200 - 3 * x / 2, x), (200 - 3 * x / 2, 2 * x), (200 - 3
             * x / 2, 3 * x), (200 - 3 * x / 2, 4 * x)]
yellowArr1 = [(200 + 15 * x + x / 2, x), (200 + 15 * x + x / 2, 2 * x),
              (200 + 15 * x + x / 2, 3 * x), (200 + 15 * x + x / 2, 4
              * x)]
redArr1 = [(200 - 3 * x / 2, 10 * x), (200 - 3 * x / 2, 11 * x), (200 - 3 * x / 2, 12 * x), (200 - 3 * x / 2, 13 * x)]
blueArr1 = [(200 + 15 * x + x / 2, 10 * x), (200 + 15 * x + x / 2, 11
           * x), (200 + 15 * x + x/2, 12 * x), (200 + 15 * x + x / 2, 13 * x)]

leaveList = []
d = (0, 'None')

logList = []

numberOfPlayers = 4

wonList = []

Exit = 0
safePoints = [(200+x,240),(200+6*x,2*x),(200+8*x,x),(200+12*x, 6*x),(200+13*x,8*x),(200+8*x,12*x),(200+6*x,13*x),(200+2*x,8*x)]


score1 = 0
score2 = 0
score3 = 0
score4 = 0


def main():

    global FPSCLOCK, displaySurf, BASICFONT, x, fullBoard, greenBox, \
        yellowBox, blueBox, redBox, mainboard, moves, d, newboard, \
        second, namePlayer, wonList, logList, leaveList, greenDead, yellowDead, blueDead, redDead, greenArr, yellowArr, blueArr, redArr, Exit, avatar, scoreGreen, scoreYellow, scoreBlue, scoreRed , BASICFONT2

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    displaySurf = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('      LUDO                                               STUPEFY CORPORATIONS'
                               )

    BASICFONT = pygame.font.Font('freesansbold.ttf', basicfontsize)
    BASICFONT2 = pygame.font.Font('freesansbold.ttf', bigfontsize)
    pygame.mixer.music.load('ludo.mp3')
    pygame.mixer.music.play(0)

    opening()

    second = secondWindow()

    (numberOfPlayers, mode) = thirdWindow()

    if mode == 'offline' and numberOfPlayers == 4:
        namePlayer1, avatar1 = nameWindow('1')
        namePlayer2, avatar2 = nameWindow('2')
        namePlayer3, avatar3 = nameWindow('3')
        namePlayer4, avatar4 = nameWindow('4')

          # iconPlayer1 = iconWindow(1)
          # iconPlayer2 = iconWindow(2)
          # iconPlayer3 = iconWindow(3)
          # iconPlayer4 = iconWindow(4)

        namePlayer = [namePlayer1, namePlayer2, namePlayer3,
                      namePlayer4]
        avatar = [avatar1, avatar2, avatar3, avatar4]

    elif mode == 'offline' and numberOfPlayers == 2:
        namePlayer1, avatar1 = nameWindow('1')
        namePlayer2, avatar2 = nameWindow('2')
        #namePlayer3 = nameWindow('3')
        #namePlayer4 = nameWindow('4')

          # iconPlayer1 = iconWindow(1)
          # iconPlayer2 = iconWindow(2)
          # iconPlayer3 = iconWindow(3)
          # iconPlayer4 = iconWindow(4)

        namePlayer = [namePlayer1,"", namePlayer2,""]
        avatar = [avatar1,"", avatar2, ""]
          # iconPlayer = [iconPlayer1, iconPlayer2, iconPlayer3, iconPlayer4]

     # thirdWindow()

     # numberOfPlayers = selectNumberOfPlayer()

    if numberOfPlayers == 4:
        k = 1
    elif numberOfPlayers == 2:
        k = 2
        mainboard = []
        for i in newboard:
            if i[2] == 'GREEN' or i[2] == 'BLUE':
                mainboard.append(i)

                     # newboard.remove(i)

        newboard = []
        for i in mainboard:
            newboard.append(i)

    img1 = pygame.image.load('grey.jpg')
    displaySurf.blit(img1, (0, 0))
    img1 = pygame.image.load('home.png')
    displaySurf.blit(img1, (440, 240))

     # newboard = mainboard
    scoreGreen = 0
    scoreYellow = 0
    scoreBlue = 0
    scoreRed = 0
    player = 0
    moves = 0
    Exit = 0
    while True:

        player = revisedPlayer(k, player)

        drawboard(player)
        drawDice(moves, player)

        drawLine(moves, player)

        if player == None:
            wonAnimation()
            pygame.quit()
            sys.exit()

        ifquit()

          # moves = 1

        color = getColor(player)
        if moves > 0 and checkNoMove(moves, color):
            logListUpdate('P' + str(player + 1), moves, 0)
            time = pygame.time.get_ticks() + 1000
            while time >= pygame.time.get_ticks():
                drawDice(moves, player)
                pygame.display.update()
            moves = 0
            player = (player + k) % 4
        else:

            for event in pygame.event.get():
                if event.type == MOUSEMOTION:

                    (spotx, spoty) = (event.pos[0], event.pos[1])
                    (centerx, centery) = getCenter(spotx, spoty)

                    if (centerx, centery) != (None, None) \
                        and Valid(centerx, centery, color, moves):

                        if isValid(centerx, centery, moves, color):
                            drawHighlightBox(centerx, centery, moves,
                                    color)

                if event.type == MOUSEBUTTONUP:
                    (spotx, spoty) = (event.pos[0], event.pos[1])
                    (centerx, centery) = getCenter(spotx, spoty)
                    if ifleave(centerx, centery):
                        pygame.mixer.music.load('button.mp3')
                        pygame.mixer.music.play(0)
                        pygame.draw.rect(displaySurf, WHITE,(1040,640,120,40),4)
                        performLeave(player)
                        player = (player + k) % 4
                        moves = 0
                    elif ifreset(centerx, centery):
                        pygame.mixer.music.load('button.mp3')
                        pygame.mixer.music.play(0)
                        pygame.draw.rect(displaySurf, WHITE,(1040,680,120,40),4)
                        player, moves = performReset()
                        
                    elif (centerx, centery) != (None, None) \
                        and Valid(centerx, centery, color, moves):

             #            elif ifexit(centerx,centery):
             #                Exit = 1
             # elif ifreset(centerx,centery):
             #     performReset()

                        if isValid(centerx, centery, moves, color):

                            if moves == 0:
                                pygame.mixer.music.load('dice2.WAV')
                                pygame.mixer.music.play(0)
                                moves = getRandom()
                            else:
                                logListUpdate('P' + str(player + 1),
                                        moves, 1)
                                (newx, newy) = getNew(centerx, centery,
                                        moves, color)
                                if (newx, newy) != (None, None):
                                    shiftAnimation(newx, newy, color)
                                    mainboard.append((newx, newy,
        color))
                                    if (newx == 200 + x or newx == 200
        + 4 * x or newx == 200 + 10 * x or newx == 200 + 13 * x) \
    and (newy == x or newy == 4 * x or newy == 10 * x or newy == 13
         * x):
                                        pygame.mixer.music.load('splat.mp3'
        )
                                        pygame.mixer.music.play(0)
                                    else:
                                        pygame.mixer.music.load('button.mp3'
        )
                                        pygame.mixer.music.play(0)
                                    mainboard.remove((centerx, centery,
        color))
                                    player = (player + k) % 4
                                    moves = 0

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def ifexit(centerx, centery):
    if centerx == 40 and centery == 640:
        return True

    return False


def ifleave(centerx, centery):
    if (centerx == 1040 or centerx == 1080 or centerx == 1120) \
        and centery == 640:
        return True

    return False


def ifreset(centerx, centery):
    if (centerx == 1040 or centerx == 1080 or centerx == 1120) \
        and centery == 680:
        return True

    return False


def performLeave(player):
    if player == 0:
        leaveList.append(1)
        board = []
        for tup in mainboard:
            if tup[2] == 'GREEN':
                print tup[0]
                print tup[1]
                print tup[2] 
                board.append(tup)
        for tup in board:
            mainboard.remove(tup)
        for tup in greenDead:
            mainboard.append((tup[1],tup[2],'GREEN'))
        board1 = []
        for tup in greenDead:
            board1.append(tup)
        for tup in board1:
            greenDead.remove(tup)
            greenDead.append((1,tup[1],tup[2]))
        board2 = []
        for tup in greenBox:
            board2.append(tup)
        for tup in board2:
            greenBox.remove(tup)
            greenBox.append((0,tup[1],tup[2]))
        board3 = []
        for tup in greenArr:
            board3.append(tup)
        for tup in board3:
            greenArr.remove(tup)
            

    if player == 1:
        leaveList.append(2)
        board = []
        for tup in mainboard:
            if tup[2] == 'YELLOW':
                print tup[0]
                print tup[1]
                print tup[2] 
                board.append(tup)
        for tup in board:
            mainboard.remove(tup)
        for tup in yellowDead:
            mainboard.append((tup[1],tup[2],'YELLOW'))
        board1 = []
        for tup in yellowDead:
            board1.append(tup)
        for tup in board1:
            yellowDead.remove(tup)
            yellowDead.append((1,tup[1],tup[2]))
        board2 = []
        for tup in yellowBox:
            board2.append(tup)
        for tup in board2:
            yellowBox.remove(tup)
            yellowBox.append((0,tup[1],tup[2]))
        board3 = []
        for tup in yellowArr:
            board3.append(tup)
        for tup in board3:
            yellowArr.remove(tup)
    if player == 2:
        leaveList.append(3)
        board = []
        for tup in mainboard:
            if tup[2] == 'BLUE':
                print tup[0]
                print tup[1]
                print tup[2] 
                board.append(tup)
        for tup in board:
            mainboard.remove(tup)
        for tup in blueDead:
            mainboard.append((tup[1],tup[2],'BLUE'))
        board1 = []
        for tup in blueDead:
            board1.append(tup)
        for tup in board1:
            blueDead.remove(tup)
            blueDead.append((1,tup[1],tup[2]))
        board2 = []
        for tup in blueBox:
            board2.append(tup)
        for tup in board2:
            blueBox.remove(tup)
            blueBox.append((0,tup[1],tup[2]))
        board3 = []
        for tup in blueArr:
            board3.append(tup)
        for tup in board3:
            blueArr.remove(tup)
    if player == 3:
        leaveList.append(4)
        board = []
        for tup in mainboard:
            if tup[2] == 'RED':
                print tup[0]
                print tup[1]
                print tup[2] 
                board.append(tup)
        for tup in board:
            mainboard.remove(tup)
        for tup in redDead:
            mainboard.append((tup[1],tup[2],'RED'))
        board1 = []
        for tup in redDead:
            board1.append(tup)
        for tup in board1:
            redDead.remove(tup)
            redDead.append((1,tup[1],tup[2]))
        board2 = []
        for tup in redBox:
            board2.append(tup)
        for tup in board2:
            redBox.remove(tup)
            redBox.append((0,tup[1],tup[2]))
        board3 = []
        for tup in redArr:
            board3.append(tup)
        for tup in board3:
            redArr.remove(tup)


def performReset():
    board1 = []
    '''
    for tup in mainboard:
         board1.append(tup)
    '''
    del mainboard[:]
    for tup in newboard:
         mainboard.append(tup)

    greenBox1 = [(1, 200 + x, x), (1, 200 + 4 * x, x), (1, 200 + x, 4
                * x), (1, 200 + 4 * x, 4 * x)]
    '''
    for tup in greenBox:
         del tup
    '''
    del greenBox[:]
    for tup in greenBox1:
         greenBox.append(tup)
    yellowBox1 = [(1, 200 + 10 * x, x), (1, 200 + 13 * x, x), (1, 200
                 + 10 * x, 4 * x), (1, 200 + 13 * x, 4 * x)]
    '''
    for tup in yellowBox:
         del tup
    '''
    del yellowBox[:]
    for tup in yellowBox1:
         yellowBox.append(tup)
    redBox1 = [(1, 200 + x, 10 * x), (1, 200 + 4 * x, 10 * x), (1, 200
              + x, 13 * x), (1, 200 + 4 * x, 13 * x)]
    '''
    for tup in redBox:
         del tup
    '''
    del redBox[:]
    for tup in redBox1:
         redBox.append(tup)
    blueBox1 = [(1, 200 + 10 * x, 10 * x), (1, 200 + 13 * x, 10 * x),
               (1, 200 + 13 * x, 13 * x), (1, 200 + 10 * x, 13 * x)]
    '''
    for tup in blueBox:
         del tup
    '''
    del blueBox[:]

    for tup in blueBox1:
         blueBox.append(tup)
    greenDead1 = [(0, 200 - 3 * x / 2, x), (0, 200 - 3 * x / 2, 2 * x),
                 (0, 200 - 3 * x / 2, 3 * x), (0, 200 - 3 * x / 2, 4
                 * x)]
    '''
    for tup in greenDead:
         del tup
    '''
    del greenDead[:]
    for tup in greenDead1:
         greenDead.append(tup)
    yellowDead1 = [(0, 200 + 15 * x + x / 2, x), (0, 200 + 15 * x + x
                  / 2, 2 * x), (0, 200 + 15 * x + x / 2, 3 * x), (0,
                  200 + 15 * x + x / 2, 4 * x)]
    '''
    for tup in yellowDead:
         del tup
    '''
    del yellowDead[:]
    for tup in yellowDead1:
         yellowDead.append(tup)
    redDead1 = [(0, 200 - 3 * x / 2, 10 * x), (0, 200 - 3 * x / 2, 11
               * x), (0, 200 - 3 * x / 2, 12 * x), (0, 200 - 3 * x
               / 2, 13 * x)]
    '''
    for tup in redDead:
         del tup
    '''
    del redDead[:]
    for tup in redDead1:
         redDead.append(tup)
    blueDead1 = [(0, 200 + 15 * x + x / 2, 10 * x), (0, 200 + 15 * x + x
                / 2, 11 * x), (0, 200 + 15 * x + x/2, 12 * x), (0, 200 + 15
                * x + x / 2, 13 * x)]
    '''
    for tup in blueDead:
         del tup
    '''
    del blueDead[:]

    for tup in blueDead1:
         blueDead.append(tup)
    

    greenArr2 = [(200 - 3 * x / 2, x), (200 - 3 * x / 2, 2 * x), (200
                - 3 * x / 2, 3 * x), (200 - 3 * x / 2, 4 * x)]
    '''
    for tup in greenArr:
         del tup
    '''
    del greenArr[:]
    for tup in greenArr2:
         greenArr.append(tup)
    yellowArr2 = [(200 + 15 * x + x / 2, x), (200 + 15 * x + x / 2, 2
                 * x), (200 + 15 * x + x / 2, 3 * x), (200 + 15 * x + x
                 / 2, 4 * x)]
    '''
    for tup in yellowArr:
         del tup
    '''
    del yellowArr[:]
    for tup in yellowArr2:
         yellowArr.append(tup)
    redArr2 = [(200 - 3 * x / 2, 10 * x), (200 - 3 * x / 2, 11 * x),
              (200 - 3 * x / 2, 12 * x), (200 - 3 * x / 2, 13 * x)]
    '''
    for tup in redArr:
         del tup
    '''
    del redArr[:]
    for tup in redArr2:
         redArr.append(tup)
    blueArr2 = [(200 + 15 * x + x / 2, 10 * x), (200 + 15 * x + x / 2,
               11 * x), (200 + 15 * x + x/2, 12 * x), (200 + 15 * x + x / 2,
               13 * x)]
    '''
    for tup in blueArr:
         del tup
    '''
    del blueArr[:]
    for tup in blueArr2:
         blueArr.append(tup)

    del leaveList[:]
    '''
    for tup in leaveList:
         del tup
    for tup in wonList:
         del tup
    for tup in logList:
         del tup
    '''
    del wonList[:]
    del logList[:]
    
    
    d = (0, 'None')

    
    player = 0
    moves = 0
    Exit = 0
    global scoreGreen, scoreYellow, scoreBlue, scoreRed
    scoreGreen = 0
    scoreYellow = 0
    scoreBlue = 0
    scoreRed = 0

    return (player, moves)


def logListUpdate(playerName, moves, isMoved):
    if len(logList) == 14:
        for i in range(13):
            logList[i] = logList[i + 1]
        logList[13] = (playerName, moves, isMoved)
    else:
        logList.append((playerName, moves, isMoved))


def maketext(
    text,
    color,
    backcolor,
    top,
    left,
    ):
    textsurf = BASICFONT.render(text, True, color, backcolor)
    textrect = textsurf.get_rect()
    textrect.topleft = (top, left)
    return (textsurf, textrect)

def maketext2(
    text,
    color,
    backcolor,
    top,
    left,
    ):
    textsurf = BASICFONT2.render(text, True, color, backcolor)
    textrect = textsurf.get_rect()
    textrect.topleft = (top, left)
    return (textsurf, textrect)


def drawNameWindow(player, strng):
    displaySurf.fill(forthWindowColor)
    (textsurf, textrect) = maketext2('PLAYER ' + player + '       ENTER NAME   &   SELECT AVATAR'
                                    , WHITE, forthWindowColor, 100, 100)
    displaySurf.blit(textsurf, textrect)
    (textsurf, textrect) = maketext2(strng, WHITE, BLACK, 150, 350)
    displaySurf.blit(textsurf, textrect)

    img1 = pygame.image.load('a1.png')
    displaySurf.blit(img1, (560+x, 200))

    img1 = pygame.image.load('a2.png')
    displaySurf.blit(img1, (560+4*x, 200))    

    img1 = pygame.image.load('a3.png')
    displaySurf.blit(img1, (560+7*x, 200))

    img1 = pygame.image.load('a4.png')
    displaySurf.blit(img1, (560+10*x, 200))

    img1 = pygame.image.load('a5.png')
    displaySurf.blit(img1, (560+x, 200+3*x))

    img1 = pygame.image.load('a6.png')
    displaySurf.blit(img1, (560+4*x, 200+3*x))    

    img1 = pygame.image.load('a7.png')
    displaySurf.blit(img1, (560+7*x, 200+3*x))

    img1 = pygame.image.load('a8.png')
    displaySurf.blit(img1, (560+10*x, 200+3*x))

    img1 = pygame.image.load('a9.png')
    displaySurf.blit(img1, (560+x, 200+6*x))

    img1 = pygame.image.load('a10.png')
    displaySurf.blit(img1, (560+4*x, 200+6*x))    

    img1 = pygame.image.load('a11.png')
    displaySurf.blit(img1, (560+7*x, 200+6*x))

    img1 = pygame.image.load('a12.png')
    displaySurf.blit(img1, (560+10*x, 200+6*x))


def getAvatarNumber(centerx, centery):
    ans  = 0
    if ((centerx == 560 + x or centerx == 560 + 2*x) and (centery == 200 or centery == 200 + x)):
        pygame.draw.rect(displaySurf, BLACK, (560+x, 200, 80, 80), 5)
        ans =  1
    elif ((centerx == 560 + 4*x or centerx == 560 + 5*x) and (centery == 200 or centery == 200 + x)):
        pygame.draw.rect(displaySurf, BLACK, (560+4*x, 200, 80, 80), 5)
        ans = 2
    elif ((centerx == 560 + 7*x or centerx == 560 + 8*x) and (centery == 200 or centery == 200 + x)):
        pygame.draw.rect(displaySurf, BLACK, (560+7*x, 200, 80, 80), 5)
        ans = 3
    elif ((centerx == 560 + 10*x or centerx == 560 + 11*x) and (centery == 200 or centery == 200 + x)):
        pygame.draw.rect(displaySurf, BLACK, (560+10*x, 200, 80, 80), 5)
        ans = 4
    elif ((centerx == 560 + x or centerx == 560 + 2*x) and (centery == 200 + 3*x or centery == 200 + 4*x)):
        pygame.draw.rect(displaySurf, BLACK, (560+x, 200+3*x, 80, 80), 5)
        ans = 5
    elif ((centerx == 560 + 4*x or centerx == 560 + 5*x) and (centery == 200 + 3*x or centery == 200 + 4*x)):
        pygame.draw.rect(displaySurf, BLACK, (560+4*x, 200+3*x, 80, 80), 5)
        ans = 6
    elif ((centerx == 560 + 7*x or centerx == 560 + 8*x) and (centery == 200 + 3*x or centery == 200 + 4*x)):
        pygame.draw.rect(displaySurf, BLACK, (560+7*x, 200+3*x, 80, 80), 5)
        ans = 7
    elif ((centerx == 560 + 10*x or centerx == 560 + 11*x) and (centery == 200 + 3*x or centery == 200 + 4*x)):
        pygame.draw.rect(displaySurf, BLACK, (560+10*x, 200+3*x, 80, 80), 5)
        ans = 8
    elif ((centerx == 560 + x or centerx == 560 + 2*x) and (centery == 200 + 7*x or centery == 200 + 6*x)):
        pygame.draw.rect(displaySurf, BLACK, (560+x, 200+6*x, 80, 80), 5)
        ans = 9
    elif ((centerx == 560 + 4*x or centerx == 560 + 5*x) and (centery == 200 + 7*x or centery == 200 + 6*x)):
        pygame.draw.rect(displaySurf, BLACK, (560+4*x, 200+6*x, 80, 80), 5)
        ans = 10
    elif ((centerx == 560 + 7*x or centerx == 560 + 8*x) and (centery == 200 + 7*x or centery == 200 + 6*x)):
        pygame.draw.rect(displaySurf, BLACK, (560+7*x, 200+6*x, 80, 80), 5)
        ans = 11
    elif ((centerx == 560 + 10*x or centerx == 560 + 11*x) and (centery == 200 + 7*x or centery == 200 + 6*x)):
        pygame.draw.rect(displaySurf, BLACK, (560+10*x, 200+6*x, 80, 80), 5)
        ans = 12

    print ans
    pygame.display.update()
    return ans 

def nameWindow(player):
    strng = ''
    drawNameWindow(player, strng)
    cnt1 = 0
    while True:
        
        drawNameWindow(player, strng)
        ifquit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                (spotx, spoty) = (event.pos[0], event.pos[1])
                (centerx, centery) = getCenter(spotx, spoty)
                avatarNumber = getAvatarNumber(centerx, centery)
                #pygame.display.update()
                if avatarNumber != 0:
                    pygame.mixer.music.load('button.mp3')
                    pygame.mixer.music.play(0)
                    cnt1 = 1
                else :
                    cnt1 = 0    
            elif event.type == KEYUP:
                l = len(strng)
                if event.key == K_a and l <10:
                    strng += 'A'
                elif event.key == K_b and l < 10:
                    strng += 'B'
                elif event.key == K_c and l <10:
                    strng += 'C'
                elif event.key == K_d and l <10:
                    strng += 'D'
                elif event.key == K_e and l <10:
                    strng += 'E'
                elif event.key == K_f and l <10:
                    strng += 'F'
                elif event.key == K_g and l <10:
                    strng += 'G'
                elif event.key == K_h and l <10:
                    strng += 'H'
                elif event.key == K_i and l <10: 
                    strng += 'I'
                elif event.key == K_j and l <10:
                    strng += 'J'
                elif event.key == K_k and l <10:
                    strng += 'K'
                elif event.key == K_l and l <10:
                    strng += 'L'
                elif event.key == K_m and l <10:
                    strng += 'M'
                elif event.key == K_n and l <10:
                    strng += 'N'
                elif event.key == K_o and l <10:
                    strng += 'O'
                elif event.key == K_p and l <10:
                    strng += 'P'
                elif event.key == K_q and l <10:
                    strng += 'Q'
                elif event.key == K_r and l <10:
                    strng += 'R'
                elif event.key == K_s and l <10:
                    strng += 'S'
                elif event.key == K_t and l <10:
                    strng += 'T'
                elif event.key == K_u and l <10:
                    strng += 'U'
                elif event.key == K_v and l <10:
                    strng += 'V'
                elif event.key == K_w and l <10:
                    strng += 'W'
                elif event.key == K_x and l <10:
                    strng += 'X'
                elif event.key == K_y and l <10:
                    strng += 'Y'
                elif event.key == K_z and l <10:
                    strng += 'Z'
                elif event.key == K_SPACE and l <= 10:
                    if strng != '' and cnt1 != 0:
                        return (strng, avatarNumber)
                elif event.key == K_BACKSPACE and l >= 0:
                    strng = strng[0:len(strng) - 1]

        pygame.display.update()


def revisedPlayer(k, player):
    for i in range(4):
        if player == 0 and greenArr == []:
            player = (player + k) % 4
        elif player == 1 and yellowArr == []:
            player = (player + k) % 4
        elif player == 2 and blueArr == []:
            player = (player + k) % 4
        elif player == 3 and redArr == []:
            player = (player + k) % 4
        else:
            return player

    return None


def checkNoMove(moves, color):

    for tup in mainboard:
        if tup[2] == color and isValid(tup[0], tup[1], moves, tup[2]):

               # pygame.draw.rect(displaySurf,BLACK,(tup[0],tup[1],x,x))
               # pygame.display.update()

            return False

    return True


def drawLine(moves, player):
    if moves == 0 and player == 0:
        pygame.draw.line(displaySurf, BLACK, (10, 5 * x + 10), (10
                         + 100, 5 * x + 10), 8)
    elif moves == 0 and player == 1:
        pygame.draw.line(displaySurf, BLACK, (890, 5 * x + 10), (890
                         + 100, 5 * x + 10), 8)
    elif moves == 0 and player == 2:
        pygame.draw.line(displaySurf, BLACK, (890, 5 * x + 10 + 9 * x),
                         (890 + 100, 5 * x + 10 + 9 * x), 8)
    elif moves == 0 and player == 3:
        pygame.draw.line(displaySurf, BLACK, (10, 5 * x + 10 + 9 * x),
                         (10 + 100, 5 * x + 10 + 9 * x), 8)


def shiftDead(color):
    if color == 'GREEN':
        for tup in greenDead:
            if i[0] == 0:
                greenDead.append((1, i[1], i[2]))
                greenDead.remove((0, i[1], i[2]))
                return (i[1], i[2])
    if color == 'YELLOW':
        for tup in yellowDead:
            if i[0] == 0:
                yellowDead.append((1, i[1], i[2]))
                yellowDead.remove((0, i[1], i[2]))
                return (i[1], i[2])
    if color == 'BLUE':
        for tup in blueDead:
            if i[0] == 0:
                blueDead.append((1, i[1], i[2]))
                blueDead.remove((0, i[1], i[2]))
                return (i[1], i[2])
    if color == 'RED':
        for tup in redDead:
            if i[0] == 0:
                redDead.append((1, i[1], i[2]))
                redDead.remove((0, i[1], i[2]))
                return (i[1], i[2])

    return (None, None)


def shiftAnimation(newx, newy, color):
    global scoreGreen, scoreYellow, scoreBlue, scoreRed
    for tup in mainboard:
        if tup[0] == newx and tup[1] == newy and tup[2] != color and ((tup[0],tup[1]) not in safePoints):
            if color == 'GREEN':
                 scoreGreen = scoreGreen + 1
            elif color == 'YELLOW':
                 scoreYellow = scoreYellow + 1
            elif color == 'BLUE':
                 scoreBlue = scoreBlue + 1
            elif color == 'RED':
                 scoreRed = scoreRed + 1
            if tup[2] == 'GREEN':
                 scoreGreen = scoreGreen - 1
            elif tup[2] == 'YELLOW':
                 scoreYellow = scoreYellow - 1
            elif tup[2] == 'BLUE':
                 scoreBlue = scoreBlue - 1
            if tup[2] == 'RED':
                 scoreRed = scoreRed - 1
  
            (lol1, lol2) = findEmpty(tup[2])
            mainboard.append((lol1, lol2, tup[2]))
            mainboard.remove((newx, newy, tup[2]))

            return
    return


def findEmpty(color):
    if color == 'GREEN':
        for i in greenBox:
            if i[0] == 0:
                greenBox.remove((0, i[1], i[2]))
                greenBox.append((1, i[1], i[2]))
                return (i[1], i[2])
    if color == 'YELLOW':
        for i in yellowBox:
            if i[0] == 0:
                yellowBox.remove((0, i[1], i[2]))
                yellowBox.append((1, i[1], i[2]))
                return (i[1], i[2])
    if color == 'RED':
        for i in redBox:
            if i[0] == 0:
                redBox.remove((0, i[1], i[2]))
                redBox.append((1, i[1], i[2]))
                return (i[1], i[2])
    if color == 'BLUE':
        for i in blueBox:
            if i[0] == 0:
                blueBox.remove((0, i[1], i[2]))
                blueBox.append((1, i[1], i[2]))
                return (i[1], i[2])
    return (None, None)


def drawHighlightBox(
    boxx,
    boxy,
    moves,
    color,
    ):

    if moves > 0:
        pygame.draw.circle(displaySurf, HilightColor, (boxx + 20, boxy
                           + 20), 23, 4)


def getNew(
    a,
    b,
    moves,
    color,
    ):

    if a < 440 and b == 7 * x and color == 'GREEN':
        if a + moves * x < 440:
            return (a + moves * x, 7 * x)
        elif a + moves * x == 440:
            for tup in greenArr:
                greenArr.remove(tup)
                if greenArr == []:
                    wonList.append(1)
                return (tup[0], tup[1])
        else:
            return (None, None)
    elif a == 440 + x and b < 6 * x and color == 'YELLOW':

        if b + moves * x < 6 * x:
            return (a, b + moves * x)
        elif b + moves * x == 6 * x:
            for tup in yellowArr:

                yellowArr.remove(tup)
                if yellowArr == []:
                    wonList.append(2)
                return (tup[0], tup[1])
        else:
            return (None, None)
    elif a >= 440 + 3 * x and b == 7 * x and color == 'BLUE':

        if a - moves * x >= 440 + 3 * x:
            return (a - moves * x, 7 * x)
        elif a - moves * x == 440 + 2 * x:
            for tup in blueArr:
                blueArr.remove(tup)
                if blueArr == []:
                    wonList.append(3)
                return (tup[0], tup[1])
        else:
            return (None, None)
    elif a == 440 + x and b >= 9 * x and color == 'RED':

        if b - moves * x >= 9 * x:
            return (a, b - moves * x)
        elif b - moves * x == 8 * x:
            for tup in redArr:
                redArr.remove(tup)
                if redArr == []:
                    wonList.append(4)
                return (tup[0], tup[1])
        else:
            return (None, None)
    elif b == 240 and a < 440:

        if a + x * moves > 400:
            return getNew(440, 5 * x, moves - (400 - a) / x - 1, color)
        else:
            return (a + x * moves, 240)
    elif a == 440 and b < 240:

        if b - x * moves < 0:
            return getNew(440 + x, 0, moves - b / x - 1, color)
        else:
            return (440, b - moves * x)
    elif a == 440 + x and b == 0:

        if moves > 0:
            return getNew(440 + 2 * x, 0, moves - 1, color)
        else:
            return (a, b)
    elif a == 440 + 2 * x and b < 240:

        if b + x * moves > 200:
            return getNew(440 + 3 * x, 240, moves - (200 - b) / x - 1,
                          color)
        else:
            return (a, b + x * moves)
    elif a >= 440 + 3 * x and b == 240:

        if a + x * moves > 760:
            return getNew(200 + 14 * x, 240 + x, moves - (760 - a) / x
                          - 1, color)
        else:
            return (a + x * moves, b)
    elif a == 200 + 14 * x and b == 240 + x:

        if moves > 0:
            return getNew(a, 240 + 2 * x, moves - 1, color)
        else:
            return (a, b)
    elif b == 240 + 2 * x and a >= 440 + 3 * x:

        if a - x * moves < 440 + 3 * x:
            return getNew(440 + 2 * x, 9 * x, moves - (a - 440 - 3 * x)
                          / x - 1, color)
        else:
            return (a - x * moves, 240 + 2 * x)
    elif a == 440 + 2 * x and b >= 9 * x:

        if b + x * moves > 14 * x:
            return getNew(a - x, 14 * x, moves - (14 * x - b) / x - 1,
                          color)
        else:
            return (a, b + x * moves)
    elif a == 440 + x and b == 14 * x:

        if moves > 0:
            return getNew(a - x, 14 * x, moves - 1, color)
        else:
            return (a, b)
    elif a == 440 and b >= 9 * x:

        if b - moves * x < 9 * x:
            return getNew(a - x, 240 + 2 * x, moves - (b - 9 * x) / x
                          - 1, color)
        else:
            return (a, b - moves * x)
    elif b == 240 + 2 * x and a < 440:

        if a - x * moves < 200:
            return getNew(200, 7 * x, moves - (a - 200) / x - 1, color)
        else:
            return (a - x * moves, 240 + 2 * x)
    elif a == 200 and b == 7 * x:

        if moves > 0:
            return getNew(200, 6 * x, moves - 1, color)
        else:
            return (a, b)
    else:

        for tup in newboard:
            if tup[0] == a and tup[1] == b and tup[2] == color:
                checkHome(a, b, color)
                return findOpen(color)


def checkHome(a, b, color):
    if color == 'GREEN':
        for i in greenBox:

               # pygame.draw.rect(displaySurf, WHITE, (a,b,40,40))
               # pygame.time.wait(500)
               # pygame.draw.rect(displaySurf, RED, (i[0],i[0],40,40))
               # pygame.time.wait(1000)

            if i[0] == 1 and i[1] == a and i[2] == b:

                    # pygame.draw.rect(displaySurf, WHITE, (a,b,40,40))

                greenBox.remove((1, i[1], i[2]))
                greenBox.append((0, i[1], i[2]))
    elif color == 'YELLOW':

        for i in yellowBox:
            if i[0] == 1 and i[1] == a and i[2] == b:
                yellowBox.remove((1, i[1], i[2]))
                yellowBox.append((0, i[1], i[2]))
    elif color == 'RED':
        for i in redBox:
            if i[0] == 1 and i[1] == a and i[2] == b:
                redBox.remove((1, i[1], i[2]))
                redBox.append((0, i[1], i[2]))
    elif color == 'BLUE':
        for i in blueBox:
            if i[0] == 1 and i[1] == a and i[2] == b:
                blueBox.remove((1, i[1], i[2]))
                blueBox.append((0, i[1], i[2]))


def findOpen(color):
    if color == 'GREEN':

        return (240, 240)
    elif color == 'YELLOW':
        return (440 + 2 * x, 40)
    elif color == 'BLUE':

        return (200 + 13 * x, 240 + 2 * x)
    else:
        return (440, 13 * x)


def isValid(
    a,
    b,
    moves,
    color,
    ):
    if moves == 0:
        return True
    elif moves > 0:
        for tup in newboard:
            if tup[0] == a and tup[1] == b and tup[2] == color \
                and moves != 1:

                    # pygame.draw.rect(displaySurf,WHITE,(tup[0],tup[1],x,x))
                    # pygame.display.update()

                return False

        if color == 'GREEN' and (a < 440 and b == 240 + x and (440 - a)
                                 / 40 < moves or (a, b) in greenArr1):
            return False
        elif color == 'YELLOW' and (b < 240 and a == 440 + x and (240
                                    - b) / 40 < moves or (a, b)
                                    in yellowArr1):

            return False
        elif color == 'BLUE' and (a >= 200 + 9 * x and b == 240 + x
                                  and (a - (200 + 8 * x)) / 40 < moves
                                  or (a, b) in blueArr1):

            return False
        elif color == 'RED' and (b >= 9 * x and a == 440 + x and (b
                                 - (240 + 2 * x)) / 40 < moves or (a,
                                 b) in redArr1):

            return False
        else:

            return True


def Valid(
    a,
    b,
    color,
    moves,
    ):
    if moves == 0 and color == 'GREEN' and ((a, b) == (0, 160) or (a,
            b) == (40, 160) or (a, b) == (80, 160)):
        return True
    elif moves == 0 and color == 'YELLOW' and ((a, b) == (880, 160)
            or (a, b) == (920, 160) or (a, b) == (960, 160)):
        return True
    elif moves == 0 and color == 'BLUE' and ((a, b) == (880, 520)
            or (a, b) == (920, 520) or (a, b) == (960, 520)):
        return True
    elif moves == 0 and color == 'RED' and ((a, b) == (0, 520) or (a,
            b) == (40, 520) or (a, b) == (80, 520)):
        return True
    elif moves > 0:
        for tup in mainboard:
            if tup[0] == a and tup[1] == b and tup[2] == color:
                return True

    return False


def getCenter(a, b):
    for i in range(0, 1200, 40):
        for j in range(0, 750, 40):
            tilerect = pygame.Rect(i, j, 40, 40)
            if tilerect.collidepoint(a, b):
                return (i, j)

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
    return random.randint(1, 6)


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
    displaySurf.blit(img1, (0, 0))
    img1 = pygame.image.load('home.png')
    displaySurf.blit(img1, (440, 240))

    drawOuterRect()

    drawInnerRect()
    drawGrids()
    drawSafeGrids()
        # drawDice() ....
     # drawCoins()

    drawDeadCoins()
    drawCoins()
    drawLowerRect()
    drawAvatar()
    #drawScore()
    for i in range(4):
        if i == 0:
            (textsurf, textrect) = maketext(namePlayer[i], WHITE,
                    GREEN, 200, 0)
            displaySurf.blit(textsurf, textrect)
        elif i == 1:
            (textsurf, textrect) = maketext(namePlayer[i], WHITE,
                    YELLOW, 560, 0)
            displaySurf.blit(textsurf, textrect)
        elif i == 2:
            (textsurf, textrect) = maketext(namePlayer[i], WHITE, BLUE,
                    560, 360)
            displaySurf.blit(textsurf, textrect)
        elif i == 3:
            (textsurf, textrect) = maketext(namePlayer[i], WHITE, RED,
                    200, 360)
            displaySurf.blit(textsurf, textrect)

    pygame.draw.rect(displaySurf, BLACK, (1000, 0, 200, 600))
    (textsurf, textrect) = maketext('MOVE LOGS', WHITE, BLACK, 1040, 20)
    displaySurf.blit(textsurf, textrect)

    drawLogs()

     # pygame.draw.rect(displaySurf, WHITE, (200, 0, 600, 600), 8)
     # pygame.draw.rect(displaySurf, BLACK, (206, 6, 588, 588), 2)

    pygame.display.update()


def drawAvatar():
    cnt = 40
    j = 1
    global scoreGreen, scoreYellow, scoreBlue, scoreRed
    for i in avatar:
        if i != "":
             img1 = pygame.image.load("avatar"+str(i)+".png")
             displaySurf.blit(img1, (cnt,640))
             if j == 1:
                 (textsurf, textrect) = maketext2(str(scoreGreen), WHITE,BLACK, cnt+3*x, 640)
                 displaySurf.blit(textsurf, textrect)
                 pygame.draw.line(displaySurf, GREEN, (cnt, 710), (cnt+160, 710), 8)
             elif j == 2:
                 (textsurf, textrect) = maketext2(str(scoreYellow), WHITE,BLACK, cnt+3*x, 640)
                 displaySurf.blit(textsurf, textrect)
                 pygame.draw.line(displaySurf, YELLOW, (cnt, 710), (cnt+160, 710), 8)
             elif j == 3:
                 (textsurf, textrect) = maketext2(str(scoreBlue), WHITE,BLACK, cnt+3*x, 640)
                 displaySurf.blit(textsurf, textrect)
                 pygame.draw.line(displaySurf, BLUE, (cnt, 710), (cnt+160, 710), 8)
             elif j == 4:
                 (textsurf, textrect) = maketext2(str(scoreRed), WHITE,BLACK, cnt+3*x, 640)
                 displaySurf.blit(textsurf, textrect)
                 pygame.draw.line(displaySurf, RED, (cnt, 710), (cnt+160, 710), 8) 
        cnt = cnt + 250 
        j = j+1    

def drawSafeGrids():
    for tup in safePoints:
        img1 = pygame.image.load('safe.png')
        displaySurf.blit(img1, (tup[0],tup[1]))
 
def drawLowerRect():
    pygame.draw.rect(displaySurf, BLACK, (0, 600, 1200, 150))

    img1 = pygame.image.load('leave.png')
    displaySurf.blit(img1, (1040, 640))

    img1 = pygame.image.load('reset.png')
    displaySurf.blit(img1, (1040, 680))


def drawLogs():
    cnt = 40
    for tup in logList:
        (textsurf, textrect) = maketext(tup[0], WHITE, BLACK, 1000, cnt)
        displaySurf.blit(textsurf, textrect)
        (textsurf, textrect) = maketext(str(tup[1]), WHITE, BLACK, 1000
                + 2 * x, cnt)
        displaySurf.blit(textsurf, textrect)

          # textsurf, textrect = maketext(str(tup[2]), WHITE, BLACK, 1000+4*x, cnt)
          # displaySurf.blit(textsurf, textrect)

        if tup[2] == 0:
            img1 = pygame.image.load('cross.png')
            displaySurf.blit(img1, (1000 + 4 * x, cnt))
        else:
            if tup[0] == 'P1':
                img1 = pygame.image.load('green.png')
                displaySurf.blit(img1, (1000 + 4 * x, cnt))
            elif tup[0] == 'P2':
                img1 = pygame.image.load('yellow.png')
                displaySurf.blit(img1, (1000 + 4 * x, cnt))
            elif tup[0] == 'P3':
                img1 = pygame.image.load('blue.png')
                displaySurf.blit(img1, (1000 + 4 * x, cnt))
            elif tup[0] == 'P4':
                img1 = pygame.image.load('red.png')
                displaySurf.blit(img1, (1000 + 4 * x, cnt))
        cnt = cnt + 40


def drawDeadCoins():
    pygame.draw.rect(displaySurf, LIGHTGREEN, (200 - 3 * x / 2, x, 40,
                     40))
    pygame.draw.rect(displaySurf, GREEN, (200 - 3 * x / 2, 2 * x, 40,
                     40))
    pygame.draw.rect(displaySurf, LIGHTGREEN, (200 - 3 * x / 2, 3 * x,
                     40, 40))
    pygame.draw.rect(displaySurf, GREEN, (200 - 3 * x / 2, 4 * x, 40,
                     40))
    pygame.draw.rect(displaySurf, LIGHTYELLOW, (200 + 15 * x + x / 2,
                     x, 40, 40))
    pygame.draw.rect(displaySurf, YELLOW, (200 + 15 * x + x / 2, 2 * x,
                     40, 40))
    pygame.draw.rect(displaySurf, LIGHTYELLOW, (200 + 15 * x + x / 2, 3
                     * x, 40, 40))
    pygame.draw.rect(displaySurf, YELLOW, (200 + 15 * x + x / 2, 4 * x,
                     40, 40))
    pygame.draw.rect(displaySurf, RED, (200 - 3 * x / 2, 13 * x, 40,
                     40))
    pygame.draw.rect(displaySurf, LIGHTRED, (200 - 3 * x / 2, 10 * x,
                     40, 40))
    pygame.draw.rect(displaySurf, RED, (200 - 3 * x / 2, 11 * x, 40,
                     40))
    pygame.draw.rect(displaySurf, LIGHTRED, (200 - 3 * x / 2, 12 * x,
                     40, 40))
    pygame.draw.rect(displaySurf, LIGHTBLUE, (200 + 15 * x + x / 2, 10
                     * x, 40, 40))
    pygame.draw.rect(displaySurf, BLUE, (200 + 15 * x + x / 2, 11 * x,
                     40, 40))
    pygame.draw.rect(displaySurf, LIGHTBLUE, (200 + 15 * x + x / 2, 12
                     * x, 40, 40))
    pygame.draw.rect(displaySurf, BLUE, (200 + 15 * x + x / 2, 13 * x,
                     40, 40))


def drawOuterRect():
    pygame.draw.rect(displaySurf, GREEN, (200, 0, 240, 240))
    pygame.draw.rect(displaySurf, YELLOW, (560, 0, 240, 240))
    pygame.draw.rect(displaySurf, BLUE, (560, 360, 240, 240))
    pygame.draw.rect(displaySurf, RED, (200, 360, 240, 240))


def drawInnerRect():

     # GREEN

    pygame.draw.rect(displaySurf, LIGHTGREEN, (200 + x, x, 160, 160))

     # YELLOW

    pygame.draw.rect(displaySurf, LIGHTYELLOW, (200 + 10 * x, x, 160,
                     160))

     # BLUE

    pygame.draw.rect(displaySurf, LIGHTBLUE, (200 + 10 * x, 10 * x,
                     160, 160))

     # RED

    pygame.draw.rect(displaySurf, LIGHTRED, (200 + x, 10 * x, 160, 160))

     # BLACK BORDERS

    img1 = pygame.image.load('down.png')
    displaySurf.blit(img1, (240, 200))

    img1 = pygame.image.load('left.png')
    displaySurf.blit(img1, (560, 40))

    img1 = pygame.image.load('up.png')
    displaySurf.blit(img1, (720, 360))

    img1 = pygame.image.load('right.png')
    displaySurf.blit(img1, (400, 520))

    pygame.draw.rect(displaySurf, BLACK, (200 - 80, 0, 80, 600))
    pygame.draw.rect(displaySurf, BLACK, (800, 0, 80, 600))

     # img1 = pygame.image.load('button_leave.png')
     # displaySurf.blit(img1,(5, 120))

    img1 = pygame.image.load('green_roll.png')
    displaySurf.blit(img1, (10, 160))

     # img1 = pygame.image.load('button_leave.png')
     # displaySurf.blit(img1,(885, 120))

    img1 = pygame.image.load('yellow_roll.png')
    displaySurf.blit(img1, (890, 160))

     # img1 = pygame.image.load('button_leave.png')
     # displaySurf.blit(img1,(5, 480))

    img1 = pygame.image.load('red_roll.png')
    displaySurf.blit(img1, (10, 520))

     # img1 = pygame.image.load('button_leave.png')
     # displaySurf.blit(img1,(885, 480))

    img1 = pygame.image.load('blue_roll.png')
    displaySurf.blit(img1, (890, 520))

    img1 = pygame.image.load('1.png')
    displaySurf.blit(img1, (280, 80))

    img1 = pygame.image.load('2.png')
    displaySurf.blit(img1, (640, 80))

    img1 = pygame.image.load('4.png')
    displaySurf.blit(img1, (280, 440))

    img1 = pygame.image.load('3.png')
    displaySurf.blit(img1, (640, 440))


def drawGrids():
    cnt = 0

    fullBoard = []
    for i in range(200, 440, 40):
        if cnt % 2 == 0:
            pygame.draw.rect(displaySurf, WHITE, (i, 240, 40, 40))
        else:

               # fullBoard.append(i,240,'WHITE')

            pygame.draw.rect(displaySurf, GREY, (i, 240, 40, 40))

               # fullBoard.append(i,240,'GREY')

        cnt = cnt + 1
    pygame.draw.rect(displaySurf, LIGHTGREEN, (200 + 40, 240, 40, 40))

    # fullBoard.append(280,240,'LIGHTGREEN')

    cnt = 0

    for i in range(200, 440, 40):
        if cnt == 0:
            pygame.draw.rect(displaySurf, GREY, (i, 280, 40, 40))
        elif cnt % 2 == 0:

               # fullBoard.append(i,280,'GREY')

            pygame.draw.rect(displaySurf, LIGHTGREEN, (i, 280, 40, 40))
        elif cnt % 2 != 0:

               # fullBoard.append(i,280,'LIGHTGREEN')

            pygame.draw.rect(displaySurf, GREEN, (i, 280, 40, 40))

               # fullBoard.append(i,280,'GREEN')

        cnt = cnt + 1

    cnt = 0

    for i in range(200, 440, 40):
        if cnt % 2 == 0:
            pygame.draw.rect(displaySurf, WHITE, (i, 320, 40, 40))
        else:

               # fullBoard.append(i,320,'WHITE')

            pygame.draw.rect(displaySurf, GREY, (i, 320, 40, 40))

               # fullBoard.append(i,320,'GREY')

        cnt = cnt + 1

    cnt = 0

    for i in range(0, 240, 40):
        if cnt % 2 == 0:
            pygame.draw.rect(displaySurf, WHITE, (440, i, 40, 40))
        else:

               # fullBoard.append(440,i,'WHITE')

            pygame.draw.rect(displaySurf, GREY, (440, i, 40, 40))

               # fullBoard.append(440,i,'GREY')

        cnt = cnt + 1

    cnt = 0

    for i in range(0, 240, 40):
        if cnt == 0:
            pygame.draw.rect(displaySurf, GREY, (440 + 40, i, 40, 40))
        elif cnt % 2 != 0:

               # fullBoard[440+40][i] = 'GREY'

            pygame.draw.rect(displaySurf, YELLOW, (440 + 40, i, 40, 40))
        elif cnt % 2 == 0:

               # fullBoard[440+40][i] = 'YELLOW'

            pygame.draw.rect(displaySurf, LIGHTYELLOW, (440 + 40, i,
                             40, 40))

               # fullBoard[440+40][i] = 'LIGHTYELLOW'

        cnt = cnt + 1

    cnt = 0

    for i in range(0, 240, 40):
        if cnt % 2 == 0:
            pygame.draw.rect(displaySurf, WHITE, (440 + 80, i, 40, 40))
        else:

               # fullBoard[440+80][i] = 'WHITE'

            pygame.draw.rect(displaySurf, GREY, (440 + 80, i, 40, 40))

               # fullBoard[440+80][i] = 'GREY'

        cnt = cnt + 1

    pygame.draw.rect(displaySurf, LIGHTYELLOW, (440 + 80, 40, 40, 40))

     # fullBoard[440+80][40] = 'LIGHTYELLOW'

    cnt = 0

    for i in range(360, 600, 40):
        if cnt % 2 == 0:
            pygame.draw.rect(displaySurf, GREY, (440, i, 40, 40))
        else:

               # fullBoard[440][i] = 'GREY'

            pygame.draw.rect(displaySurf, WHITE, (440, i, 40, 40))

               # fullBoard[440][i] = 'WHITE'

        cnt = cnt + 1
    pygame.draw.rect(displaySurf, LIGHTRED, (440, 520, 40, 40))

    # fullBoard[440][520] = 'LIGHTRED'

    cnt = 0

    for i in range(360, 600, 40):
        if cnt == 5:
            pygame.draw.rect(displaySurf, GREY, (440 + 40, i, 40, 40))
        elif cnt % 2 == 0:

               # fullBoard[440+40][i] = 'GREY'

            pygame.draw.rect(displaySurf, RED, (440 + 40, i, 40, 40))
        elif cnt % 2 != 0:

               # fullBoard[440+40][i] = 'RED'

            pygame.draw.rect(displaySurf, LIGHTRED, (440 + 40, i, 40,
                             40))

               # fullBoard[440+40][i] = 'LIGHTRED'

        cnt = cnt + 1

    cnt = 0

    for i in range(360, 600, 40):
        if cnt % 2 == 0:
            pygame.draw.rect(displaySurf, GREY, (440 + 80, i, 40, 40))
        else:

               # fullBoard[440+80][i] = 'GREY'

            pygame.draw.rect(displaySurf, WHITE, (440 + 80, i, 40, 40))

               # fullBoard[440+80][i] = 'WHITE'

        cnt = cnt + 1

    cnt = 0

    for i in range(560, 800, 40):
        if cnt % 2 == 0:
            pygame.draw.rect(displaySurf, GREY, (i, 240, 40, 40))
        else:

               # fullBoard[i][240] = 'GREY'

            pygame.draw.rect(displaySurf, WHITE, (i, 240, 40, 40))

               # fullBoard[i][240] = 'WHITE'

        cnt = cnt + 1

    cnt = 0

    for i in range(560, 800, 40):
        if cnt == 5:
            pygame.draw.rect(displaySurf, GREY, (i, 240 + 40, 40, 40))
        elif cnt % 2 == 0:

               # fullBoard[i][240+40] = 'GREY'

            pygame.draw.rect(displaySurf, BLUE, (i, 240 + 40, 40, 40))
        elif cnt % 2 != 0:

               # fullBoard[i][240+40] = 'BLUE'

            pygame.draw.rect(displaySurf, LIGHTBLUE, (i, 240 + 40, 40,
                             40))

               # fullBoard[i][240+40] = 'LIGHTBLUE'

        cnt = cnt + 1

    cnt = 0

    for i in range(560, 800, 40):
        if cnt % 2 == 0:
            pygame.draw.rect(displaySurf, GREY, (i, 240 + 80, 40, 40))
        else:

               # fullBoard[i][240+80] = 'GREY'

            pygame.draw.rect(displaySurf, WHITE, (i, 240 + 80, 40, 40))

               # fullBoard[i][240+80] = 'WHITE'

        cnt = cnt + 1

    pygame.draw.rect(displaySurf, LIGHTBLUE, (720, 240 + 80, 40, 40))


     # fullBoard[720][240+80] = 'LIGHTBLUE'

def drawCoins():
    for tup in mainboard:
        if tup[2] == 'RED':
            img1 = pygame.image.load('red.png')
            displaySurf.blit(img1, (tup[0], tup[1]))
        elif tup[2] == 'GREEN':
            img1 = pygame.image.load('green.png')
            displaySurf.blit(img1, (tup[0], tup[1]))
        elif tup[2] == 'YELLOW':
            img1 = pygame.image.load('yellow.png')
            displaySurf.blit(img1, (tup[0], tup[1]))
        else:
            img1 = pygame.image.load('blue.png')
            displaySurf.blit(img1, (tup[0], tup[1]))


          # pygame.draw.circle(displaySurf,clr, (tup[0],tup[1]),20,0)

def drawDice(moves, player):

    if player == 0:
        if moves == 1:
            img1 = pygame.image.load('dice1.png')
            displaySurf.blit(img1, (20, 20))
        if moves == 2:
            img1 = pygame.image.load('dice2.png')
            displaySurf.blit(img1, (20, 20))
        if moves == 3:
            img1 = pygame.image.load('dice3.png')
            displaySurf.blit(img1, (20, 20))
        if moves == 4:
            img1 = pygame.image.load('dice4.png')
            displaySurf.blit(img1, (20, 20))
        if moves == 5:
            img1 = pygame.image.load('dice5.png')
            displaySurf.blit(img1, (20, 20))
        if moves == 6:
            img1 = pygame.image.load('dice6.png')
            displaySurf.blit(img1, (20, 20))

    if player == 1:
        if moves == 1:
            img1 = pygame.image.load('dice1.png')
            displaySurf.blit(img1, (900, 20))
        if moves == 2:
            img1 = pygame.image.load('dice2.png')
            displaySurf.blit(img1, (900, 20))
        if moves == 3:
            img1 = pygame.image.load('dice3.png')
            displaySurf.blit(img1, (900, 20))
        if moves == 4:
            img1 = pygame.image.load('dice4.png')
            displaySurf.blit(img1, (900, 20))
        if moves == 5:
            img1 = pygame.image.load('dice5.png')
            displaySurf.blit(img1, (900, 20))
        if moves == 6:
            img1 = pygame.image.load('dice6.png')
            displaySurf.blit(img1, (900, 20))

    if player == 2:
        if moves == 1:
            img1 = pygame.image.load('dice1.png')
            displaySurf.blit(img1, (900, 380))
        if moves == 2:
            img1 = pygame.image.load('dice2.png')
            displaySurf.blit(img1, (900, 380))
        if moves == 3:
            img1 = pygame.image.load('dice3.png')
            displaySurf.blit(img1, (900, 380))
        if moves == 4:
            img1 = pygame.image.load('dice4.png')
            displaySurf.blit(img1, (900, 380))
        if moves == 5:
            img1 = pygame.image.load('dice5.png')
            displaySurf.blit(img1, (900, 380))
        if moves == 6:
            img1 = pygame.image.load('dice6.png')
            displaySurf.blit(img1, (900, 380))
    if player == 3:
        if moves == 1:
            img1 = pygame.image.load('dice1.png')
            displaySurf.blit(img1, (20, 380))
        if moves == 2:
            img1 = pygame.image.load('dice2.png')
            displaySurf.blit(img1, (20, 380))
        if moves == 3:
            img1 = pygame.image.load('dice3.png')
            displaySurf.blit(img1, (20, 380))
        if moves == 4:
            img1 = pygame.image.load('dice4.png')
            displaySurf.blit(img1, (20, 380))
        if moves == 5:
            img1 = pygame.image.load('dice5.png')
            displaySurf.blit(img1, (20, 380))
        if moves == 6:
            img1 = pygame.image.load('dice6.png')
            displaySurf.blit(img1, (20, 380))


def opening():

    displaySurf.fill(openBgColor)

    arr = []
    cnt = 0
    for i in range(0, windowWidth + 1, 100):
        for j in range(0, windowHeight + 1, 100):
            arr.append([i, j])
            cnt += 1
    colors = []

    for i in range(100):
        a1 = random.randint(0, 255)
        a2 = random.randint(0, 255)
        a3 = random.randint(0, 255)
        colors.append([a1, a2, a3])

    for i in range(cnt):

        color = random.choice(colors)
        (left, top) = random.choice(arr)
        arr.remove([left, top])
        pygame.draw.rect(displaySurf, color, (left, top, 100, 100))
        pygame.display.update()
        pygame.time.wait(30)

    img1 = pygame.image.load('ludo.png')
    displaySurf.blit(img1, (340 + 120, 300))

    pygame.display.update()
    pygame.time.wait(2000)


def secondWindow():

    displaySurf.fill(BLACK)
    img1 = pygame.image.load('player.png')
    displaySurf.blit(img1, (0, 0))

    img1 = pygame.image.load('rules.png')
    displaySurf.blit(img1, (335, 0))

    while True:
        displaySurf.fill(DARKTURQUOISE)
        img1 = pygame.image.load('player.png')
        displaySurf.blit(img1, (0, 0))
        
        img1 = pygame.image.load('rules.png')
        displaySurf.blit(img1, (335, 0))

        img1 = pygame.image.load('agree.png')
        displaySurf.blit(img1, (529, 540))
        ifquit()

          # pygame.display.update()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                (spotx, spoty) = (event.pos[0], event.pos[1])
                (centerx, centery) = getCenter(spotx, spoty)
                pygame.draw.rect(displaySurf, WHITE, (centerx, centery,
                                 40, 40))
                pygame.display.update()
                if (centerx == 520 or centerx == 560 or centerx == 600) \
                    and (centery == 520 or centery == 560):
                    pygame.mixer.music.load('button.mp3')
                    pygame.mixer.music.play(0)
                    return 1

        pygame.display.update()


def thirdWindow():
    displaySurf.fill(BLACK)
    img1 = pygame.image.load('player.png')
    displaySurf.blit(img1, (0, 0))

    img1 = pygame.image.load('selectPlay.png')
    displaySurf.blit(img1, (20, 100))

    img1 = pygame.image.load('2player.png')
    displaySurf.blit(img1, (520, 400))
 
    img1 = pygame.image.load('4player.png')
    displaySurf.blit(img1, (520, 480))

    img1 = pygame.image.load('enter.png')
    displaySurf.blit(img1, (520, 560))

    selection = 0

    while True:
        img1 = pygame.image.load('player.png')
        displaySurf.blit(img1, (0, 0))
        
        img1 = pygame.image.load('selectPlay.png')
        displaySurf.blit(img1, (20, 100))

        img1 = pygame.image.load('2player.png')
        displaySurf.blit(img1, (520, 400))
 
        img1 = pygame.image.load('4player.png')
        displaySurf.blit(img1, (520, 480))

        img1 = pygame.image.load('enter.png')
        displaySurf.blit(img1, (520, 560))
        
        ifquit()
        

        for event in pygame.event.get():
            
            if event.type == MOUSEBUTTONUP:

                (spotx, spoty) = (event.pos[0], event.pos[1])
                (centerx, centery) = getCenter(spotx, spoty)

                if (centerx == 520 or centerx == 560 or centerx == 600) and (centery == 400):
                    pygame.mixer.music.load('button.mp3')
                    pygame.mixer.music.play(0)
                    pygame.draw.rect(displaySurf, WHITE, (520, 400,120, 40),5)
                    selection = 2
                elif  (centerx == 520 or centerx == 560 or centerx == 600) and (centery == 480):
                    pygame.mixer.music.load('button.mp3')
                    pygame.mixer.music.play(0)
                    pygame.draw.rect(displaySurf, WHITE, (520, 480,120, 40),5)
                    selection = 4
                elif (centerx == 520 or centerx == 560 or centerx == 600) and (centery == 560) and selection != 0:
                    pygame.mixer.music.load('button.mp3')
                    pygame.mixer.music.play(0)
                    pygame.draw.rect(displaySurf, WHITE, (520, 560,120, 40),5)
                    return (selection, 'offline')
        
        pygame.display.update()            


def wonAnimation():
    displaySurf.fill(forthWindowColor)
    img1 = pygame.image.load('rsz_won.jpg')
    displaySurf.blit(img1, (0,0))

    img1 = pygame.image.load('win.png')
    displaySurf.blit(img1, (200,100))
    cnt = 0
    x = 0
    pygame.mixer.music.load('ludo.mp3')
    pygame.mixer.music.play(0)
    for i in wonList:
        cnt = cnt + 1
        x = x+40
        (textsurf, textrect) = maketext2(str(cnt) + '.   '
                + namePlayer[i-1], WHITE, BLACK, 200, 300+x)
        displaySurf.blit(textsurf, textrect)

    for i in reversed(leaveList):
        x = x+40
        cnt = cnt + 1
        (textsurf, textrect) = maketext2(str(cnt) + '.   '
                + namePlayer[i-1], WHITE, BLACK, 200, 300+x)
        displaySurf.blit(textsurf, textrect)
    pygame.display.update()
    pygame.time.wait(5000)


if __name__ == '__main__':
    main()


			
