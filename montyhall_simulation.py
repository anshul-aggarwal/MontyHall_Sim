import random

no_of_tests = 1000000     #1 million tests


def montyhall():

    correct_switchdoor = 0
    correct_samedoor = 0
    incorrect_switchdoor = 0
    incorrect_samedoor = 0

    switchdoor_actual = 0
    samedoor_actual = 0

    for test in range(no_of_tests):
        car = random.randint(0,2)       #Door with car, chhosen randomly

        player_choice1 = random.randint(0,2)    #Player makes the choice

        #Monty hall reveals a door with a goat.

        #Initially, if player chose the door with a goat, Monty Hall reveals the other door with the goat.
        #To win, the player must switch to the unopened door, which has the car behind it.
        if player_choice1 != car:       
            switchdoor_actual += 1      #Switch door to win
            player_flip_choice = bool(random.getrandbits(1))    #Player decision on switching
            
            if player_flip_choice:
                correct_switchdoor += 1 #Player Switches and Wins
            else:
                incorrect_samedoor += 1 #Player Retains same door and Loses

        #Initially, if player chose the door with the car, Monty Hall reveals any of the other two doors randomly, both of which have a goat behind themm. 
        #To win the car, the player must retain the same door.    
        else:
            samedoor_actual += 1        #Retain same door to win
            player_flip_choice = bool(random.getrandbits(1))    #Player decision on switching

            if player_flip_choice:
                incorrect_switchdoor += 1   #Player Switches and Loses
            else:
                correct_samedoor += 1   #Player Retains same door and Wins

    
    #Results for a random gameshow contestant
    print("RESULTS FOR A RANDOM GAMESHOW CONTESTANT\n----------------------------------------")
    print("Player Switches door and Wins: " + str(correct_switchdoor/no_of_tests))
    print("Player Switches door and Loses: " + str(incorrect_switchdoor/no_of_tests))
    print("Player Stays with same door and Wins: " + str(correct_samedoor/no_of_tests))
    print("Player Stays with same door and Loses: " + str(incorrect_samedoor/no_of_tests))

    #Success probabilities on making the switching decision
    print("\nSUCCESS SCENARIOS FOR GAMESHOW CONTESTANTS\n------------------------------------------")
    print("Switch Door to Win: " + str(switchdoor_actual/no_of_tests))
    print("Same Door to Win: " + str(samedoor_actual/no_of_tests))


montyhall()
