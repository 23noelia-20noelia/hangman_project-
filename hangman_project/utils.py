#!/usr/bin/env python3
"""Funciones auxiliares del juego Hangman"""
import random


def get_random_word():
    """Devuelve al azar una palabra de wordlist.txt,
    perimte espacios y signos."""
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        words = file.readlines()

    check_words = []
    for word in words:
        word = word.strip()
        check_words.append(word)
    select_word = random.choice(check_words)
    return select_word
