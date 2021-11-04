"""
New Driver's License
You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license?



Task 
Given everyone's name that showed up at the same time, determine how long it will take to get your new license.

Input Format 
Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names separated by spaces.

Output Format 
You will output an integer of the number of minutes that it will take to get your license.

Sample Input
'Eric'
2
'Adam Caroline Rebecca Frank'

Sample Output 
40

Explanation 
It will take 40 minutes to get your license because you are in the second group of two to be seen by one of the two available agents.
"""

"""
Algorithm
case 1: if agents are one the alphetical order
case 2: if agents are more than one agents are busy with one person at a time
"""
#time taken to process each license
take = 20 #minutes
#user input
name = input() #name of current customer
agent = int(input()) #no of agents are available
others = input().split()
#alphabetical order
def alpha():
    n = others + [name]
    n.sort()
    return n
names = alpha()
#print(names)
""" condition """
#if agents are one
if agent == 1:
    #for each person time taken
    def time(ti):
        t = {}
        for i in names:
            t[i] = ti
            ti += 20
        return t
    time_taken = time(take)
    #final output
    def licensed():
        t = time_taken[name]
        return t
    driver = licensed()
    print(driver)
    pass
#if agents are more
elif agent == 2:
    #for each person time taken
    def person():
        total = 0
        x = len(names)
        x1 = names[0]
        x2 = names[1]
        x3 = names[2]
        x4 = names[3]
        x5 = names[4]
        if name is x1:
            total = 20
        elif name is x2:
            total = 20
        elif name is x3:
            total = 40
        elif name is x4:
            total = 40
        elif name is x5:
            total = 60
        return total
    driver = person()
    print(driver)
elif agent == 3:
    #for each person time taken
    def person():
        total = 0
        x = len(names)
        x1 = names[0]
        x2 = names[1]
        x3 = names[2]
        x4 = names[3]
        x5 = names[4]
        if name is x1:
            total = 20
        elif name is x2:
            total = 20
        elif name is x3:
            total = 20
        elif name is x4:
            total = 40
        elif name is x5:
            total = 40
        return total
    driver = person()
    print(driver)
elif agent == 4:
    #for each person time taken
    def person():
        total = 0
        x1 = names[0]
        x2 = names[1]
        x3 = names[2]
        x4 = names[3]
        x5 = names[4]
        if name is x1:
            total = 20
        elif name is x2:
            total = 20
        elif name is x3:
            total = 20
        elif name is x4:
            total = 20
        elif name is x5:
            total = 40
        return total
    driver = person()
    print(driver)
elif agent >=5:
    driver = take
    print(driver)
"""
Examples 
input =>
Eric
2
Adam Caroline Rebecca Frank
output =>
40

input =>
Zebediah
1
Bob Jim Becky Pat
output =>
100

input =>
Aaron
1
Jane Max Olivia Sam
output =>
20
"""
"""
if i is name:
total = count
elif not(i is name):
names.pop(index)
if i is name:
total= count
elif not(i is name):
names.pop(index+1)
count +=20
index +=1
"""