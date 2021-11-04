"""
Guard Flamingos
You decide to add a pink flamingo lawn ornament every 2 feet around the perimeter of your yard. How many flamingos do you need to purchase?



Task: 
Given the length and width of your rectangular yard, determine how many flamingos your should buy to put one every 2 feet along the edges of your yard.

Input Format: 
Two integer values that represent the length and width of your front yard.

Output Format: 
An integer that represents the total number of flamingos that you should purchase.

Sample Input: 
10
10

Sample Output: 
20

Explanation: 
The perimeter of your yard is 40 feet long. You will need 20 flamingos to place one every 2 feet.
"""

#user input 
l = int(input()) # feet
b = int(input()) # feet

#perimeter in yard
p = (l *2) + (b * 2) #feet

#flamingos
f = 2 #feet

#result
res = round(p / f)
print(res)