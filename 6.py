def game(player1, player2):
    while input("Want to Play Again") == 'Y':
        a = input("Player 1 do you want to choose rock paper or scissors")
        b = input("Player 2 do you want to choose rock paper or scissors")
        if a == b:
            print("It's a Tie")
        if a == 'rock' and b == 'scissors':
            print("Rock Wins")
        if a == 'scissors' and b == 'rock':
            print("Rock Wins")
        if a == 'scissors' and b == 'paper':
            print("scissors win")
        if a == 'paper' and b == 'scissors':
            print("scissors win")
        if a == 'rock' and b == 'paper':
            print("paper win")
        if a == 'paper' and b == 'rock':
            print('paper won')
    else:
        print("Thanks for coming to play")
player1 = input("Enter your name")
player2 = input("Enter your name")
game(player1, player2)
