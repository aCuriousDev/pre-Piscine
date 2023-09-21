import os
import time
import random


class HangmanGame:
    def __init__(self):
        self.attempts = 10
        self.guessed_letters = []
        self.current_word = ""
        self.hidden_word = ""
        self.start_time = None
        self.end_time = None
        self.pseudo = ""
        self.score_file = "scores.txt"

        # Ensure the path is relative to the script's location
        self.dictionary_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "dictionaries")

    def get_pseudo(self):
        self.pseudo = input("Enter your pseudo: ")

    def select_dictionary(self):
        print(os.listdir(self.dictionary_path))
        files = [f for f in os.listdir(
            self.dictionary_path) if f.endswith('.txt')]
        print("Available dictionaries:")
        for index, file in enumerate(files, 1):
            print(f"{index}. {file}")
        choice = int(input("Select a dictionary by number: "))
        with open(os.path.join(self.dictionary_path, files[choice - 1]), 'r') as f:
            words = f.readlines()
        self.word_to_guess = random.choice(words).strip().lower()

    def play(self)
        self.start_time = time.time()
        while self.attempts > 0:
            display_word = ''.join(
                [letter if letter in self.guessed_letters else '_' for letter in self.word_to_guess])
            print(display_word)

            if "_" not in display_word:
                self.end_time = time.time()
                print(
                    f"Congratulations, {self.pseudo}! You've guessed the word in {self.end_time - self.start_time:.2f} seconds.")
                self.save_score()
                return

            guess = input("Guess a letter or the whole word: ").lower()

            if len(guess) == 1:
                if guess in self.word_to_guess and guess not in self.guessed_letters:
                    self.guessed_letters.append(guess)
                else:
                    self.attempts -= 1
                    print(f"Incorrect! {self.attempts} attempts remaining.")
            else:
                if guess == self.word_to_guess:
                    self.end_time = time.time()
                    print(
                        f"Congratulations, {self.pseudo}! You've guessed the word in {self.end_time - self.start_time:.2f} seconds.")
                    self.save_score()
                    return
                else:
                    self.attempts -= 1
                    print(f"Incorrect! {self.attempts} attempts remaining.")

        print(f"Game over! The word was: {self.word_to_guess}")
        choice = input("Would you like to retry? (yes/no): ")
        if choice.lower() == "yes":
            self.attempts = 10
            self.guessed_letters = []
            self.select_dictionary()
            self.play()
        else:
            self.display_leaderboard()

    def save_score(self):
        # Score out of 300 seconds
        score = max(300 - (self.end_time - self.start_time), 0)
        with open("score.txt", "a") as file:
            file.write(f"{self.pseudo},{score}\n")
        print(f"Your score: {score:.2f}")

    def display_leaderboard(self):
        try:
            with open("score.txt", "r") as file:
                lines = file.readlines()
            scores = [line.strip().split(",") for line in lines]
            scores.sort(key=lambda x: float(x[1]), reverse=True)

            print("\nLeaderboard:")
            print("Pseudo\t\tScore")
            print("-------------------------")
            for pseudo, score in scores[:10]:
                print(f"{pseudo}\t\t{score}")
        except FileNotFoundError:
            print("No scores available yet!")

    def run(self):
        self.get_pseudo()
        self.select_dictionary()
        self.play()


if __name__ == "__main__":
    game = HangmanGame()
    game.run()
