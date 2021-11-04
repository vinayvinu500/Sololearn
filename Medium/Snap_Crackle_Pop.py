"""
Snap, Crackle and Pop
You have six bowls of Rice Krispies in front of you, and they make different noises when you pour milk over them based on the total number of Rice Krispies in each bowl.

If a bowl has a number of Rice Krispies that is divisible by 3, it will make a Pop sound. If it is not divisible by 3 but is odd it will make a Snap sound.  If it is not divisible by 3, but it is even, it will make a Crackle sound.


Task: 
Based on the quantities in each bowl, output the noise that they make.

Input Format: 
You receive 6 integers and each integer represents the number of Rice Krispies in your bowls.

Output Format: 
You should output a string with the sounds made by each bowl separated by spaces in the order that they were input.

Sample Input: 
18
5
100
25
40
24

Sample Output: 
Pop Snap Crackle Snap Crackle Pop

Explanation: 
Each number divisible by 3 makes a pop sound. If not, the even numbers produce a Crackle, and the odd numbers produce a Snap.
"""

#user input of 6 integers
user = []
res = []
for i in range(6):
    a = int(input())
    user.append(a)
#even and odd
even = list(range(0,10000,2))
odd = list(range(1,10000,2))
#rice krispies
p = "Pop" # divisible by 3
s = "Snap" # not divisible by 3 and odd
c = "Crackle" # not divisible by 3 and even
#for- loop integration
for i in user:
    if i % 3 == 0:
        res.append(p)
    elif not i % 3 == 0 and i in even:
        res.append(c)
    elif not i % 3 == 0 and i in odd:
        res.append(s)
res = " ".join(res)
print(res)

"""
Example 
18,5,100,25,40,24 => p,s,c,s,c,p
1,2,3,4,5,6 => s,c,p,c,s,p
100,200,300,150,250,350 => c,c,p,p,c,c
"""