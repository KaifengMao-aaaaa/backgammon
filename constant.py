import pygame
#basic set
width_of_background = 700
height_of_background = 700
# #(column, row)
offsets = [(-1,0),(-1,-1),(0,-1),(1,-1)]
offsets_count = [1,1,1,1]
screen = pygame.display.set_mode((width_of_background,height_of_background))
text_font = pygame.font.Font(None, 80)
machine_turn = False
people_turn = True      
people = 1
Ai = 2
