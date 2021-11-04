"""
Hex Color Code Generator
You are starting a new company and unfortunately that means you can no longer rely on the free hex-color code software you used to rely on. It’s time to put your skills to the test and create one from the ground up!



Task: 
Create a function that accepts three integers that represent the RGB (red, green, blue) values and outputs the hex-code representation.

Input Format: 
Three integers that represent RGB values.

Output Format: 
The hexadecimal color code string that corresponds with the entered RGB values.

Sample Input: 
100 
200 
233

Sample Output: 
#64c8e9

Explanation: 
Hex color codes work within 15 characters, 0-9 and a-f. RGB goes into hex color codes as such # (red) 00 (green) 00 (blue) 00. Hex color codes work by rolling over the value of 09 to 0a. Once 0f is hit (15) the following value (16) would be represented as 10 instead of (16). This means the RGB values (16, 32, 161) would evaluate to #1020a1 (10, 20, a1).
"""
#user
r = int(input())
g = int(input())
b = int(input())

#calculation
d = {0:0,
1:1,
2:2,
3:3,
4:4,
5:5,
6:6,
7:7,
8:8,
9:9,
10:'a',
11:'b',
12:'c',
13:'d',
14:'e',
15:'f'}
#first part
r1 = r // 16
g1 = g // 16
b1 = b // 16
#second part
r2 = int(((r / 16) - (r // 16))* 16)
g2 = int(((g / 16) - (g // 16)) * 16)
b2 = int(((b / 16) - (b // 16)) * 16)

#result
#print(r1,r2,g1,g2,b1,b2)
#print(d[r1],d[r2],d[g1],d[g2],d[b1],d[b2])
print(f'#{d[r1]}{d[r2]}{d[g1]}{d[g2]}{d[b1]}{d[b2]}')