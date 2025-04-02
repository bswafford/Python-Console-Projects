#Coin Toss Record Breaker


def main():#Contains the code for the program
    import random #Imports the Python module necessary to generate random numbers used to simulate coin flips.
    high_score=0 #Used to record the highest score of all attempts to break the high score. Starts at 0 and then is raised by successful iterations.
    game=0 #A variable used to record the number of games played. Starts at 0 and then is raised incrementally by each game.
    while True: #An infinite loop that will run until the program is terminated. This is what drives the games to continue endlessly.
        score=0 #A variable used to record the score of each attempt to break the high score. Starts at 0 and then is raised by successful iterations. Resets to 0 when each game is lost.
        game+=1 #Label each game with an incremental number.
        first_flip=random.randint(0,1) #The first coin flip of each game.
        while True: #A temporary loop that will be broken each time a game is lost.
            next_flip=random.randint(0,1) #The second coin flip of each game.
            if first_flip==next_flip: #If the coin flip successfully matches previous coin flip, then...
                score+=1 #Records the win by increasing the score variable by one.
                continue #Continue the game by returning to the beginning of the temporary loop.
            else: #But if the coin flip does not match the previous coin flip, then...
                if high_score<score: #If the current score is the highest score yet, then...
                    high_score=score #Record it as the high score, otherwise it will be ignored.
                    print("Game#        {:,}".format(game),"\nHigh Score:  "+str(high_score),"\nOdds:        {:,}".format(2**score)+" to 1","\nChance:      {:.5f}".format(((1/score**2)*100))+"%\n\n") #Display the end of game stats. Will not display if high score is still 0.
                break #Returns to the infinite loop to start another game.
                    
main()#Start the program


'''
Highest score so far
Game#        9,908,225,805 
High Score:  36 
Odds:        68,719,476,736 to 1 
Chance:      0.07716%
'''
