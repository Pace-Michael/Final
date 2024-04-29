# Michael Pace
# Intermediate Programing CISW 126
# mpace1@csi.edu

import unittest
import code_classes

trpsls = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'] # list of posable choises.
winning_con = [
    ('Rock', 'Scissors'), ('Rock', 'Lizard'), ('Paper', 'Rock'), 
    ('Paper', 'Spock'), ('Scissors', 'Paper'), ('Scissors', 'Lizard'), 
    ('Lizard', 'Paper'), ('Lizard', 'Spock'), ('Spock', 'Rock'), 
    ('Spock', 'Scissors')
    ] # List of all winning combinations. 

class Test_Code(unittest.TestCase): # Create a test class. 
    def test_pick_random(self): # Test the ramdom pick for computer. 
        r = code_classes.pick() # assigns computers pick to varable r
        if r in trpsls: # checks if r is in list rpsls.
            t = True # sets t == True if r is in list rpsls.
            self.assertTrue(t) # checks if t is true
        else: # runs if r is not is list rpsls.
            t = False # set t to False
            self.assertTrue(t) # checks if t is true. 

    def test_ls_Elements(self): # Function to test list elements. 
        self.expected = code_classes.rpsls # Tells the function to expected code_classes.rpsls
        self.result = trpsls # checks the expected list with the test list. 

    def test_player_win(self): # Creates a function for testing win conditions
        #game1 = code_classes.Check_Win('Rock', 'Scissors')
        #self.assertEqual(game1.player_Win(), 1)
        for uc in code_classes.rpsls: # creates a for loop running through code_classes.rpsls for the users choise.
            for cc in code_classes.rpsls: # creates a for loop running through code_classes.rpsls for the computers choise.
                with self.subTest(uc = uc, cc = cc):
                    game1 = code_classes.Check_Win(uc, cc) # Creates a varable and asigns it to code_classes.Check_Win.
                    if (uc, cc) in winning_con: # Checks in uc and cc are in the winning_con list
                        self.assertEqual(game1.player_Win(), 1) # Checks if the player won. 
                    else:
                        self.assertEqual(game1.player_Win(), 0) # checks if the player lost. 

    
if __name__ == '__main__':
    unittest.main()   