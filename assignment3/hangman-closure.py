def make_hangman(secret_word):
    """Creates a closure for a hangman game."""
    guesses = []
    
    def hangman_closure(letter):
        """Inner function that handles guesses and displays the word."""
        # Append the letter to guesses array
        guesses.append(letter)
        
        # Build the display string with underscores for unguessed letters
        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"
        
        # Print the word with underscores
        print(display)
        
        # Check if all letters in the word have been guessed
        # If there are no underscores in the display, then all letters have been guessed
        all_guessed = "_" not in display
    
        return all_guessed
    
    return hangman_closure


# Main game loop
if __name__ == "__main__":
    # Prompt for the secret word
    secret_word = input("Enter the secret word: ")
    
    # Create the hangman closure
    hangman_game = make_hangman(secret_word)
    word_guessed = False
    
    # Game loop - keep prompting for guesses until word is guessed
    while not word_guessed:
        guess = input("Guess a letter: ")
        word_guessed = hangman_game(guess)

    print("Congratulations! You guessed the word!")
            