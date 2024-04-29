# Michael Pace
# Intermediate Programing CISW 126
# mpace1@csi.edu
# Final Project. 
# Coding with Ross youtube channel provided a lot of help with the code. Mainly the botton code and multiply window code.

# Game Imports. 
import pygame, sys, code_classes, button, time

# Initializes pygame.
pygame.init()

# Variables that set windows Width and Height
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 550

fps = 30 
clock = pygame.time.Clock()

# Sets the fonts for pygame. 
title_font = pygame.font.Font('fonts/campus.ttf', 25)
title_bf = pygame.font.Font('fonts/college.ttf', 20)
game_bf = pygame.font.Font('fonts/collegeb.ttf', 30)
socre_font = pygame.font.Font('fonts/CollegiateFLF.ttf', 20)

# Loads the images for background and buttons.
icon = pygame.image.load('photo/icon.png')
play = pygame.image.load('photo/play_button.png')
play_again = pygame.image.load('photo/play_again.png')
main_menu = pygame.image.load('photo/main_menu.png')
directions = pygame.image.load('photo/directions_button.png')
exit_img = pygame.image.load('photo/exit_button.png')
background = pygame.image.load('photo/enterprise.png')
rock = pygame.image.load('photo/rock.jpg')
paper = pygame.image.load('photo/paper.jpg')
scissors = pygame.image.load('photo/scissors.png')
lizard = pygame.image.load('photo/lizard.jpg')
spock = pygame.image.load('photo/spock.jpg')

# Sets the colors for pygame. 
white = (255, 255, 255)
black = (0, 0, 0)
gray = (113, 121, 126)
green = (170, 255, 0)

# Creates Buttons.
play_button = button.Button(375, 175, play, .35)
info_button = button.Button(375, 250, directions, .35)
exit_button = button.Button(375, 325, exit_img, .35)
exit_button1 = button.Button(126, 505, exit_img, .30)
play_again_button = button.Button(251, 505, play_again, .30)
main_menu_button = button.Button(1, 505, main_menu, .30)
rock_button = button.Button(150, 100, rock, .15)
paper_button = button.Button(275, 100, paper, .35)
scissors_button = button.Button(525, 100, scissors, .68)
lizard_button = button.Button(185, 250, lizard, .20)
spock_button = button.Button(450, 250, spock, .17)

# Creates the window and sets the window title. 
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Main Menu")
pygame.display.set_icon(icon)

# game window control. 
window_state = 'main'

# player selection.
player = ''
code_classes.users_choise = player


# Fuction to draw text on screen.
def show_text(text, font, text_color, x, y):
    text_img = font.render(text, True, text_color)
    window.blit(text_img, (x, y))

# main game loop.
app = True # Sets the varabile app to True.
while app: # Creates a while loop.
    # fills the root_window with black.
    window.fill('black')
    window.blit(background, (0, 0))
    clock.tick(fps)

    # chech game state.
    if window_state == 'main': # if window_state varabile is 'main' run code below.
        show_text('Rock, Paper, Scissors, Lizard, Spock', title_font, green, 180, 10) # Puts text on the screen.
        show_text('Please make a selection', title_font, green, 255, 40) # Puts text on the screen.
        if play_button.draw_button(window): # Puts button on screen.
            #time.sleep(.5)
            window_state = 'play' # Changes the window_state varabile to 'play'
        if info_button.draw_button(window): # Puts button on screen.
            window_state = 'info' # Changes the window_state varabile to 'info'
        if exit_button.draw_button(window): # Puts button on screen.
            app = False # Sets the varabile app to False and close the while loop exiting the game.
    if window_state == 'play': # if window_state varabile is 'main' run code below.
        player_choise = ''
        show_text('Rock, Paper, Scissors, Lizard, Spock', title_font, green, 180, 10) # Puts text on the screen.
        show_text('Please make a selection', title_font, green, 255, 40) # Puts text on the screen.
        show_text(f'Score = {code_classes.score_str()}', socre_font, green, 650, 510) # Puts text on the screen.
        show_text(f'{code_classes.statement}', game_bf, green,300, 375)
        if main_menu_button.draw_button(window): # Puts button on screen.
            window_state = 'main' # Changes the window_state varabile to 'main'
        if exit_button1.draw_button(window): # Puts button on screen.
           app = False # Sets the varabile app to False and close the while loop exiting the game.
           sys.exit()
        if rock_button.draw_button(window): # Puts button on screen.
            player_choise = 'Rock'
            #print('Rock')
        if paper_button.draw_button(window): # Puts button on screen.
            player_choise = 'Paper'
            #print('Paper')
        if scissors_button.draw_button(window): # Puts button on screen.
            player_choise = 'Scissors'
            #print('Scissors')
        if lizard_button.draw_button(window): # Puts button on screen.
            player_choise = 'Lizard'
            #print('Lizard')
        if spock_button.draw_button(window): # Puts button on screen.
            player_choise = 'Spock'
            #print('Spock')
        if player_choise:
            computer_choise = code_classes.pick()
            check_win = code_classes.Check_Win(player_choise, computer_choise)
            winner = check_win.player_Win()
            check_win.add_score(winner)
            statement = check_win.statments_to_return(winner)
            player_choise = ''

    if window_state == 'info': # if window_state varabile is 'main' run code below.
        show_text('Rock, Paper, Scissors, Lizard, Spock', title_font, green, 180, 10) # Puts text on the screen.
        show_text('THE RULES ARE AS FOLLOWS:', title_font, green, 250, 80) # Puts text on the screen.
        show_text('The user will pick one of the following: Rock, Paper, Scissors, Lizard or Spock.', title_bf, green, 25, 110) # Puts text on the screen.
        show_text('The computer will than randomly make a choise.', title_bf, green, 175, 130) # Puts text on the screen.
        show_text('HOW TO WIN:', title_font, green, 325, 200) # Puts text on the screen.
        show_text('Rock beats scissors and lizard.', title_bf, green, 250, 220) # Puts text on the screen.
        show_text('Paper beats rock and disproves Spock.', title_bf, green, 225, 240) # Puts text on the screen.
        show_text('Scissors cuts paper and decapitates lizard.', title_bf, green, 200, 260) # Puts text on the screen.
        show_text('Lizard eats paper and poisons Spock.', title_bf, green, 225, 280) # Puts text on the screen.
        show_text('Spock vaporizes rock and smashes scissors.', title_bf, green, 200, 300) # Puts text on the screen.
        if main_menu_button.draw_button(window): # Puts button on screen.
            window_state = 'main' # Changes the window_state varabile to 'main'
        if exit_button1.draw_button(window): # Puts button on screen.
            app = False # Sets the varabile app to False and close the while loop exiting the game.
            sys.exit()
    # handles events
    for event in pygame.event.get(): # Looks for and get events from pygame.
        if event.type == pygame.QUIT: # If the event is equal to pygame quit event exacute code below.
            app = False # Sets the varabile app to False and close the while loop exiting the game.

    # updates the game window.
    pygame.display.update() #update game display

# Quits pygame when loop exits. 
pygame.quit()