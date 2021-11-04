"""
Halloween Candy
You go trick or treating with a friend and all but three of the houses that you visit are giving out candy. One house that you visit is giving out toothbrushes and two houses are giving out dollar bills. 



Task
Given the input of the total number of houses that you visited, what is the percentage chance that one random item pulled from your bag is a dollar bill? 

Input Format 
An integer (>=3) representing the total number of houses that you visited. 

Output Format
A percentage value rounded up to the nearest whole number.

Sample Input
4

Sample Output 
50

Explanation 
If you visited four houses, one would be candy, two would be dollars, and one would be a toothbrush. A 2 in 4 chance is 50%.
"""

from math import ceil
#user input
u = int(input())
r = ceil(100 * (2.0/u))
print(r)
"""
#previous
#input user
houses = int(input())
#your code goes here
dollar = houses//2
toothbrush = 1
candy = 1
#collection
treats = dollar + toothbrush + candy
#percentage
perc = 100 // dollar
#calculation
calc = houses - treat
"""
"""
Examples
input => 4, 3 , 10
expect =>50, 67 , 20
"""