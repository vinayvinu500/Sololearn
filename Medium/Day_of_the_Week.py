"""
Day of the Week
You receive a date and need to know what day of the week it is. 

 

Task: 
Create a program that takes in a string containing a date, and outputs the day of the week.

Input Format: 
A string containing a date in either "MM/DD/YYYY" format or "Month Day, Year" format.

Output Format: 
A string containing the day of the week from the provided date.

Sample Input: 
11/19/2019

Sample Output: 
Tuesday

Explanation: 
19 November 2019 is a Tuesday.
"""
#imports
import re
import datetime

#data
w = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
}

m = {
    'January':'01',
    'February':'02',
    'March':'03',
    'April':'04',
    'May':'05',
    'June':'06',
    'July':'07',
    'August':'08',
    'September':'09',
    'October':'10',
    'November':'11',
    'December':'12'
}

#user
u = input() 
p1 = r'../../....'
p2 = r'[a-zA-Z]+ [0-9]+, [0-9]+'

#Format MM/DD/YYYY or Month Date, Year
match = re.search(p1,u) if re.search(p1,u) is not None else re.search(p2,u)

if re.search(p2,u) is not None:
    a = match.string.replace(',','').split(' ')
    a = [int(a[1]),int(m[a[0]]),int(a[2])]
else:
    a = match.string.replace('/',' ').split()
    a = [int(a[1]),int(a[0]),int(a[2])]
#print(a)

#Format date(YYYY,MM,DD)
day = datetime.date(a[2],a[1],a[0])
day = day.strftime("%A")
print(day)

"""
Format
MM/DD/YYYY
12/30/2019
Month Date, Year
July 20, 2020
"""