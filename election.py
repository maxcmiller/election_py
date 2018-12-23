import json
from candidate import Candidate
from ballot import Ballot

class Election:
    """Represents an election for a single electorate with candidates and
    ballots."""

    def __init__(self, date, type, name, enrolled, turnout):
        self.date = date
        self.type = type
        self.name = name
        self.enrolled = enrolled
        self.turnout = turnout

        self.candidates = []
        self.ballots = []

    @classmethod
    def from_json(cls, filepath):
        """Instantiates an Election with candidates and ballots loaded from a
        local JSON file."""
        with open(filepath) as file:
            filecontents = file.read()
        data = json.loads(filecontents)

        date     = data['date']
        type     = data['type']
        name     = data['name']
        enrolled = data['enrolled']
        turnout  = len(data['ballots']) # Number of votes received

        election = Election(date, type, name, enrolled, turnout)

        for candidate_dict in data['candidates']:
            candidate = Candidate(
                candidate_dict['id'],
                candidate_dict['name'],
                candidate_dict['party']
            )
            election.candidates.append(candidate)

        for preferences_list in data['ballots']:
            election.ballots.append(Ballot(preferences_list))

        return election

    def calculate(self):
        """Calculates the final winning candidate of the election
        and total vote counts for all candidates."""
        winner = None

        # Allocate first preferences by moving ballots to candidates' counts
        for ballot in self.ballots:
            cand = Candidate.find_by_id(ballot.get_candidate())
            cand.add_ballot(ballot)

        while winner is None:
            # Check if a winner exists by majority of votes
            for candidate in self.candidates:
                if candidate.vote_count() > self.turnout / 2:
                    winner = candidate

            # Find and eliminate the candidate with the least votes
            last_candidate = sorted(self.candidates,
                key=Candidate.vote_count)[0]
            ballots_to_eliminate = last_candidate.get_ballots()
            print('eliminating {}'.format(ballots_to_eliminate))
            for ballot in ballots_to_eliminate:
                # Update ballot's preferences to reflect the eliminated candidate
                ballot.eliminate()

                print(ballot)
                # Remove ballot from their votes
                last_candidate.remove_ballot(ballot)

                # Find the ballot's next preference and allocate the vote to them
                next_preference = Candidate.find_by_id(ballot.get_candidate())
                next_preference.add_ballot(ballot)

    def print_results(self):
        """Print the final results to the console."""

        print('{} in {}:'.format(self.type, self.name))
        turnout_percent = (self.turnout / self.enrolled) * 100
        print('Turnout: {} of {} enrolled ({:.2f}%)'
            .format(self.turnout, self.enrolled, turnout_percent)
        )
        print(self.candidates)
        print(self.ballots)
        for cand in self.candidates:
            print('{} got {} votes'.format(cand, cand.vote_count()))

        
