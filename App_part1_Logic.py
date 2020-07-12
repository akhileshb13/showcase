# Currently under-construction app
# This app is meant to be an electronic version of Indian women's traditional _ for saving money. This game has many names in various regions of the country.
# Rules of the game: A group of few women come together & pool specific amount of money per person. Each month a winner is declared and all the money goes to her. Like this, the game goes on till each and every lady has won once. This proved to be a good way of saving money for women.

import random
import numpy as np
import sqlite3
import os
os.chdir(r'c:\users\.....\....\App')
import app_part2_database   # Import database logic file for creation,insertion,updation and deletion

# Defining a function to take user input and create a list of players
def create_list():
    new_plyr_lst = []                                              # Create a blank list to take in the names of players
    try: 
        n = int(input("Enter number of players: "))
    except ValueError:                                             # Exception handling: If user inputs alphabet instead of a number
        print('Please enter a valid number')
    else:                                                          # Execute this code block if there is no exception thrown
        if n >= 11:                                                # Condition to set a limit on number of players in a single game
           print("Only a maximum of 10 players are supported currently")
           #break
        elif n < 1:                                                 # Check if number of players are NOT negative or NOT zero
           print("Not a valid number") 
        else:                                                       # Executes when number of players fall within the accepted criterion
            temp_uid_lst = UniqueIDgenerator(n)                     # Call the function which generates unique IDs for each of the players
            print(f"Enter {n} names:")  
            for i in range(0, n):                                   # Iterating loop to collect user input player names
                element = (input()) ########
                while element in new_plyr_lst:                      # Condition to prevent same player being added twice
                    element = input("Two players cannot have similar names, please choose another name for the player: ")
                    if element not in new_plyr_lst:                 # Add new player to the list ONLY IF they are not present in the list already (This check is to see if the user has not entered an existing player AGAIN!)
                        new_plyr_lst.append(element)
                        print(f"Please add {n-i-1} more player/s")
                        break                                       # Exit While loop due to user compliance to adding a different player
                if element not in new_plyr_lst:                     # Condition to prevent same player being added twice
                    new_plyr_lst.append(element)
    merged_list = [[temp_uid_lst[i], new_plyr_lst[i]] for i in range(0, len(new_plyr_lst))]  # Merge the two lists (unique ID list and player name list) to get them ready to insert into database               
    app_part2_database.insertMultipleRecords(merged_list)                      # Call the backend function to insert Unique ID and Player Names to the database
    return merged_list
 
#------------------------------------------------------------------------------
  
def UniqueIDgenerator(num):                                         # This function generates a list of unique ID's which will then be assigned to each player in the game
    last_value = app_part2_database.getLastUniqueID()                          # Get the last inserted Unique ID value from database, so that new Unique Id can be generated after that
    uid_lst = np.arange(last_value[0]+1,last_value[0]+1+num,1)      # Generate a numpy list of newly generated Unique IDs
    uid_lst = uid_lst.tolist()                                      # Convert the numpy list to a simple python list to make it compatible for insertion into database
    return uid_lst

#------------------------------------------------------------------------------
#Define a function to select a lucky winner
def winner(ingame_plyr_lst):
    count = len(ingame_plyr_lst)
    if count == 0:
        return "The list is complete"
    else:
        indexes = np.arange(0,count,1)
        random_num = random.choice(indexes)
        lucky_winner = ingame_plyr_lst[random_num]
        ingame_plyr_lst.remove(lucky_winner)
        return (lucky_winner)

#------------------------------------------------------------------------------
#Code to detect and set winner flag in the database


        
#------------------------------------------------------------------------------
# Function calls
create_list()
temp_plyr_lst = app_part2_database.fetch()[:]
ingame_plyr_lst = []
for record in temp_plyr_lst:
    ingame_plyr_lst.append(record[0])
output = winner(ingame_plyr_lst)

#Output prints
if output == "The list is complete":
    print(output)      
else:
    print("...and the lucky winner is", output)

