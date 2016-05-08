#!/usr/bin/python

people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars"
elif cars < people:
    print "we shouldn't take cars"
else:
    print "We can't decide"
    
if buses > cars:
    print "That's too many buses"
elif buses < cars:
    print "Maybe we could take the buses"
else:
    print "we still can't decide"
    
if people > buses:
    print "Alright. let's just take the buses"
else:
    print "fine, let's stay at home"
    
if people > buses and people < cars:
    print "let's decide the means to use"
