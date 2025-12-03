class Config:
    _ru_path = "src/hangman/data/ru.txt"
    _eng_path = "src/hangman/data/eng.txt"
    _alphabets = {
        "ru" : "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
        "eng" : "abcdefghijklmnopqrstuvwxyz"
    }
    _mask_character = "_"
    _default_mistake_count = 5
    _default_language = "ru"