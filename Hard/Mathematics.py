"""
Mathematics
Find which math expression matches the answer that you are given, if you have an integer answer, and a list of math expressions.



Task: 
Test each math expression to find the first one that matches the answer that you are given.

Input Format: 
Two inputs: an integer and a space separated string of math expressions. The following operations need to be supported: addition +, subtraction -, multiplication *, division /. 
An expression can include multiple operations.

Output Format: 
A string that tells the index of the first math expression that matches. If there are no matches, output 'none'.

Sample Input: 
15
(2+100) (5*3) (14+1)

Sample Output: 
index 1

Explanation: 
Index counting starts at 0, so '(5*3)' is at index 1 and matches your answer of 15.
"""
#user
n = float(input())
p = list(map(eval,input().split()))
p = list(map(float,p))
a = ' '
for i in range(len(p)):
    if n == p[i]:
        a += 'index '+ str(i)
a = a if a != ' ' else 'none'
print(a)