from enum import Enum

class PauseElements(Enum):
    CONTINUE = "1"
    EXIT_TO_MENU = "2"
    EXIT = "3"

class MainMenuElements(Enum):
    NEW_GAME = "1"
    SETTINGS = "2"
    QUIT = "3"

class SettingsMenuElements(Enum):
    CHANGE_LANG = "1"
    CHANGE_MISTAKE_COUNT = "2"

class Languages(Enum):
    RU = "1"
    ENG = "2"