import random
import time

def load_words():
    # List of words for the typing game
    return ["python", "developer", "keyboard", "programming", "code", "function", "variable", "loop", "condition", "syntax"]

def typing_game():
    words = load_words()
    random.shuffle(words)
    print("Welcome to the Typing Game!")
    print("Type the words as fast as you can. Press Enter after each word.")
    input("Press Enter to start...")

    start_time = time.time()
    correct_words = 0

    for word in words:
        print(f"Type this word: {word}")
        user_input = input()
        if user_input == word:
            correct_words += 1
        else:
            print(f"Incorrect! The correct word was: {word}")

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"\nGame Over! You typed {correct_words} words correctly.")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {correct_words / (time_taken / 60):.2f}")

if __name__ == "__main__":
    typing_game()
