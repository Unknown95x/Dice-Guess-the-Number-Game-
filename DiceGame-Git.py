# This program allows customers to play between two different games offered at the QCC Casino Royale, "Guess The Number" and "Dice" games.

#import necessary modules
import random, time, sys

# Function to allow customers choice of game
def choice():
    game_chosen = False
    while game_chosen == False:
        print('Select the game you want to play\n1 = Guess The Number\n2 = Dice')
        game = input('Enter the game code: ')
        
        # get input from customers as game code, where 1 is Guess The Number and 2 is Dice
        if game == '1':
            print()
            print('                                 Guess The Number')
            print('''The Guess The Number game is played by guessing a number between 1 and 10. If the number is correctly guessed,
you win and the odds are 10 to 1 so if you bet 1 dollar and win, you will receive 11 dollars.''')
            print()
            choose = input('Do you want to play this game y/n? ')
            if choose == 'y':
                game_chosen = 'Guess The Number'

        elif game == '2':
            print()
            print('                                             Dice Game')
            print('''The Dice game is played by rolling a pair of dice. If you roll a seven(7) or eleven(11), you win. Any other roll and you lose.
The odds of rolling a seven is 6 to 1 so if you bet 1 dollar and win, you will receive seven(7) dollars. The odds of rolling an eleven are 18 to 1 so 
if you bet 1 dollar and win, you will receive nineteen(19) dollars. ''')
            print()
            choose = input('Do you want to play this game y/n? ')
            if choose == 'y':
                game_chosen = 'Dice Game'
        else:
            print()
            print('Please enter a valid game code.')
    #return the game name for later use
    return game_chosen

# guess the number function for the Guess The Number game
def guess_the_number(total_round, balance):
    # keep track of the current game winning, losses and rounds with variables
    wins = 0
    loss = 0
    current_round = 2
    print('Guess The Number game will begin shortly')
    time.sleep(2)

    # keep the round going until the balance is less than 5 or the round reaches 10
    while current_round <= 11 and balance >= 5:
        print('Guess The Number Round',current_round-1)
        bet = int(input('What is your bet for this round? '))
        while bet < 5 or bet > 50 or bet > balance:
            print()
            print('Minimum bet is $5 and Maximum bet is $50. Bet amount cannot be greater than your balance')
            bet = int(input('What is your bet for this round? '))

        print()
        print('Shuffling the numbers ',end='')
        sys.stdout.flush()
        for i in range(3):
            print(random.randrange(1,11), end='')
            sys.stdout.flush()
            time.sleep(.1)
            print('.', end='')
            sys.stdout.flush()
            time.sleep(.1)
            print('.', end='')
            sys.stdout.flush()
            time.sleep(.1)
            print('.', end='')
            sys.stdout.flush()
            time.sleep(.1)
        
        #the number the customer has to guess
        secret_num = random.randrange(1,11)
        cus_num = int(input('\nWhat is the Secret Number? '))
        print('The Secret Number is', secret_num)

        # if the guess is correct, increase balance and winnings else decrease balance and increase loss
        if cus_num == secret_num:
            print('You have guessed the number correctly!')
            balance += bet * 7
            wins += bet * 7
            print('Your winning amount is $', bet*7)
            print('Your current balance is $', balance)

        elif cus_num != secret_num:
            print('You guessed the number wrong!')
            balance -= bet
            loss += bet
            print('You have lost $', bet)
            print('Your current balance is $', balance)

        print()
        current_round += 1
        total_round += 1

        # let the customer know that his balance has run out and must exit the casino
        if balance < 5:
            print('You have run out of balance to play. Please exit the casino')
            print()
        
    # shows the summary of the current game with total winnings, rounds played and losses
    print(current_round-2, 'rounds of Guess The Number has been played. Your game summary:')
    print()

    print('Total Rounds of Guess The Number played:',total_round)
    print('Total Won $',wins)
    print('Total Lost $', loss)
    print('Final Balance $', balance)
    result = wins - loss
    if result < 0:
        print('Your total loss is $', loss-wins)

    elif result > 0:
        print('Your total won is $', result)
    print()

    # return the numbers for showing all game summary at once
    return balance, total_round, wins, loss

# Dice_game function for the Dice game
def dice_game(total_round, balance):
    #variables to keep track of the current games
    current_round = 2
    wins = 0
    loss = 0
    print('Dice Game will begin shortly')
    time.sleep(2)
    while current_round <= 11 and balance >= 5:
        print('Dice Game Round',current_round-1)
        bet = int(input('What is your bet for this round? '))

        while bet < 5 or bet > 50 or bet > balance:
            print()
            print('Minimum bet is $5 and Maximum bet is $50. Bet amount cannot be greater than your balance')
            bet = int(input('What is your bet for this round? '))
        print()

        print('Shuffling the dice ',end='')
        sys.stdout.flush()
        for i in range(3):
            print(random.randrange(1,11), end='')
            sys.stdout.flush()
            time.sleep(.1)
            print('.', end='')
            sys.stdout.flush()
            time.sleep(.1)
            print('.', end='')
            sys.stdout.flush()
            time.sleep(.1)
            print('.', end='')
            sys.stdout.flush()
            time.sleep(.1)
        
        # random dice numbers
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        total_dice = dice1+dice2
        print('\nDice 1 has the number', dice1)
        time.sleep(0.2)
        print('Dice 2 has the number', dice2)
        time.sleep(1)
        print('Your dice roll was', total_dice)
        print()

        # winning numbers are 7 and 11, everything else counts as a loss
        if total_dice == 7:
            print('By matching the number 7, you have won the round!')
            print('Your winning amount is $',7*bet)
            wins += 7*bet
            balance += 7*bet
            print('Your current balance is $',balance)
        
        elif total_dice == 11:
            print('By matching the number 11, you have won the round!')
            print('Your winning amount is $',19*bet)
            wins += 19*bet
            balance += 19*bet
            print('Your current balance is $',balance)
        
        else:
            print('Unfortunately, your dice was not among the lucky numbers')
            print('You have lost $',bet)
            loss += bet
            balance -= bet
            print('Your current balance is $',balance)

        print()
        current_round += 1
        total_round += 1
        if balance < 5:
            print('You have run out of balance to play. Please exit the casino')
            print()
    
    # show current round summary and return the variables
    print(current_round-2, 'rounds of Dice Game that has been played. Your game summary: ')
    print()
    print('Total Round of Dice game played: ',total_round)
    time.sleep(0.5)
    print('Total Won $: ',wins)
    print('Total Lost $: ', loss)

    time.sleep(0.5)
    
    print('Final Balance $: ', balance)
    result = wins - loss
    if result < 0:
        print('Your total losses $: ', loss-wins)
    elif result > 0:
        print('Your total won $: ', result)
    print()

    return balance, total_round, wins, loss

# welcome message with some aesthetics
welcome_mess = 'Welcome to QCC Casino Royale!'
for i in welcome_mess:
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(1)

print('\nWe are offerring you to play and go home with big bucks by playing either of two games')
time.sleep(2)
# show the customers available games
print('Guess The Number and Dice Game')
time.sleep(2)
print('Each game has their own rules, multiple ways to win, and different odds of winning')
print('Select the game which suits you the best and good luck!')
print()

# call the funtion where the customer will choose the game
current_game = choice()

print('You selected',current_game)
print()
# balance they will put into the game
balance = int(input(('Enter the amount of money you want to play with: ')))

while balance < 5 or balance > 1000:
    print('Amount cannot be less than $5 or greater than $1000')
    balance = int(input(('Enter the amount of money you want to play with: ')))

# keep the starting balance and the ending balance separate
starting_balance = balance
print()
print('You are playing', current_game, 'with bankroll amount of $',balance)
time.sleep(0.5)
print('Let the game begin!')

# these variables will be used before customers leave the casino to show a full summary of all games
guess_rounds = 0
guess_wins = 0
guess_loss = 0

dice_rounds = 0
dice_wins = 0
dice_loss = 0


keep_playing = 'yes'

# Keep asking for a choice after game ends until the customer has a balance or decides to leave
while balance >= 5 and keep_playing == 'yes':
    if current_game == 'Guess The Number':
        balance, guess_rounds, wins, loss = guess_the_number(guess_rounds, balance)
        guess_loss += loss
        guess_wins += wins

    elif current_game == 'Dice Game':
        balance, dice_rounds, wins, loss = dice_game(dice_rounds, balance)
        dice_wins += wins
        dice_loss += loss
    if balance >= 5: 
        new_game = input('Do you want to play another game y/n ')
        if new_game == 'y':
            current_game = choice()
        else:
            keep_playing = 'no'

# show a full summary of all games played
end_balance = starting_balance + guess_wins + dice_wins - dice_loss - guess_loss
tot_rounds = guess_rounds + dice_rounds
tot_wins = guess_wins + dice_wins
tot_loss = guess_loss + dice_loss
print('Your total summary of all your games:')
time.sleep(1)
print('Game Name            Rounds Played         Total Won           Total Lost          Net Earning')
time.sleep(2)
print('Guess The Number         ',guess_rounds,'                  ',guess_wins,'               ', guess_loss, '                ', guess_wins-guess_loss)
time.sleep(2)
print('Dice Game                ',      dice_rounds,'                 ',dice_wins,'               ',dice_loss,'                 ',dice_wins-dice_loss)
time.sleep(2)
for i in range(95):
    print('-', end='')
    sys.stdout.flush()
    time.sleep(0.015)
print('\nStarting Balance',starting_balance,'    ',tot_rounds,'Rounds           ',tot_wins,'              ',tot_loss,'  Ending Balance',end_balance)
time.sleep(1)
print()

# ending message based on losses and winnings
if tot_loss > tot_wins:
    print('Better luck next time!')
elif tot_loss < tot_wins:
    print('Good winnings and we hope to see you again!')
elif tot_loss == tot_wins:
    print('Tough luck!')
