import random

# Step 1: Word list
words = ["apple", "mango", "grape", "peach", "lemon"]

# Step 2: Randomly choose a word
word = random.choice(words)

# Step 3: Initialize variables
guessed_letters = []
attempts = 6

# Step 4: Game loop
while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Incorrect! Attempts left:", attempts)

    if attempts == 0:
        print("💀 Game Over! The word was:", word)
