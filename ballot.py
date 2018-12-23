class Ballot:
    """
    Represents a single voting ballot paper.
    e.g. [1, 4, 2, 3]
    first preference to candidate with id 1
    second preference to candidate with id 4
    third              ...              id 2
    fourth             ...              id 3.
    """

    def __init__(self, preferences):
        self.preferences = preferences

    def get_candidate(self):
        """Return the highest preferenced candidate on the ballot."""
        return self._get_preference(0)

    def eliminate(self):
        """
        Removes the current top preference.
        Used when a candidate is eliminated.
        """
        self.preferences.pop(0)

    def _get_preference(self, position=0):
        """Return the candidate-id of the preference at the position
        marked on the ballot. By default, returns the first preference."""
        return self.preferences[position]

    def __str__(self):
        return str(self.preferences)

    def __repr__(self):
        return str(self)
