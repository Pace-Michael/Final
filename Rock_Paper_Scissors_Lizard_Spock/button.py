# Michael Pace
# Intermediate Programing CISW 126
# mpace1@csi.edu
# Final Project. 

# Game Imports. 
import pygame
# Creats a class for making a button in pygame.
class Button:
    def __init__(self, x, y, image, scale):
        # Gets the image width and set it to variable image_width
        image_width = image.get_width()
        # Gets the image height and set it to variable image_height
        image_height = image.get_height()
        # Sets the scale of the image using transform.scale by multipling the image varables by a decimal and asigns the image to a variable image.
        self.image = pygame.transform.scale(image, (int(image_width * scale), int(image_height * scale))) # You have to set your math to an int pygame will crash if your code returns a float.
        # Sets the image on a pygame rect object.
        self.rect = self.image.get_rect()
        # Sets the top left conor of the rect object to x, y position.
        self.rect.topleft = (x, y)
        # Sets the button clicked value to False (button clicked off).
        self. clicked = False

    # Defines a new fuction under the Button class.
    def draw_button(self, surface):
        action = False
        # Gets the mouse positon.
        pos = pygame.mouse.get_pos()

        # Checks if the mouse is over a button and in button was clicked.
        if self.rect.collidepoint(pos):
            # checks if the left [0] mouse button was clicked and only lets the button be click if clicked is False.
            for event in pygame.event.get(): # Creates a for loop for mouse detection on button press. 
                if event.type == pygame.MOUSEBUTTONDOWN: # says if mouse button down (These inculded all buttons Left, right, roller click) then do command below.
                    action = True # set action to True
                if event.type == pygame.MOUSEBUTTONUP: # # says if mouse button up (These inculded all buttons Left, right, roller scroll) then do command below.
                    action = False # set action to False.
            
            
            
            
            # if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            #     # When letf mouse button click set the click varable to True and stops the mouse from clicking again.
            #     self.clicked = True
            #     action = True
                

            # # Reset the clicked varable to False when left mouse button is released.
            # if pygame.mouse.get_pressed()[0] == 0:
            #     self.clicked = False       

        
        # Draws the botton on the window.  
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
    
