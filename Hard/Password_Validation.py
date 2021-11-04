"""
Password Validation
You're interviewing to join a security team. They want to see you build a password evaluator for your technical interview to validate the input.



Task: 
Write a program that takes in a string as input and evaluates it as a valid password. The password is valid if it has at a minimum 2 numbers, 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*'), and a length of at least 7 characters.
If the password passes the check, output 'Strong', else output 'Weak'.

Input Format:
A string representing the password to evaluate.

Output Format:
A string that says 'Strong' if the input meets the requirements, or 'Weak', if not.

Sample Input: 
Hello@$World19

Sample Output: 
Strong

Explanation:
The password has 2 numbers, 2 of the defined special characters, and its length is 14, making it valid.
"""
#user input
user = input()
#length
le = len(user)
#characters 
char = ['!', '@', '#', '$', '%', '&', '*']
num = list(range(0,1000))
n = []
for i in num:
    n.append(str(i))
#alphabet
low ='abcdefghijklmnopqrstuvwxyz'
high = low.upper()
alpha = low + high
s = "Strong"
w = "Weak"
#only string
st = ""
for i in user:
    if i in alpha:
        st += i
st = len(st)
#only char
ch = []
for i in user:
    if i in char:
        ch.append(i)
ch = len(ch)
#only num
nu =[]
for i in user:
    if i in n:
        nu.append(i)
nu = len(nu)
#condition
if le >=7 and ch >= 2 and nu >= 2:
    print(s)
else:
    print(w)