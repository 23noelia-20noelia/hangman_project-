def normalize_letter(letter):
    """Normaliza las vocales para ignorar las tildes."""
    return letter.lower().translate(str.maketrans("áéíóú", "aeiou"))


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
        normalized_guesses = [
            normalize_letter(letter)
            for letter in self.guessed_letters
        ]

        for letter in self.word:
            normalized = normalize_letter(letter)

            if not letter.isalpha():
                progress.append(letter)
            elif normalized in normalized_guesses:
                progress.append(letter)
            else:
                progress.append("_")

        print("Letras intentadas:", ", ".join(self.guessed_letters))
        print("Progreso:", " ".join(progress))
        print("Intentos restantes:", self.max_errors - self.errors)

    def is_won(self):
        """Comprueba si todas las letras fueron adivinadas."""
        normalized_guesses = [
            normalize_letter(letter)
            for letter in self.guessed_letters
        ]

        return all(
            not letter.isalpha()
            or normalize_letter(letter) in normalized_guesses
            for letter in self.word
        )

    def is_lost(self):
        """Comprueba si se alcanzó el máximo de errores."""
        return self.errors >= self.max_errors

    def process_guess(self, letter):
        """Registra la letra intentada y devuelve si fue acertada."""
        self.guessed_letters.append(letter)

        normalized_guess = normalize_letter(letter)
        normalized_word = normalize_letter(self.word)

        if normalized_guess in normalized_word:
            return True

        self.errors += 1
        return False
