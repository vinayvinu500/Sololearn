"""
Land Ho!
You are on a large ship and you put down anchor near a beautiful beach. There is a small boat ferrying passengers back and forth, and you get in line for it. How long will you have to wait to get to the beach? You know that 20 people can fit on the boat and each trip to shore takes 10 minutes each way.



Task: 
Determine your wait time if you know the total number of people ahead of you in line.  

Input Format: 
An integer that represents the total number of people ahead of you in line.

Output Format: 
An integer that represents the number of minutes that you will have to wait until you are standing on the beach.

Sample Input: 
15

Sample Output: 
10

Explanation: 
You can get on the boat right away if you are the 16th person in line, it takes 10 minutes on the boat to get to the beach.
"""
#user input
u = int(input())

"""
boat back and fourth to shore by 20 person per trip and time taken 10min to shore and return 10 min to back to ship
 """
#function of boat
def boat(u):
    r = round(u / 20) * 10
    r = r * 2 + 10
    return r

#boat per 20 person
c = 10 if u <=20 else boat(u)

#result
res = c
print(res)