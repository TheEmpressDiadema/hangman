class LanguageConfig:
    languages = ['ru', 'eng']
    paths = {
        "ru" : "src/hangman/data/ru.txt",
        "eng" : "src/hangman/data/eng.txt"
    }
    alphabets = {
        "ru" : "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
        "eng" : "abcdefghijklmnopqrstuvwxyz"
    }

class GameConfig:
    mask_character = "_"
    mistake_count = 5