# Michael Pace
# Intermediate Programing CISW 126
# mpace1@csi.edu

import random # This imports the module for generating random numbers.

'''Below are Varables for the game. '''
computers_choise = ''
users_choise = ''
score = 0
win = 0
statement = 'Make a Choise' 

win_statement = 'You Won'
lose_statement = 'You lost'
tie_statement = 'You have tied'

'''Below is a list of choise for the user and computer to use.'''
rpsls = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

def score_str():
    score_string = str(score)
    return score_string

def pick():
    pick = random.randrange(5)
    computers_choise = rpsls[pick]
    return computers_choise

def users_choise():
    return users_choise.capitalize()

class Check_Win:
    def __init__(self, users_choise, computers_choise):
        self.computers_choise = computers_choise
        self.users_choise = users_choise

    def player_Win(self):
        win = 0
        if (self.users_choise == 'Rock'):
            if (self.computers_choise == 'Scissors'):
                win += 1
            elif (self.computers_choise == 'Lizard'):
                win += 1
            elif (self.users_choise == self.computers_choise):
                win += 1.5
        elif (self.users_choise == 'Paper'):
            if (self.computers_choise == 'Rock'):
                win += 1
            elif (self.computers_choise == 'Spock'):
                win += 1
            elif (self.users_choise == self.computers_choise):
                win += 1.5
        elif (self.users_choise == 'Scissors'):
            if (self.computers_choise == 'Paper'):
                win += 1
            elif (self.computers_choise == 'Lizard'):
                win += 1
            elif (self.users_choise == self.computers_choise):
                win += 1.5
        elif (self.users_choise == 'Lizard'):
            if (self.computers_choise == 'Paper'):
                win += 1
            elif (self.computers_choise == 'Spock'):
                win += 1
            elif (self.users_choise == self.computers_choise):
                win += 1.5
        elif (self.users_choise == 'Spock'):
            if (self.computers_choise == 'Rock'):
                win += 1
            elif (self.computers_choise == 'Scissors'):
                win += 1
            elif (self.users_choise == self.computers_choise):
                win += 1.5
            else:
                return "What the hell"       
        return win
        
    def add_score(self, win):
        global score

        self.win = win 
        if win == 1:
          score += 1
        else:
            score
        return score

    def statments_to_return(self, win):
        global statement
        self.win = win 
        if win == 1:
            win = 0
            statement = win_statement
            return statement
        elif win == 1.5:
            win = 0
            statement = tie_statement
            return statement
        else:
            statement = lose_statement
            return statement


if __name__ == '__main__': # This says if this is the main program run everything if not do not print. 
    computers_choise = pick()
    print(computers_choise)

   