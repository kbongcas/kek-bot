#Currently only works on linux-based machines 

import signal 

#max time to wait for input in seconds 
WAITTIME = 40

#handle the Alarm if wait time expires 
def timeExpired( signum, frame ):
    print("TIMED OUT!")
    raise TimeOutException

signal.signal(signal.SIGALRM, timeExpired)

def attemptInput():
    try:
        #print("You have seconds to enter an input." WAITTIME)
        userInput = input()
        return userInput
    except: 
       #If Alarm goes off 
        return None

#set the alarm 
signal.alarm(WAITTIME)

attemptInput() 

#no interrupt, thus turn alarm off 
signal.alarm(0)

