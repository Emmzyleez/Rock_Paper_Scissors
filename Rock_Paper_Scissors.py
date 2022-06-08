import random



game_options = ['R', 'P', 'S']
CPU = random.choice(game_options)

print("Welcome to Rock, Paper and Scissiors Game!\n")
print("Rules of the game are as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")


while True: 

    player = input ('Enter your option (S for stone, R for rock and P for Paper): ')
    print('Computer picks ' + CPU)
    if player != CPU:
        if player == 'R'and CPU == 'S':
            print('You win!')
      
        if player == 'S' and CPU == 'R':
            print('Computer win!')
    
        if player == 'P' and CPU ==  'R':
            print('You win!')
    
        if player == 'R' and CPU == 'P':
            print('Computer win!')
    
        if player == 'S' and CPU == 'P':
            print('You win!')
  
        if player == 'P' and CPU == 'S':
            print ('Computer win!')
        break 
    elif player == CPU:
        print('\nIts a tie, pick an option again')

