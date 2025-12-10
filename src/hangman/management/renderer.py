from hangman.management.menu import Menu
from hangman.management.gallows import Gallows

class MenuRenderer:

    def render(self, menu: Menu) -> None:
        for item in menu.view:
            print(item)

class GallowsRenderer:

    def render(self, gallows: Gallows, state: int) -> None:
        print(gallows.get_state(state))