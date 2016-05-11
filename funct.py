#!/usr/bin/python

# A function that takes 2 strings, one dict and other arguments that can be passed any value

def lion_room(door1="one", door2="two", "door3":'dead', *args): 
    print "Choose door to start the game:
    
    
    next = raw_input("> ")
    if "door1" in next:
        enter_room()
    elif "door2" in next:
        jungle_room()
    elif "door3" in next:
        print "Man, you are dead!"
    else:
        print "You need to read the rules man"



#creating the enter  function (door1) that allows player to continue with the game

def enter_room():
    print "Now you are in the room"
    print "you need to look for the hidden treasure"
    
    next =  raw_input("> ")
    if "ceil" in  next:
       burnt("No treasure for you. You are burnt!")
    elif "floor" in next:
       print "Hurray! take your treasure"
    else:
        lion_room()
        
def jungle_room():
    print "You are in the jungle"
    print "it is either you leave or try"
     
    next =  raw_input("> ")
    if "leave" in  next:
       burnt("No treasure for you. You are burnt!")
    elif "try" in next:
       find_treasure()
    else: 
        jungle_room()

        
def find_treasure():
    print "Look for the treasure"
    Print "kindly choose 'oak tree' or 'highland' to play"
    
    next = raw_input("> ")
    if "oak tree" in next:
        burnt("No treasure for you. You are burnt!")
    elif "highland" in next:
        print "Hurray! take your treasure"
    else:
        find_treasure()
        


def burnt():
    print "Bye.Good luck next time"
    exit(0)
     
lion_room()
    


