"""
Days between dates
You need to calculate exactly how many days have passed between two dates.



Task:  
Calculate how many days have passed between two input dates, and output the result. 

Input Format: 
Two strings that represent the dates, first date should be the older date. 
Date format: Month DD, YYYY

Output Format: 
A number representing the number of days between the two dates.

Sample Input: 
August 15, 1979
June 15, 2018

Sample Output: 
14184

Explanation: 
14184 days have passed between the two input days.
"""
#imports
from datetime import date
import re

#data
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

#search
p = r'[a-zA-Z]+ [0-9]+, [0-9]+'

#match
a = re.search(p,input()).string.replace(',','').split()
b = re.search(p,input()).string.replace(',','').split()
a = int(a[2]),int(m[a[0]]),int(a[1])
b = int(b[2]),int(m[b[0]]),int(b[1])
#print(a)
#print(b)

#result
r = date(b[0],b[1],b[2]) - date(a[0],a[1],a[2])
print(r.days)

"""
Format : MM DD, YYYY
August 15, 1979
June 15, 2018
=> 14184
April 18, 1999
September 27, 2020
"""