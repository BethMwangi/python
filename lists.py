#!/usr/bin/python

the_count = [1, 2, 3, 4, 5, 6]
fruits = ['apples', 'oranges','pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#the for loop used below goes through a list
for number in the_count:
    print "This is count %d" %number
    
for fruits in fruits:
    print "A fruit of type %s" % fruits

#it is possible to go through mixed lists as well 
#however, % (raw data) has to be used since we do not know what is in it

for i in change:
    print "I got %r" % i
    
#building an empty list
elements = [ ]

#using the range function to do 0 to 6 counts

for i in range(0, 7):
    print "Adding %d to the list." % i
    #append function that adds an element to a list
    elements.append(i)
    
#printing them out 
for i in elements:
    print "Elements was %d" % i   














    
    
    
    
    
    
    
    
    
    
    


