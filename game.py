class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        progress = []

        for letter in self.word:
            if not letter.isalpha():
                progress.append(letter)
            elif letter.lower() in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append("_")

        print("Letras adivinadas:", ", ".join(self.guessed_letters))
        print("Progreso:", " ".join(progress))
        print("Intentos restantes:", self.max_errors - self.errors)

