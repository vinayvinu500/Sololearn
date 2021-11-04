"""
Flowing Words
If a sentence flows, the first letter of each word will be the same to the last letter of the previous word. 



Task:
Write a program that takes in a string that contains a sentence, checks if the first letter of each word is the same as the last letter of the previous word. If the condition is met, output true, if not, output false. 
Casing does not matter.

Input Format: 
A string containing a sentence of words.

Output Format: 
A string: true or false.

Sample Input:
this string gets stuck

Sample Output: 
true

Explanation: 
Each word begins with the letter that the previous word ends with, therefore the output is true.
"""
#user
u = input().split()
t = 'true'
f = 'false'
#for-loop integration
a = []
for i in range(len(u)-1):
    o = u[i][-1].lower() == u[i+1][0].lower()
    a.append(o)
if all(a):
    print(t)
else:
    print(f)
"""
this string gets stuck
compatable koalas
Temporary yeild doesnt turn
"""