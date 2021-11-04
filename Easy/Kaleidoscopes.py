"""
Kaleidoscopes
You sell souvenir kaleidoscopes at a gift shop, and if a customer buys more than one, they get a 10% discount on all of them!

Given the total number of kaleidoscopes that a customer buys, let them know what their total will be. Tax is 7%. All of your kaleidoscopes cost the same amount, 5.00.


Task: 
Take the number of kaleidoscopes that a customer buys and output their total cost including tax and any discounts.

Input Format: 
An integer value that represents the number of kaleidoscopes that a customer orders.

Output Format: 
A number that represents the total purchase price to two decimal places.

Sample Input: 
4

Sample Output: 
19.26

Explanation: 
A purchase of 4 kaleidoscopes would give the customer a 10% discount, then with tax the total is 19.26.
"""

#user input
u = int(input())
a = 5.00

#tax = 7%
#discount = 10% #morethan 1 kaleidoscopes

#calculate
c = u * a #amount
c = c + (c/100) * 7 #tax
c = c - (c/100)*10 if u > 1 else c

#result
res = round(c,2)
print(res)