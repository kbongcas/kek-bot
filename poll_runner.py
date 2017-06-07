import threading
import poll
import time 

def split():
    time.sleep(5)

if __name__ == "__main__":

    string2parse = "Did I just make a python program?|yah|notreally|sure|imreaddy"
    poll1 = poll.Poll()
    poll1.create_poll(string2parse)

    t = threading.Thread(target=split, args=()) 
    t.start()
    poll1.vote("kevin","1")
    t.join()

    print(poll1.vote("steve","2"))
