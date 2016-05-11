#!/usr/bin/python

#create mapping os state to abbreviation

states = [
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
]
#states with cities     
cities = [
      'CA':'San Francisco',
      'MI': 'Detroit',
      'FL': 'Jacksonville'
      ]

#adding more cities      
cities['NY'] = 'New york'
cities['OR'] = 'Portland'

#print cities
print '-' *10
print "NY State has: ", cities['NY']
print "OR states has: ", cities['OR']

#print statess
print '-' *10
print "Michigan's abbbreviation is: ", states['Michigan']

print '-' *10
print "Michigan has: ",cities[states['Michigan']]
print "Florida has: ",cities[states['Florida']]

print '-' *10
for state, abbrev in states.items():
    print "%s is abbreviated %s" %(state, abrrev)


print '-' *10
state = state.get('Texas', None)

if not state:
    print "sorry, no Texas"

























 
