class Progression:
    """A base class to represent progression of different kinds."""

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        """The core logic of progression. For base class, it'll increment by one. For subclasses, will replace it."""
        self._current += 1

    def __next__(self):
        """Next in the iteration"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """Make Iterator. By default they return self only."""
        return self

    def generate_progression(self, n):
        """Range n until which progression must work."""
        return " ".join(str(next(self)) for _ in range(n))