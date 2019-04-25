## Simple Blackjack Program
while True:
    print("Welcome to the Blackjack Program.")
    input_start = input("\nWould you like to play a new game? (yes or no): ")
    if input_start == "yes": #Starts a new Blackjack game
        from random import randint
        player_value = computer_value = randint(2,21)       
        def disp(player_value, computer_value):
            user_disp = "Player: " + str(player_value)
            cpu_disp = "Computer: " + str(computer_value)
            return "\n"+ user_disp + "\n" + cpu_disp #Initial hand of player and computer output
        print(disp(player_value, computer_value))
        if player_value == 21 and computer_value != 21:
            print("\nPlayer has Blackjack. You win!", "\n")
            continue
        elif player_value != 21 and computer_value == 21:
            print("\nComputer has Blackjack. You lose!", "\n")
            continue
        elif player_value == 21 and computer_value == 21:
            print("\nBoth of your hands push. It's a draw.", "\n")
            continue
        else:
            while player_value < 21:
                option = input("\nWould you like to hit or stand? ")
                if option == "hit":
                    player_value += randint(1,11)
                    print(disp(player_value, computer_value))
                elif option == "stand":
                    break
                else:
                    print("\nUnknown input, try again. Please choose hit or stand")
            else:
                if player_value > 21:
                    print("\nPlayer busts. You lose!", "\n")
                    continue               
            while computer_value < 21:
                computer_value += randint(1,11)
                if computer_value == 21 and player_value != 21:
                    print(disp(player_value, computer_value))
                    print("\nComputer has Blackjack. You lose!", "\n")
                elif computer_value != 21 and player_value == 21:
                    print(disp(player_value, computer_value))
                    print("\nPlayer has Blackjack. You win!", "\n")
                else:
                    print(disp(player_value, computer_value))
                    if computer_value > 21:
                        print("\nComputer busts. You win!", "\n")
                        continue               
    elif input_start == "no":
        print("\nThank you for participating!", "\n")
        break
    else:
        print("\nUnknown input, try again. Please choose either yes or no.\n")
        continue