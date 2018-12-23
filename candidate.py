class Candidate:
    """Represents a candidate for an electorate."""

    id_index = {}

    def __init__(self, id, name, party='Independent'):
        self.id = id
        self.name = name
        self.party = party

        self.ballots = []

        Candidate.id_index[id] = self

    def get_ballots(self):
        """Returns the list of ballots for the candidate."""
        return self.ballots

    def vote_count(self):
        """Returns the number of votes the candidate has."""
        return len(self.ballots)

    def add_ballot(self, ballot):
        """Adds a ballot to the candidate's ballots."""
        self.ballots.append(ballot)

    def remove_ballot(self, ballot):
        """Removes a ballot from the candidate's ballots."""
        self.ballots.remove(ballot)

    @classmethod
    def find_by_id(cls, id):
        return cls.id_index[id]

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<{}, {}, {}>".format(self.id, self.name, self.vote_count())
