"""
The Spy Life
You are a secret agent, and you receive an encrypted message that needs to be decoded. The code that is being used flips the message backwards and inserts non-alphabetic characters in the message to make it hard to decipher.



Task: 
Create a program that will take the encoded message, flip it around, remove any characters that are not a letter or a space, and output the hidden message.

Input Format:  
A string of characters that represent the encoded message.

Output Format: 
A string of character that represent the intended secret message.

Sample Input: 
d89%l++5r19o7W *o=l645le9H

Sample Output: 
Hello World

Explanation: 
If you remove everything that isn't a letter or space from the original message and flip it around, you get 'Hello World'.
"""
#user input
msg = input()
msg = msg[::-1].split()
#decode msg
decode = ""
#length
l = len(msg)
#alphabets of small and captial
low  = "abcdefghijklmnopqrstuvwxyz"
high = low.upper()
alphabet = low + high
alphabet = ",".join(alphabet)
#function to remove non-alphabet
def code(str):
    s = ""
    for i in str:
        if i in alphabet:
            s+=i
    return s
#for-loop integration
for i in range(l):
    str = msg[i] 
    rearrange = code(str)
    msg[i] = rearrange

msg = " ".join(msg)
print(msg)
"""
previous method
#seperated with commas
msg = ",".join(msg)
#string reversed
msg = msg[::-1]
#decoded string
decode = ""
#alphabets of small and captial
low  = "abcdefghijklmnopqrstuvwxyz"
high = low.upper()
alphabet = low + high
alphabet = ",".join(alphabet)
#for-loop integration
for i in msg:
    if i in alphabet:
        #print(i)
        decode+=i

decode = " ".join(decode)
print(decode)
"""
"""
Examples
d89%l++5r19o7W *o=l645le9H => ''Hello World
1s2o3c4a5t => tacos
"""