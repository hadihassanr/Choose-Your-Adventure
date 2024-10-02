def adventure_game():

    name = input("Type your name: ")
    print("Welcome", name, "to this adventure!")

    answer = input("You are on a dirt road, it has come to an end and you can now go left or right. Which way would you like to go? For left, type left and for right, type right ").lower()

    if answer == "left":
        answer = input("You come to a river, you can walk around it or swim across? Type 'walk' to walk around and 'swim' to swim across: ").lower()

        if answer == "swim":
            print("You try to swim across, and were eaten by a crocodile. You lose.")
            
        elif answer == "walk":
            print("You walked for many miles, ran out of water and you lost the game.")
            
        else:
            print("Not a valid option. You lose.")
            

    elif answer == "right":
        answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

        if answer == "back":
            print("You go back, you get attacked by Bigfoot and you die. You lost.")
            
        elif answer == "cross":
            answer = input("You crossed the bridge, and meet a stranger. Do you talk to them (yes/no)? ").lower()

            if answer == "yes":
                print("You talk to the stranger and he guides you to the secret tunnel out and you win.")
                
            elif answer == "no":
                print("You ignore the stranger, and because of that you remain lost in the forest and you lose.")
                
            else:
                print("Not a valid option. You lose.")
                
        else:
            print("Not a valid option. You lose.")
            

    else:
        print("Not a valid option. You lose.")
        

    
    
    
    
    print("Thank you for trying", name)

adventure_game()