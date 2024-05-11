# first we make a question dictionary:

import time

now = time.ctime
QNA = {
    "hii": "hey",
    "how are you": "i am fine",
    "what is your name": " i am Bhagam",
    "who is your boss": "Rashmi sir is my boss",
    "what is the time Bhagam": now,
}

while True:
    Question = input("Enter your Question please: ")

    if(Question== "quit"):
        break
    
    else:
        print(QNA[Question])
    
