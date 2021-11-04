"""
Snowballing Numbers
You are given a list of numbers in a particular order. You need to check to see if each number is greater than the sum of all the previous number of the list.  

If they are, you have created successful snowball numbers.


Task: 
Create a program that takes in an array of numbers, check if each number is greater than the sum of all previous numbers, and output true if the condition is met, and false, if not.

Input Format: 
The first input denotes the length of the list (N). The next N lines contain the list elements as integers. 

Output Format: 
A string, true or false.

Sample Input: 
4
1
3
7
58

Sample Output: 
true

Explanation: 
Each number in the input list is greater than the sum of the previous numbers: 3>1, 7>3+1, 58>7+3+1
"""
#user
u = [int(input()) for _ in range(int(input()))]
#for-loop integration
a = []
for i in range(1,len(u)):
    s = [u[j] for j in range(i)]
    o = u[i] > sum(s)
    a.append(o)
if all(a):
    print('true')
else:
    print('false')