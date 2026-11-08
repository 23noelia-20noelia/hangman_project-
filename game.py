
class HangmanGame:
    """Representa el juego del ahorcado."""

    def __init__(self, word):
        """Inicializa el juego con la palabra secreta."""
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Muestra el progreso actual de la palabra."""
        progress = []

        for letter in self.word:
            if not letter.isalpha():
                progress.append(letter)
            elif letter.lower() in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append("_")

        print("Letras utilizadas:", ", ".join(self.guessed_letters))
        print("Progreso:", " ".join(progress))
        print("Intentos restantes:", self.max_errors - self.errors)


    def is_won(self):
        """Comprueba si todas las letras fueron adivinadas."""
        return all(
            not letter.isalpha() or letter.lower() in self.guessed_letters
            for letter in self.word
        )

    def is_lost(self):
        """Comprueba si se alcanzó el máximo de errores."""
        return self.errors >= self.max_errors

    def process_guess(self, letter):
        """Registra el acierto o suma un error y
        devuelve si la letra fue acertada."""

        letter = letter.lower()
        self.guessed_letters.append(letter)

        if letter in self.word.lower():
            return True

        self.errors += 1
        return False

