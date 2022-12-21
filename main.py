import pygame
import pygame.gfxdraw
pygame.init()
from checkerboard import checkerboard, drawbackground
import constant
from constant import screen, people, Ai
from AI import AI

# people always start fist
checkboard_1 = checkerboard()     
computer = AI() 
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         machine_turn = True
    # machine turn and people turn store at constant.py
    if constant.machine_turn == True:
        checkboard_1.drawchessman()    
        constant.machine_turn = False
        constant.people_turn = True
    elif constant.people_turn == True:
        return_value = checkboard_1.play_chess()
        # the return value[2] is ture if people click mouse at checkerboard
        if return_value[2]:
            constant.people_turn = False
            constant.machine_turn = True
            if checkboard_1.check_win(return_value[0], return_value[1], people):
                print('people win')
                checkboard_1.show_winner('people')
    pygame.display.update()

