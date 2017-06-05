import creatPoll

user1 = "kevin" 
user2 = "steve" 
user3 = "mark" 
user4 = "shaq" 


string2parse = "Did I just make a python program?|yah|notreally|sure|imreaddy"
creatPoll.create_poll( string2parse) 
print("The string to be parsed: " ) 
print(string2parse)
print("")
print("The Polling Question is: ") 
print("")
print(creatPoll.question)
print("")
print("The Options are: ") 
for counter in range(1, len(creatPoll.options)) :
        print(counter,creatPoll.options[counter])

print("")
print(user1, " has voted: 1")
creatPoll.vote(user1, "1")
print(user1, " has voted: 2")
creatPoll.vote(user1, "2")
print(user2, " has voted: 1")
creatPoll.vote(user2, "1")
print(user3, " has voted: 4")
creatPoll.vote(user3, "4")
print(user4, " has voted: 4")
creatPoll.vote(user4, "4")

print("")
print("The winner is: ")
print(creatPoll.find_winners())



