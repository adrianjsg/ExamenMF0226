import random

class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = []
        self.max_attempts = 7

    def guess(self, letter):
        if letter in self.guessed:
            print("You already guessed that letter")
        elif letter in self.word:
            self.guessed.append(letter)
            print("You guessed the letter!")
        else:
            self.guessed.append(letter)
            self.max_attempts -= 1
            print("You guessed wrong!")

    def get_status(self):
        print("Guess the word:")
        for char in self.word:
            if char in self.guessed:
                print(char, end="")
            else:
                print("_", end="")
        print('\n')

    def check_if_player_won(self):
        if all(char in self.guessed for char in self.word):
            return True
        return False

class Game:
    def __init__(self):
        self.word = self.choose_random_word()
        self.hanged = Hangman(self.word)

    def choose_random_word(self):
        words = ["asno", "bofetada", "cocacola", "docena", "elegante", "faraona"]
        return random.choice(words)

    def play(self):
        while self.hanged.max_attempts > 0:
            self.hanged.get_status()
            letter = input("Guess a letter: ").lower()
            self.hanged.guess(letter)

            if self.hanged.check_if_player_won():
                print("You won!")
                break

        if self.hanged.max_attempts == 0:
            print(f"You're out of attempts. The word was '{self.word}'.")

if __name__ == "__main__":
    game = Game()
    game.play()


