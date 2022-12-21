from constant import width_of_background, height_of_background,screen,offsets, offsets_count, text_font, people, Ai
import constant
import pygame
class checkerboard:
    def __init__ (self):
        self.row_points = 15
        self.rediu_of_chessman = 18
        self.screen_center = (width_of_background / 2, height_of_background / 2)
        self.column_points = 15
        self.table_per_line = 14
        self.the_length_between_two_point = 40
        self.line_colour = 'black'
        self.line_width = 2
        # we need add big black circle at specific position for getting a better checkborad
        self.special_position = [[3,3],[3,11],[11,3],[11,11]]
        self.game_background = pygame.Surface((self.table_per_line * self.the_length_between_two_point, self.table_per_line * self.the_length_between_two_point))
        self.game_background_rect = self.game_background.get_rect(center = self.screen_center)
        self.checkerboard = [[0 for i in range(0,15)] for j in range(0,15)]
        self.checkerboard_position = [[0 for i in range(0,15)] for j in range(0,15)]
        drawbackground()
        self.drawcheckerboard()
        self.draw_specialpoints()
    #     #draw line
    #     # use rectangle to get the start and end point of line
    #     # move rectangle 15 times 
    #     # two loops for horizontal lines and vertical lines
    def drawcheckerboard(self):
        for i in range(0,15):
            # the width of first and last line of checkboard are larger
            if i == 0 or i == 14:
                pygame.draw.line(screen, self.line_colour, self.game_background_rect.topleft, self.game_background_rect.bottomleft, self.line_width + 2)
            else:    
                pygame.draw.line(screen, self.line_colour, self.game_background_rect.topleft, self.game_background_rect.bottomleft, self.line_width)
            self.game_background_rect.x += self.the_length_between_two_point
        self.game_background_rect.center = (350,350)
        for i in range(0,15):
            if i == 0 or i == 14:
                pygame.draw.line(screen, self.line_colour, self.game_background_rect.topleft, self.game_background_rect.topright, self.line_width + 2)
            else:
                pygame.draw.line(screen, self.line_colour, self.game_background_rect.topleft, self.game_background_rect.topright, self.line_width)
            #collect information about exact position of each point
            self.fill_position_list(i)
            self.game_background_rect.y += self.the_length_between_two_point
        self.game_background_rect.center = self.screen_center
    def fill_position_list(self, row):
        for j in range(0,15):
            self.checkerboard_position[row][j] = [self.game_background_rect.x + j * self.the_length_between_two_point, self.game_background_rect.y]
    def drawchessman(self):
        for i in range(0,15):
            for j in range(0,15):
                if self.checkerboard[i][j] == people:
                    pygame.gfxdraw.aacircle(screen,self.checkerboard_position[i][j][0], self.checkerboard_position[i][j][1], self.rediu_of_chessman, (0,0,0))
                    pygame.gfxdraw.filled_circle(screen,self.checkerboard_position[i][j][0], self.checkerboard_position[i][j][1], self.rediu_of_chessman, (0,0,0))

                elif self.checkerboard[i][j] == Ai:
                    pygame.gfxdraw.aacircle(self.screen,self.checkerboard_position[i][j][0], self.checkerboard_position[i][j][1], self.rediu_of_chessman, (255,255,255))
                    pygame.gfxdraw.filled_circle(self.screen,self.checkerboard_position[i][j][0], self.checkerboard_position[i][j][1], self.rediu_of_chessman, (255,255,255))
    def draw_specialpoints(self):

        for point in self.special_position:
            i = point[0]
            j = point[1]
            pygame.gfxdraw.aacircle(screen,self.checkerboard_position[i][j][0], self.checkerboard_position[i][j][1], 5, (0,0,0))
            pygame.gfxdraw.filled_circle(screen,self.checkerboard_position[i][j][0], self.checkerboard_position[i][j][1], 5, (0,0,0))
    def play_chess(self):
        if pygame.mouse.get_pressed() == (1,0,0):
            mouse_position = pygame.mouse.get_pos()
            mouse_position = list(mouse_position)
            x = mouse_position[0] - self.game_background_rect.x
            y = mouse_position[1] - self.game_background_rect.y
            if x <= self.table_per_line * self.the_length_between_two_point and x >= 0 and y >= 0 and y <= self.table_per_line * self.the_length_between_two_point:
                column = x // self.the_length_between_two_point
                column_remain =  x % self.the_length_between_two_point
                row = y // self.the_length_between_two_point
                row_remain = y % self.the_length_between_two_point
                if column_remain > 0.5 * self.the_length_between_two_point:
                    column += 1

                if row_remain > 0.5 * self.the_length_between_two_point:
                    row += 1
                self.checkerboard[row][column] = 1
                return (row, column,True)
        return(0,0,False)
    def check_win(self,row, column, target):
        index = 0
        # check whether the point have 4 more same kind of points in four different directions
        # store the direction as tuple 
        # offset[1] is row_offset, offset[0] is column offset
        for offset in offsets:
            if self.check_one_direction(target,row, column, offset[1], offset[0], index):
                return True
            index += 1
        #initialization of count time
        global offsets_count
        offsets_count = [1,1,1,1]
    def check_one_direction(self,target,row,column, row_offset, column_offset, index):
        #the time of meeting target will be counted at offset count list
        for i in range(1,5):
            row_index = row + row_offset * i
            column_index = column + column_offset * i
            if row_index < 0 or column_index > self.table_per_line:
                break
            elif self.checkerboard[row_index][column_index] == target:
                offsets_count[index] += 1
            else: break
        #check negative direction
        for i in range(1,5):
            row_index = row - row_offset * i
            column_index = column - column_offset * i
            if row_index < 0 or row_index > self.table_per_line or column_index < 0 or column_index > self.table_per_line:
                break
            if self.checkerboard[row_index][column_index] == target:
                offsets_count[index] += 1
            else: break
        return offsets_count[index] >= 5
    def show_winner(self,who):
        winner_display = pygame.Surface((width_of_background,height_of_background))
        winner_display.fill('black')
        screen.blit(winner_display,(0,0))
        text_display = text_font.render(f'winner is {who}', False, 'white')
        text_display_rect = text_display.get_rect(center = self.screen_center)
        screen.blit(text_display,text_display_rect)
        #both stop working
        constant.machine_turn = False
        constant.people_turn = False

def drawbackground():
    background = pygame.Surface((700,700))
    background.fill("#e4bf64")
    screen.blit(background,(0,0))
