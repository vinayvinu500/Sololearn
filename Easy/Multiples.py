"""
Multiples
You need to calculate the sum of all the multiples of 3 or 5 below a given number.



Task: 
Given an integer number, output the sum of all the multiples of 3 and 5 below that number. 
If a number is a multiple of both, 3 and 5, it should appear in the sum only once.

Input Format: 
An integer.

Output Format: 
An integer, representing the sum of all the multiples of 3 and 5 below the given input.

Sample Input: 
10

Sample Output:
23

Explanation: 
The numbers below 10 that are multiples of 3 or 5 are 3, 5, 6 and 9.
The sum of these numbers is 3+5+6+9=23
"""

#user input
u = int(input())
#multiples of 3
m3 = [i for i in range(0,u,3)]   
#multiples of 5
m5 = [i for i in range(0,u,5)]
#calculate 3 and 5
cal = m3 + m5
cal = list(set(cal))
#result
res = sum(cal)
print(res)