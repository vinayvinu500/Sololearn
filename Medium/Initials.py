"""
Initials
You are given a list of names for a fundraiser, but you need to keep the names relatively anonymous. You are tasked with getting the initials for each name provided.



Task: 
Given a list of first and last names, take the first letter from each name to create initials and output them as a space-separated string.

Input Format: 
The first input denotes the number of names in the list (N). The next N lines contain the list elements as strings. 

Output Format: 
A string containing the initials of each name in the original list, separated by spaces.

Sample Input: 
3 
Nick Dunburry
Tommy Newborne
David James

Sample Output: 
ND TN DJ

Explanation:
Taking the first letter from each name results in the output ND TN DJ.
"""
#user
n = int(input())
i = [input().split() for i in range(0,n)]
a = []
for j in range(0,len(i)):
    a.append([i[j][0][0],i[j][1][0]])
b = []
for i in range(0,len(a)):
    u = a[i][0] + a[i][1]
    b.append(u)
b = ' '.join(b)
print(b)