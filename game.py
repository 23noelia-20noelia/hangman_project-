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
            '#que pasa con la funcion auxiliar de utils.py'
            if not letter.isalpha():
                progress.append(letter)
            elif letter.lower() in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append("_")

        print(" ".join(progress))

    def process_guess(self, letter):
        """Registra el acierto o suma un error y
        devuelve si la letra fue acertada."""
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        self.errors += 1
        return False
