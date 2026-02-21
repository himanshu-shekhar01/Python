# import random

# # Step 1: List of words
# words = ['apple', 'banana', 'grapes', 'orange', 'mango']

# # Step 2: Choose a random word
# secret_word = random.choice(words)

# # Step 3: Setup game variables
# guessed_word = ['_'] * len(secret_word)  # shows _ _ _ _ for secret word
# attempts = 6  # number of wrong guesses allowed
# guessed_letters = []  # to store guessed letters

# # Step 4: Game loop
# while attempts > 0 and '_' in guessed_word:
#     print("\nWord:", ' '.join(guessed_word))
#     print("Guessed letters:", guessed_letters)
#     print(f"Remaining attempts: {attempts}")

#     guess = input("Guess a letter: ").lower()

#     if not guess.isalpha() or len(guess) != 1:
#         print("Please enter a single letter.")
#         continue

#     if guess in guessed_letters:
#         print("You already guessed that letter.")
#         continue

#     guessed_letters.append(guess)

#     if guess in secret_word:
#         print("✅ Good guess!")
#         for i in range(len(secret_word)):
#             if secret_word[i] == guess:
#                 guessed_word[i] = guess
#     else:
#         print("❌ Wrong guess!")
#         attempts -= 1

# # Step 5: End of game
# if '_' not in guessed_word:
#     print("\n🎉 Congratulations! You guessed the word:", secret_word)
# else:
#     print("\n😢 Game Over! The word was:", secret_word)
