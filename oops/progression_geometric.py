from progression import Progression

class GeometricProgression(Progression):
    """geometric Progression subclass from base Progression"""

    def __init__(self, multiple, start=0):
        super().__init__(start)
        self.multiple = multiple

    def _advance(self):
        """Updated logic for geometric progression"""
        self._current *= self.multiple
