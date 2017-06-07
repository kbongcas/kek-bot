#Class that represents a Poll
class Poll:

    def __init__ (self ):
        self.prev_Voted = []
        self.poll_choices = []
        self.poll_question = ""
        self.choice_tally = {}
        self.poll_is_open = True
        
    #determine if a voter has already voted
    def validVote(self, voter ):
        if any( voter in s for s in self.prev_Voted ):
            return False 
        else:
            return True

    #add voter to previously voted list 
    def add2Voted( self, voter ):
        self.prev_Voted.append( voter )

    #split a string using "|" as the split indicator
    def split_poll_string( self, poll_as_string ):
        self.poll_choices = poll_as_string.split("|") 
        self.poll_question = self.poll_choices[0]

    #creates the format of the pol
    def create_poll(self, poll_as_string ):
        self.split_poll_string( poll_as_string ) 

        #initialize each choice with 0 votes 
        for counter in range(1, len(self.poll_choices)):
            self.choice_tally.update({counter:0})

    #tallies a vote on a given choice if is a valid Vote
    def vote(self, voter, voteIDX ):
        if not self.validVote(voter) and self.poll_is_open is True:
            return False
        else: 
            self.choice_tally[int(voteIDX)] += 1 
            self.add2Voted(voter)
  
    #find the winner of the poll 
    def find_winners(self): 
        highest = []
        most = 0
        for key, value in self.choice_tally.items():
            if value > most:
                most = value
        for key, value in self.choice_tally.items():
            if value == most:
                highest.append(key) 
        return highest

    #close the poll(unable to vote)
    def close_poll(self):
        self.poll_is_open = False

    #shows the options and their tallies
    def give_results(self):
        results = ""
        for key, value in self.choice_tally.items():
            results += str(key) + " "
            results += self.poll_choices[key]
            results += ": " 
            results += str(value) + "\n"
        return results
            
    def give_poll(self):
        pollstr = ""
        pollstr += self.poll_question + "\n"
        for counter in range(1, len(self.poll_choices)) :
            pollstr += str(counter) + " " 
            pollstr += self.poll_choices[counter] + "\n"
        return pollstr


