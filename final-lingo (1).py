#!/usr/bin/env python
# coding: utf-8

# In[169]:


#step# 1:
#import laibearies
import sys
import json
import random
import time
import numpy as np
import pandas as pd
from termcolor import colored
colored()


# In[170]:


df = pd.read_csv('scrabble.json')
#print(df)


# In[171]:


df.shape


# In[172]:


#To store numbers in list name deco from 4 to 12
dico = []
list1 = df['aa'].to_list()


# In[173]:


list1


# In[174]:


for i in list1:
    #print(i)
    if len(i) > 4 and len(i) <= 12:
        #print(i)
        dico.append(i)
        #print(i,len(i)) #to show length of every number in output


# In[175]:

dico

# In[176]:


len(dico)


# In[177]:


def get_word():
    json_file ==  dico   
    text = json_file.read()   
    text = text.split()
    num_words = len(text)
    return text[random.randint(0, num_words)]


# In[178]:


def random_word(dico,l): #  Updates displayed word containing correct indices
    w = ""
    for i in range(len(dico)):  
        if i in l:    
            w += dico[i]
        else:
            w += "-"
    return w


# In[179]:


def inside(lst, w):   
    indices_correct = []
    if len(lst) != len(w):
        print("That's word not equall to gussed letter word.")
        return indices_correct
    else:
        for letter in range(len(w)):
            if lst[letter] in w[0:] and lst[letter] == w[letter]:
                print(f"\033[38;5;196m{lst[letter]} \033[0mis in the right spot!")
                indices_correct.append(letter)
            elif lst[letter] in w[1:]:
                print(f"\033[38;5;226m{lst[letter]} \033[0mis a correct letter, but in the wrong spot!")

            else:
                print(f"{lst[letter]} is incorrect!")
    return indices_correct








# In[180]:


def display_guesses(guesses):
    for lst in range(1, len(guesses)):
        print(f"Guess {lst}: ", end=" ")
        display_word(guesses[lst])
        print()


# In[181]:


def display_word(w):
    for letter in range(len(w)):
        print(f"\t{w[letter]}", end="\t")


# In[182]:


def partie(): 
    nums_found = False
    num_list = []
    x2 = []
    total_count = 0
    while not nums_found:
        if total_count == 25:
            nums_found = True
        else:
            num = random.randint(0, 100)
            if num not in num_list:
                num_list.append(num)
                total_count += 1
    for i in range(total_count):
        if not i % 5:
            x2.append([])
            x2[i // 5].append(num_list[i])
        else:
            x2[i//5].append(num_list[i])
    return x2


# In[183]:


def get_word():
    w_file = open("scrabble.json", "r")
    text = w_file.read()   #word_file = json_file
    text = text.split()
    num_words = len(text)
    return text[random.randint(0, num_words)]


# In[ ]:





# In[184]:


def initialize_players():
    num_players = int(input("How many players will there be? "))
    players = []
    for player in range(num_players):
        players.append(input(f"Please give a nickname for player {player + 1}: "))
    return players


# In[185]:


def show_scoreboard(players, scores):
    print("Current Standings:")
    for i in range(len(players)):
        print(f"{players[i]}: {scores[i]}")
    print()


# In[186]:


def initialize_scores(players):
    scores = []
    for i in range(len(players)):
        scores.append(0)
    return scores


# In[187]:


def checks_random(dico, lst, x):      
    if lst == dico:
        print(f"Congratulations, you've won! The word was: {dico}.")
        #input("Press enter to continue...")

        return 1

    elif x == 10:
        print(f"I'm sorry, you lost. The word was: {dico}.")
        #input("Press enter to continue... ")
        
        return 0
    else:
        return 0
        


# In[188]:


def partNaive(x2):
    for i in range(len(x2)):    
        for j in range(len(x2)):
            print(x2[i][j], end="\t")
        print()


# In[190]:


def play_game():  

    x2 = partie()
    players = initialize_players()
    scoreboard = initialize_scores(players)
    player_up = 0
    winning_score = 1

    while True:
        w = get_word()
        print(w)
        show_scoreboard(players, scoreboard)
        print(f"Okay {players[player_up]}, it's your turn!")
        guess_allowance = 10
        x = 0
        guess_so_far = w[0:1] + "---------"
        tot_indices_correct = [0, 1]
        guesses = [w, guess_so_far]

        for i in range(guess_allowance):
            display_guesses(guesses)
            lst = input("\nHere's your word. Make a guess! ").lower()
            guesses[i+1] = lst
            cur_indices_correct = inside(lst, w)
            tot_indices_correct.extend(cur_indices_correct)
            guesses.append(random_word(w, tot_indices_correct))
            x += 1
            if checks_random(w, guesses[i+1], x):
                scoreboard[player_up] += 1
                break

        if winning_score in scoreboard:
            print(f"Congratulations, {players[scoreboard.index(winning_score)]}, you've won!")
            break

        elif winning_score not in scoreboard:
            break

        else:
            player_up += 1
            if player_up == len(players):
                player_up = 0
        

def main():
    print(f"Welcome to Lingo.py. The object of this game is to guess a 5-letter word in 5 tries.")
    print(f"After each guess, you are told which letters are in the correct position, which aren't, and which are just wrong.")
    play_game()

    while True:
        quit = input("\nPress \033[38;5;196mQ\033[0m for Quit the Game\nPress \033[38;5;226mC\033[0m for Quit the Game").lower()
        if quit == "c":
            play_game()

        elif quit=="q":
            break

        elif quit != "q" or quit != "c":
            print("\033[38;5;196mWrong Input !\033[0m")

main()




# In[ ]:





# In[ ]:





# In[ ]:




