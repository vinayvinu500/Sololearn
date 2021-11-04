"""
Military Time 
You want to convert the time from a 12 hour clock to a 24 hour clock. If you are given the time on a 12 hour clock, you should output the time as it would appear on a 24 hour clock.  



Task:  
Determine if the time you are given is AM or PM, then convert that value to the way that it would appear on a 24 hour clock.

Input Format: 
A string that includes the time, then a space and the indicator for AM or PM.

Output Format: 
A string that includes the time in a 24 hour format (XX:XX)

Sample Input: 
1:15 PM

Sample Output: 
13:15

Explanation:
1:00 PM on a 12 hour clock is equivalent to 13:00 on a 24 hour clock.
"""

#user input
user = input().split()
time = user[0].split(":")
first = int(time[0])
second = time[1]
meri = user[1]

#meridian
if meri == "AM":
    d = {
    "00":12,
    1:"01",
    2:"02",
    3:"03",
    4:'04',
    5:"05",
    6:"06",
    7:"07",
    8:"08",
    9:"09",
    10:"10",
    11:"11",
    12:"00",
    13:"01",
    14:"02",
    15:"03",
    16:"04",
    17:"05",
    18:"06",
    19:"07",
    20:"08",
    21:"09",
    22:"10",
    23:"11",
    24:"00"
    }
    if first in d:
        first = d[first]
        first = str(first)
    pass
if meri == "PM":
    d = {
    "00":12,
    1:13,
    2:14,
    3:15,
    4:16,
    5:17,
    6:18,
    7:19,
    8:20,
    9:21,
    10:22,
    11:23,
    12:12,
    13:"01",
    14:"02",
    15:"03",
    16:"04",
    17:"05",
    18:"06",
    19:"07",
    20:"08",
    21:"09",
    22:"10",
    23:"11",
    24:"00"
    }
    if first in d:
        first = d[first]
        first = str(first)
    pass
    

#formation
time = first + ":" + str(second)
print(time)