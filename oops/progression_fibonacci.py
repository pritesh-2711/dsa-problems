from progression import Progression

class FibonacciProgression(Progression):
    """Fibonacci Progression subclass from base Progression"""

    def __init__(self, first, second, start=0):
        super().__init__(start)
        self._first = first
        self._second = second

    def _advance(self):
        """Updated logic for Fibonacci progression"""
        self._current, self._first = self._second, (self._first + self._second) - self._first
        self._current = self._second
