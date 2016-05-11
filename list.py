#!/usr/bin/python

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "10 things in list"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "frisbee", "corn", "banana", "girl" , "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "adding:", next_one
    stuff.append(next_one)
    print "there is %d item now." % len(stuff)
    
print "there we go:", stuff

print "let's do some things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5])





























































