import  random
def get_choice():
   choices  = ['rock','paper', 'scissors']
   computer_choice = random.choice(choices)
   while True: 
      user_choice  = input("Enter 'rock for rock, 'paper' for paper, 'scissors' for scissors: ")
      if user_choice  not in ['rock','paper', 'scissors']:
         print("Invalid choice. Please enter 'rock',or  'paper', or 'scissors'.")
      else:
         return [user_choice, computer_choice]
def who_win(playyer, opponent):
    if playyer == opponent:
        return "It's a tie!"
    elif (playyer == "rock" and opponent == 'scissors')  or  (playyer == 'scissors'  and opponent == 'paper') or (playyer == 'paper' and  opponent == 'rock'):
        return "Congratulations! You win!"
    else: 
        return "Computer wins!"
def play_game():
     print("Let's play Rock, Paper, Scissors!")
     while True:
        user_choice, computer_choice   = get_choice() # unpacking choice
        print(f"You choose {user_choice}. Computer choose {computer_choice}.")
        print(who_win(user_choice, computer_choice))
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again not in [ 'yes','y','Y']:
            break

play_game()