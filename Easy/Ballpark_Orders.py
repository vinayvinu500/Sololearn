"""
Ballpark Orders
You and three friends go to a baseball game and you offer to go to the concession stand for everyone. They each order one thing, and you do as well. Nachos and Pizza both cost $6.00. A Cheeseburger meal costs $10. Water is $4.00 and Coke is $5.00. Tax is 7%.



Task 
Determine the total cost of ordering four items from the concession stand. If one of your friend’s orders something that isn't on the menu, you will order a Coke for them instead.

Input Format
You are given a string of the four items that you've been asked to order that are separated by spaces.

Output Format 
You will output a number of the total cost of the food and drinks.

Sample Input 
'Pizza Cheeseburger Water Popcorn'

Sample Output 
26.75

Explanation
Because Popcorn is not on the menu, this friend gets a coke which brings the subtotal to $25.00 and $26.75 with tax.
"""

#user input
user = input().split()
#items in dollars
menu = {"Nachos":6.00,"Pizza":6.00,"Cheeseburger":10,"Water":4.00,"Coke":5.00}
#Tax
Total = 0
Tax = 7
#for-loop integration
for i in user:
    if i in menu:
        Total+=menu[i]
    elif i not in menu:
        Total+=menu["Coke"]

#percentage
perc = (Tax/100)*Total
perc+=Total
print(perc)

"""
Example
Water Water Water Water=>17.12
Cheeseburger Cheeseburger coke water => 31.03
Pizza Cheeseburger Water Popcorn => 26.75
"""