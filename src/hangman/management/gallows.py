class Gallows:

    _states = [
        """
        --------|
                |
                |
                |
               / \\\n
        """,
        """
        --------|
        |       |
                |
                |
               / \\\n
        """,
        """
        --------|
        |       |
        0       |
                |
               / \\\n
        """,
        """
        --------|
        |       |
        0       |
        |       |
               / \\\n
        """,
        """
        --------|
        |       |
        0       |
       /|\\     |
       / \\    / \\\n
        """
    ]

    def get_state(self, index: int) -> str:
        return self._states[index - 1]