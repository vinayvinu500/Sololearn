"""
That's odd...
You want to take a list of numbers and find the sum of all of the even numbers in the list. Ignore any odd numbers.



Task:
Find the sum of all even integers in a list of numbers.

Input Format: 
The first input denotes the length of the list (N). The next N lines contain the list elements as integers.

Output Format: 
An integer that represents the sum of only the even numbers in the list.

Sample Input: 
9
1
2
3
4
5
6
7
8
9

Sample Output: 
20

Explanation: 
If you add together 2, 4, 6, and 8 from the list, you get a sum of 20.
"""

list = []
n = 0
for i in range(int(input())):
    line = int(input())
    list.append(line)

for x in list:
    if x%2==0:
        n+=x
print(n)
"""
N = []
list = 0
line = int(input())
for i in range(line):
    N.append(i)
    if i%2==0:
        list+=i
print(list)

#examples
string 1
5 190 88 43 63
string 2
1 191
"""