"""
Missing Numbers
You are given a list of whole numbers in ascending order. You need to find which numbers are missing in the sequence.



Task: 
Create a program that takes in a list of numbers and outputs the missing numbers in the sequence separated by spaces.

Input Format: 
The first input denotes the length of the list (N). The next N lines contain the list elements as integers. 

Output Format: 
A string containing a space-separated list of the missing numbers.

Sample Input: 
5
2
4
5
7
8

Sample Output: 
3 6

Explanation: 
The input list is missing the numbers 3 and 6.
"""
#user
n = int(input())
w = [int(input()) for _ in range(n)]
f = w[0]
l = w[-1]
w = set(w)
r = [i for i in range(f,l+1)]
r = set(r)
a = w.symmetric_difference(r)
a = list(map(str,a))
a = ' '.join(a)
print(a)