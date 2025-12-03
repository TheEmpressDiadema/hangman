from hangman.management_source.config import GameConfig

from random import choice as choose_random_item


class GuessCycle:

    def __init__(self, alphabet: str, words: list[str], round_config: GameConfig):
        self._alphabet = alphabet
        self._words = words
        self._mistake_count = round_config.mistake_count
        self._mask_character = round_config.mask_character

    def _set_guessable_word(self) -> str:
        return choose_random_item(self._alphabet)
    
    def _create_mask(self, guessable_word: str):
        return self._mask_character*guessable_word
    
    def run(self):
        guessable_word = self._set_guessable_word()
        mask = self._create_mask(guessable_word)
        