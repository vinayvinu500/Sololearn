"""
Hovercraft
You run a hovercraft factory. Your factory makes ten hovercrafts in a month. Given the number of customers you got that month, did you make a profit? It costs you 2,000,000 to build a hovercraft, and you are selling them for 3,000,000. You also pay 1,000,000 each month for insurance.



Task: 
Determine whether or not you made a profit based on how many of the ten hovercrafts you were able to sell that month.
 
Input Format: 
An integer that represents the sales that you made that month.

Output Format: 
A string that says 'Profit', 'Loss', or 'Broke Even'.

Sample Input: 
5

Sample Output: 
Loss

Explanation: 
If you only sold 5 hovercrafts, you spent 21,000,000 to operate but only made 15,000,000.
"""

'''
Understand
Hovercraft Business

Factory made => 10 (in Month)

Customers => 5 (in no’s)

Hovercraft => 2,000,000 (20 lakhs per each hovercraft) x 10 no’s => 2 Cr

Selling => 3,000,000 (30 lakhs per each hovercraft) x 5 no’s =>  1Cr 50 L

Insurance => 1,000,000 (10 lakhs )

Total = 2Cr 10 L - 1Cr 50L  = -6,000,000 (60 Lakhs) Loss

Profit =>
Loss => 6,000,000 (60 lakhs)
Broke Even =>

In month insurance is 10 lakhs and hovercraft are made 10 no’s and overall price for factory is 20 lakhs x 10 no’s => 2 crore

Factory sell the hovercraft at 30 lakhs for each and overall price for factory is 30 lakhs x 10 no’s => 3 crore

Manufacture by 10 hovercraft => 20 lakhs x 10 no’s = 2 crore + 10 lakhs = 21,000,000 (2Cr and 10lakh)
Profit made by selling 10 hovercraft => 30 lakhs x 10 no’s = 3 crore - 210 lakh = 9 lakhs (remaining profit)

But customers were 5 members to buy hovercraft which 10 - 5 = 5 no’s 

Customers => 5 x 3,000,000 = 15,000,000 (1Cr 50lakh) - 6,000,000 (60 lakh loss)
'''

#factory
manufacture_hovercraft = 10 # in month
insurance_hovercraft = 1000000 
build_hovercraft = 2000000
sell_hovercraft = 3000000

#manufacture
total_build_hovercraft = build_hovercraft * manufacture_hovercraft #building 10-hovercraft
#print(total_build_hovercraft )
cost_hovercraft = total_build_hovercraft + insurance_hovercraft #budget of build-hovercraft
#print(cost_hovercraft )

#assumption
total_sell_hovercraft = sell_hovercraft * manufacture_hovercraft #selling 10-hovercraft
#print(total_sell_hovercraft )

#strategies -> profit
total = total_sell_hovercraft  - total_build_hovercraft - insurance_hovercraft 
#print(total)

#customers
customers = int(input())
sell_customers = customers
sell_customers *= sell_hovercraft 
#print(sell_customers )

#customer-strategies
customers = manufacture_hovercraft  - customers 
#print(customers)

#sales
sales = sell_customers - cost_hovercraft  
#print(sales)

#results
p = "Profit"
l = "Loss"
b = "Broke Even"

#condition
#print(customers)
if customers >=4:
    print(l)
elif customers <=2:
    print(p)
elif customers == 3:
    print(b)
"""
customers 
0 => -21000000
1 => -18000000
2 => -15000000
3 => -12000000
4 => -9000000
5 => -6000000
6 => -3000000
7 => 0
8 => 3000000
9 => 6000000
10 => 9000000
"""
