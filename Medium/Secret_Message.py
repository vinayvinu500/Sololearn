"""
Secret Message
You are trying to send a secret message, and you've decided to encode it by replacing every letter in your message with its corresponding letter in a backwards version of the alphabet. 

What do your messages look like?


Task: 
Create a program that replaces each letter in a message with its corresponding letter in a backwards version of the English alphabet.

Input Format: 
A string of your message in its normal form.

Output Format: 
A string of your message once you have encoded it (all lower case).

Sample Input: 
Hello World

Sample Output: 
svool dliow

Explanation: 
If you replace each letter in 'Hello World' with the corresponding letter in a backwards version of the alphabet, you get 'svool dliow'.
"""
#user input
user = input().lower().split()
#alphabets
low = "abcdefghijklmnopqrstuvwxyz"
rev = low[::-1]
#dictionary
x = len(low)
d = {}
for i in range(x):
        d[low[i]] = rev[i]
        pass
#for loop integration
ou = []
str = ""
for i in user:
    for j in i:
        s = d[j]
        str += s
    ou.append(str)
    str = ""
ou = " ".join(ou)
print(ou)