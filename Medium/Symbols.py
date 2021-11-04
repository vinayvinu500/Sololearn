"""
Symbols
There is a problem with your keyboard: it randomly writes symbols when you are typing a text. You need to clean up the text by removing all symbols.



Task: 
Take a text that includes some random symbols and translate it into a text that has none of them. The resulting text should only include letters and numbers.

Input Format: 
A string with random symbols.

Output Format: 
A string of the text with all the symbols removed.

Sample Input: 
#l$e%ts go @an#d@@ g***et #l#unch$$$

Sample Output: 
lets go and get lunch

Explanation: 
If you take out every symbol and leave only the letters and numbers, your text says 'lets go and get lunch'.
"""
#user input
user = input().split()
#alphabet with numbers
low = "abcdefghijklmnopqrstuvwxyz"
#for loop for numbers
num = ""
for i in range(0,1000):
    num += str(i)
high = low.upper()
alphabet = low + high + num
#for loop integration
index = 0
length = len(user)
item = ""
User = []
for x in range(length):
    for i in user[x]:
        if i in alphabet:
            item += i
    User.append(item)
    item = ""
User = " ".join(User)
print(User)

"""
Examples
#l$e%ts go @an#d@@ g***et #l#unch$$$
lets go and get lunch
H&i ##########Jenn$$$ifer@@@ 42
Hi Jennifer 42
L#ive L@augh L%%ove
Live Laugh Love
"""        