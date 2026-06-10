import random

# List of predefined words
words = ["python", "computer", "coding", "program", "developer"]

# Randomly select a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while attempts > 0:
    # Display the word with underscores
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is fully guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts)

# If attempts run out
if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)