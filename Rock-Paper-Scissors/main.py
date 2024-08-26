import random # random number generation
class Game:
    def __init__(self):
        # get the computer's pick 
        self.computer_pick=self.get_computer_pick()

        # get the user's pick
        self.user_pick=self.get_user_pick()
        # get the result of the game
        self.result = self.get_result()     
     
    #For computer pick
    def get_computer_pick(self):
        # get random number among 1, 2 and 3
        random_number=random.randint(1,3)

        #possible options
        options={1:'rock',2:'paper',3:'scissors'} #dictionary

        # return the value present at random_number
        return options[random_number]
    
    #For user pick
    def get_user_pick(self):
        # infinite while loop 
        while True:
            # get input from the user
            user_pick=input('Enter rock/paper/scissors:')
            # converting the user's pick to lowercase and returned it
            user_pick= user_pick.lower()
             # if user_pick is either rock or paper or scissors,
            # terminate the loop
            if user_pick in('rock','paper','scissors'):
                break
            else:
                print('Enter valid input !')
        return user_pick
        
    #decide win,lose or draw
    def get_result(self):
        #condition for draw
        if self.computer_pick==self.user_pick:
            return 'draw'
        
        #condition for user to win
        elif self.user_pick=='paper' and self.computer_pick=='rock':
            return 'win'
        elif self.user_pick=='rock' and self.computer_pick=='scissors':
            return 'win'
        elif self.user_pick=='scissors' and self.computer_pick=='paper':
            return 'win'
        # in all other conditions, users lose  
        else:
            return 'lose'
    
    def print_result(self):
        print(f"Computer's pick:{self.computer_pick}")
        print(f"User's pick: {self.user_pick}")
        print(f'You:{self.result}')

# create an object of the Game class
#run the game for 5 time
for i in range(5):
    game=Game()
    game.print_result()

    #enabling user to play game again
    play_again=input('Do you want to play again? (y/n): ')
    if play_again!='y':
        break
#Game Finished