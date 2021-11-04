"""
Argentina
You are in a hat store in Argentina! The prices are listed in US Dollars and Argentinian Pesos. You have both, but you want to make sure you pay the lower price! Do you pay in Dollars or Pesos? The exchange rate is 2 cents for every Peso.



Task 
Create a program that takes two prices and tells you which one is lower after conversion.

Input Format 
Two integer values, the first one is the price in Pesos and the second one is the price in Dollars.

Output Format 
A string that says which currency you should make the purchase in ('Dollars' or 'Pesos').

Sample Input 
4000
100

Sample Output 
Pesos

Explanation 
You should use Pesos to buy the hat since 4000 pesos is equal to $80.
"""
#user input
p = int(input())
d = int(input())

#currency
dol = "Dollars"
peo = "Pesos"

#exchange rate
rate = 2 #cents in dollars for every Peso

#conversion
pi = p * 2
di = p / d

if d > di:
    print(peo)
elif di <= 80:
    print(peo)
elif d < di:
    print(dol)
elif pi == 80:
    print(peo)