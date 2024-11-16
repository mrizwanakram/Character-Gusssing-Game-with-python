#!/usr/bin/env python
# coding: utf-8

import sys
import random

# Step 1: Function to load words from the text file
def load_words(file_path):
    try:
        with open(file_path, "r") as file:
            # Read lines, strip newlines, and create a list
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)

# Step 2: Filter the words between 4 and 12 characters
def filter_words(words):
    return [word for word in words if 4 <= len(word) <= 12]

# Step 3: Function to display guesses
def display_guesses(guesses):
    for index, guess in enumerate(guesses, start=1):
        print(f"Guess {index}: {guess}")

# Step 4: Function to handle checking guesses
def check_guess(word, guess):
    feedback = []
    for i, letter in enumerate(guess):
        if i < len(word) and letter == word[i]:
            feedback.append(f"\033[92m{letter}\033[0m")  # Green for correct position
        elif letter in word:
            feedback.append(f"\033[93m{letter}\033[0m")  # Yellow for correct letter
        else:
            feedback.append(f"\033[91m{letter}\033[0m")  # Red for incorrect
    return "".join(feedback)

# Step 5: Main game loop
def play_game(dico):
    word_to_guess = random.choice(dico)
    attempts = 10
    guesses = []

    print("\nWelcome to the Word Guessing Game!")
    print(f"The goal is to guess the word within {attempts} tries.\n")

    while attempts > 0:
        guess = input(f"Enter your guess ({len(word_to_guess)} letters): ").strip().lower()

        if len(guess) != len(word_to_guess):
            print(f"Please enter a word of length {len(word_to_guess)}.")
            continue

        feedback = check_guess(word_to_guess, guess)
        guesses.append(feedback)
        display_guesses(guesses)

        if guess == word_to_guess:
            print(f"\nCongratulations! You guessed the word: {word_to_guess}\n")
            return
        else:
            attempts -= 1
            print(f"\nAttempts left: {attempts}\n")

    print(f"Game over! The correct word was: {word_to_guess}\n")

# Main function
def main():
    file_path = "scrabble.json"  # Update this to your file name if needed
    print("Loading words...")
    words = load_words(file_path)
    filtered_words = filter_words(words)

    if not filtered_words:
        print("No words available in the specified range (4 to 12 characters).")
        sys.exit(1)

    play_game(filtered_words)

    while True:
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice == "y":
            play_game(filtered_words)
        elif choice == "n":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Run the game
if __name__ == "__main__":
    main()
