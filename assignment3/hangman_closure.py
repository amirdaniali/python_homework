# # Amir Daniali
# https://github.com/amirdaniali
# Code The Dream King Cobra
# Week 3


# Task 4
def make_hangman(secret_word):
    """
    Within the assignment3 folder, create a file called hangman-closure.py.
    Declare a function called make_hangman() that has one argument called secret_word. It should also declare an empty array called guesses. Within the function declare a function called hangman_closure() that takes one argument, which should be a letter. Within the inner function, each time it is called, the letter should be appended to the guesses array. Then the word should be printed out, with underscores substituted for the letters that haven't been guessed. So, if secret_word is "alphabet", and guesses is ["a", "h"], then "a__ha__" should be printed out. The function should return True if all the letters have been guessed, and False otherwise. make_hangman() should return hangman_closure.
    Within hangman-closure.py, implement a hangman game that uses make_hangman(). Use the input() function to prompt for the secret word. Then use the input() function to prompt for each of the guesses, until the full word is guessed.
    Test your program by playing a few games.
    """
    guesses = []

    def hangman_closure(new_letter):
        if type(new_letter) != str or len(new_letter) > 1:
            return "Invalid Input. A signle character string needed"

        guesses.append(new_letter)
        incomplete_guess = "".join(
            [char if char in guesses else "_" for char in list(secret_word)]
        )
        print(incomplete_guess)
        return incomplete_guess == secret_word

    return hangman_closure


hidden_secret = "closure"
game = make_hangman(hidden_secret)
has_won = False
tries = 0
while not has_won:
    user_guess = input("Type a single character guess for the hangman guess. ")
    while len(user_guess) > 1:
        user_guess = input("Invalid Input Error! Type a single character. ")
    tries += 1
    has_won = game(user_guess)

print("Good Job. The Secret was: ", hidden_secret)
print("You finished the game in", tries, "tries.")
