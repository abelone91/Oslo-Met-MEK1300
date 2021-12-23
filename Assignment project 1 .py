
# importing the random module

import random

# Display rules of game when prog. started

print ('''
************************************************************************************************************************
       Welcome to the game, rules as follows: 
       
       Choose any number between 1 and 50.
       If you guess the number correctly at your 1st attempt, you will get 10 times of money you bet.
       If you guess the number correctly at the 2nd attempt, you will get 5 times of money you bet.
       If you guess the number correctly at the 3rd attempt, you will get 3 times of money you bet.
       If you do not guess the number correctly within three attempts, you will lose your betting amount. 
       
       Good luck!
************************************************************************************************************************       
       ''')

# Genetating the winning guess

winning_guess = random.randint(1, 50)

# just for testing, removed after delivery

print(winning_guess)

#asks for name of player

name = input("insert name of player here: ")

# keep track of the attempts

attempt = 0

# prompt for user bet input

bet = int(input("insert your bet here: "))


while attempt < 3:
#for testing, removed upon delivery

       print(winning_guess)

       # Start count when entering/re-entering the loop

       attempt = attempt + 1

       # prompt for user guess input

       player_guess = int(input("insert your guess here: "))

       # validate data enty

       if player_guess < int(1) or player_guess > int(50):
              print("Please insert a number b/w 1 & 50")

       # Evaluate guess input

       if player_guess == winning_guess and attempt == 1:
              print("congratulations! you have just x10 your bet. your new balance", bet * 10)
              bet = bet * 10
              resume = input("do you want to resume game? y or n ")
              winning_guess = random.randint(1, 50)
              attempt = 0
              if resume == "n":
                     print("congratulations on collecting ", bet)
                     break

       elif player_guess == winning_guess and attempt == 2:
              print("congratulations! you have just x5 your bet. your new balance", bet * 5)
              bet = bet * 5
              resume = input("do you want to resume game? y or n ")
              winning_guess = random.randint(1, 50)
              attempt = 0
              if resume == "n":
                     print("congratulations on collecting ", bet)
                     break

       elif player_guess == winning_guess and attempt == 3:
              print("congratulations! you have just x3 your bet. your new balance", bet * 3)
              bet = bet * 3
              resume = input("do you want to resume game? y or n ")
              winning_guess = random.randint(1, 50)
              attempt = 0
              if resume == "n":
                     print("congratulations on collecting ", bet)
                     break
                     

       elif attempt == 3:
              print("Your have used up all your attempts. Your balance of ", bet , "is Lost. Please restart the game for another Go")
              break


       elif player_guess < winning_guess and attempt == 2:
              print("nr is too Low!, Try again")
              print("You have 1 remaining attempt")
              
       elif player_guess < winning_guess and attempt == 1:
           print("nr is too Low!, Try again")
           print("You have 2 remaining attempts")
               

       elif player_guess > winning_guess and attempt == 2:
              print("nr is too High!, Try again")
              print("You have 1 remaining attempt")

       elif player_guess > winning_guess and attempt == 1:
           print("nr is too High!, Try again")
           print("You have 2 remaining attempts")














