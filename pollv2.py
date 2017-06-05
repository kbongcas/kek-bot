#Class that represents a Poll
class Poll:
    prev_Voted = []
    poll_choices = []
    poll_question = ""
    choice_tally = {}


    def __init__ (self, poll_as_string ):
        self.create_poll( poll_as_string )

    #determine if a voter has already voted
    def validVote( voter ):
        if any( name in s for s in voted ):
            return False 
        else:
            return True

    #add voter to previously voted list 
    def add2Voted( voter ):
        prev_Voted.append( voter )

    #split a string using "|" as the split indicator
    def split_poll_string( poll_as_string ):
        self.poll_choices = poll_as_string.split("|") 
        self.poll_question = poll_choices[0]

    #creates the format of the pol
    def create_poll(self, poll_as_string ):
        split_poll_string( poll_as_string ) 

        #initialize each choice with 0 votes 
        for counter in range(1, len(options)):
            self.numVotes.update({counter:0})

    #tallies a vote on a given choice if is a valid Vote
    def vote( voter, voteIDX ):
        global options 
        global numVotes
        if not validVote(voter): 
            return False
        else: 
            self.umVotes[int(voteIDX)] += 1 
  
    #find the winner of the poll 
    def find_winners(): 
        highest = []
        most = 1
        for key, value in self.numVotes.items():
            if value >= most:
                highest.append(key)
        return highest

