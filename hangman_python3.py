import random
import time
import datetime
import os
from operator import itemgetter

os.system('clear')

play = True
while play:
    print(chr(27) + "[2J") #clear terminal
    os.system('clear')
    # initial variables
    lifes = 7

    user_name = input('Enter your name, to play the game: ').capitalize()
    print('\nHello ' + user_name + ', try to guess capital city, randomly choosen for you.\n' )
    
    now = datetime.datetime.now()
    #time_start = (now.minute, now.second)
    #print(time_start)
    start_time = time.time()

    # preparation
    f = open('countries_and_capitals.txt', 'r')
    lines = f.readlines()
    f.close
    country_capital = random.choice(lines)
    words = country_capital.strip().split(' | ')

    # print(country_capital)

    country = words[0].upper()
    print(country)
    capital = words[1].upper()
    print(capital)

    board = []
    missed_letters = []
    hit_letters = []
    is_winner = False
    
    for letter in capital:
        if(letter == " "):
            board.append(" ")
        else:
            board.append("_")

    while lifes > 0 and not is_winner:
        # print(chr(27) + "[2J") #clear terminal
        # os.system('clear')
        print(" ".join(board))  # glue letters from board array with space char
        print('')
        if lifes == 1:
                print('\nHint: the capital of ' + words[0] + "\n")  # gives a hint
        print("Lifes: " + str(lifes))
        print("Missed letters: "+", ".join(set(missed_letters)))
        print("Hit letters: "+", ".join(set(hit_letters)))
        guess = input('Enter a letter or full word: ').upper()
        # print(chr(27) + "[2J") #clear terminal
        os.system('clear')       
        letter_occurencies = 0
        if len(guess) > 1:  # for whole word
            if guess == capital:
                is_winner = True
            else:
                print('Wrong answear!')
                lifes -= 2

        else:   # for the letter
            i = 0
            for letter in capital:
                if letter == guess:
                    board[i] = letter
                    if letter not in hit_letters:
                        hit_letters.append(guess)
                        letter_occurencies += 1  # occurency in word (capital)
                i += 1
            if "".join(board) == capital:  # glue letters from board array with empty char
                is_winner = True
            if letter_occurencies == 0:
                missed_letters.append(guess)
                lifes -= 1
                print('\nWrong letter!\n')
                print('')
    if lifes == 0:
        print('Game over!')

    if is_winner:
        print('You won ! ' + user_name + ' that capital city is: ' + capital + '\n')
        # print(" ".join(board))
        end_time = time.time()
        game_time = int(end_time) - int(start_time)
        letters_tried = missed_letters + hit_letters
        # print(letters_tried)
        print('It took you ' + str(game_time) + ' seconds !\n')
        print('You guessed the capital after ' + str(len(letters_tried)) + ' letters')
        f = open('Scores.txt', 'a+')
        scoreline = "|".join([user_name, now.strftime("%Y-%m-%d %H:%M:%S"), str(game_time), str(len(letters_tried)), capital]) # join list to write in file
        f.write(scoreline + '\n')
        f.close()

        # print best scores
        print("\nHIGH SCORES:\n")
        f = open('Scores.txt', 'r')
        score_rows = f.readlines()
        score_board = []
        for row in score_rows:
            cols = row.split("|")
            score_board.append([cols[0], int(cols[2]), cols[3], cols[4]]) # select name and seconds pairs (convert second from string to int)
        # print(score_board)
        score_board = sorted(score_board, key=itemgetter(1)) # sort by second column (seconds)
        i = 1
        for row in score_board:
            print(str(i)+". "+row[0]+": "+str(row[1])+"sec" +" | " + str(row[2]) + " Moves" + " | " + str(row[3])) # shows ten biggest scores
            i += 1
            if i > 10:
                break

        f.close()

    yesorno = input('\nPlay again? (Y/n): ')
    if yesorno == "n":
        play = False