"""
Average Word Length
You are in a college level English class, your professor wants you to write an essay, but you need to find out the average length of all the words you use. It is up to you to figure out how long each word is and to average it out.



Task: 
Takes in a string, figure out the average length of all the words and return a number representing the average length. Remove all punctuation. Round up to the nearest whole number.

Input Format: 
A string containing multiple words.

Output Format: 
A number representing the average length of each word, rounded up to the nearest whole number.

Sample Input: 
this phrase has multiple words

Sample Output: 
6

Explanation:
The string in question has five words with a total of 26 letters (spaces do not count). The average word length is 5.20 letters, rounding it up to the nearest whole numbers results in 6.
"""
import math
#user input
user = input().split()
#alphabets
low = "abcdefghijklmnopqrstuvwxyz"
high = low.upper()
alphabet = low + high
#len of the string
length = len(user)
#counter 
count = 0
#for loop
for x in user:
    for y in x:
        if y in alphabet:
            count+=1
#average the length of the string
avg = count / length
#round up to nearest integer
rounded = math.ceil(avg)
#printing the rounded integer
print(rounded)
"""
Examples
this phrase has multiple words =>6
can you not do that? =>3
the longest word in the dictionary is.... =>5
"""