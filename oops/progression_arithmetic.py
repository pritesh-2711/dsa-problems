from progression import Progression

class ArithmeticProgression(Progression):
    """Arithemetic Progression subclass from base Progression"""

    def __init__(self, increment, start=0):
        super().__init__(start)
        self.increment = increment

    def _advance(self):
        """Updated logic for arithmetic progression"""
        self._current += self.increment
