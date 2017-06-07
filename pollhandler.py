import creatPoll
import poll

user1 = "kevin" 
user2 = "steve" 
user3 = "mark" 
user4 = "shaq" 


string2parse = "Did I just make a python program?|yah|notreally|sure|imreaddy"

poll1 = poll.Poll()
poll1.create_poll(string2parse)
poll1.vote("steveen","1")
poll1.vote("steveen","2")
poll1.vote("sddteveen","4")
print(poll1.find_winners())

print(poll1.give_results())
print(poll1.give_poll())
