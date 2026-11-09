#!/usr/bin/env python3
"""Punto de entrada del juego Hangman."""

from utils import get_random_word
from game import HangmanGame, normalize_letter


def get_valid_letter(guessed_letters):
    """Solicita y valida una letra ingresada por el usuario."""
    while True:
        letter = input("Ingresa una letra: ").strip().lower()

        if len(letter) != 1:
            print("Error: debes ingresar una sola letra.")
        elif not letter.isalpha():
            print("Error: solo se permiten letras.")
        elif any(
            normalize_letter(guess) == normalize_letter(letter)
            for guess in guessed_letters
        ):
            print("Error: ya has intentado esa letra.")
        else:
            return letter


def main():
    """Inicia el juego y solicita una letra válida."""
    word = get_random_word()
    game = HangmanGame(word)

    print("Pista: la palabra a adivinar es una película.")

    while not game.is_won() and not game.is_lost():
        letter = get_valid_letter(game.guessed_letters)
        game.process_guess(letter)
        game.display_progress()

    if game.is_won():
        print("¡Ganaste!")
    elif game.is_lost():
        print("Fin del juego")
        print("La palabra era:", game.word)


if __name__ == "__main__":
    main()
