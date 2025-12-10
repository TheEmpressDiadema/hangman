class Menu:

    def __init__(self):
        self._view = {
            1 : "New Game\n",
            2 : "Quit\n"
        }

    def __getitem__(self, index: int) -> str | None:
        return self._view.get(index)
    
    @property
    def view(self):
        return self._view.items()