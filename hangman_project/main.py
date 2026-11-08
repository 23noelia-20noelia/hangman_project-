#!/usr/bin/env python3
"""Punto de entrada del juego Hangman."""

from utils import get_random_word


def get_valid_letter(guessed_letters):
    """Solicita y valida una letra ingresada por el usuario."""
    while True:
        letter = input("Ingresa una letra: ").strip().lower()

        if len(letter) != 1:
            print("Error: debes ingresar una sola letra.")
        elif not letter.isalpha():
            print("Error: solo se permiten letras.")
        elif letter in guessed_letters:
            print("Error: ya has intentado esa letra.")
        else:
            return letter


def main():
    """Inicia el juego y solicita una letra válida."""
    from game import HangmanGame

    word = get_random_word()
    game = HangmanGame(word)

    while not game.is_won() and not game.is_lost():
        letter = get_valid_letter(game.guessed_letters)
        game.process_guess(letter)
        game.display_progress()

    if game.is_won():
        print("¡Ganaste!")
    elif game.is_lost():
        print("Fin del juego")


if __name__ == "__main__":
    main()
