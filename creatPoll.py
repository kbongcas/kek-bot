voted = []
options = []
question = ""
numVotes = {}

def validVote(name):
    if any( name in s for s in voted ):
        return False 
    else:
        return True

def add2Voted(name):
    voted.append(name)

#add2Voted("kevin")
#print(validVote("kevin"))

def create_poll( poll_string ):
    split_poll_str(poll_string) 
    for counter in range(1, len(options)) :
        #print(counter,options[counter])
        numVotes.update({counter:0})

def split_poll_str( poll_string ):
    global options 
    options = poll_string.split("|") 
    global question
    question = options[0]

#create_poll("You gucci bro?? or noh ??|yah|notreally|sure|imreaddy")


def vote( voter, voteIDX ):
    global options 
    global numVotes
    if not validVote(voter): 
        print(voter, "cannot vote more than once.")
        return False
    else: 
        numVotes[int(voteIDX)] += 1 
        #print(numVotes[int(voteIDX)])
        add2Voted( voter )

#vote("kevooo", "1")
#vote("kevdfsfin", "2")


def find_winners(): 
    global numVotes
    highest = []
    most = 0
    for key, value in numVotes.items():
        if value >= most:
            most = value
    for key, value in numVotes.items():
        if value == most:
            highest.append(key) 
    return highest

#print(find_winners())



