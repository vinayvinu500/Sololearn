"""
Word Rank
A word is a sequence of letters A-Z. Rearranging the letters in the word, you can come up with new words, composed of the same letters. 

For example, the letters in the word TESTING can be rearranged to result in SETTING.

If we sort all the words made up of the same set of letters alphabetically, we can calculate the rank of each word.  

Task:
Given a word (not limited to just "dictionary words"), calculate and output its rank among all the words that can be made from the letters of that word. The word can contain duplicate letters.

Input Format:
A string, representing a sequence of letters (A-Z).

Output Format:
An integer, representing the rank of the given word.

Sample Input:
ABAB

Sample Output:
2

Explanation: Let's create a list of all the words that can be made up of the letters of the input and sort them alphabetically:
1. AABB
2. ABAB
3. ABBA
4. BAAB
5. BABA
6. BBAA
The given word is number 2 in the list.
"""
#Word Rank = 1day (01/10/2020)

#imports
from functools import reduce
from collections import Counter
from math import factorial as fact

#user
n = list(input().upper())

#check
q = "Non-Repeat Characters" if len(set(n)) == len(n) else "Repeating Characters"

"""
#factorial
def fact(n):
    # 5! = 5 x 4 x 3 x 2 x 1 = 120.
    if n == 0:
        return 0
    else:
        a = list(range(1,n+1)) 
        b = reduce(lambda x,y: x*y,a)
        return b
"""

#Non-Repeating Characters 
def non_repeat(n):
    """Non-Repeating numbers"""
    a = sorted(list(n)) 
    w = {}
    for i,j in enumerate(a):
        w[j] = i+1
    b = [w[i] for i in n]
    c = []
    count = 0
    ab = 1
    #==========================#
    for i in range(len(b)):
        for j in range(ab,len(b)):
            if b[i] > b[j]:
                count += 1
        ab +=1
        c.append(count)
        count = 0
    #==========================#
    d = [fact(i) for i in range(len(c))][::-1]
    e = [c[i] * d[i] for i in range(len(n))]
    f = sum(e) + 1
    return f

#Repeating Characters 
def repeat(n):
    """Repeating numbers"""
    a = sorted(list(set(list(n))))
    w = {}
    for i,j in enumerate(a):
        w[j] = i+1
    b = [w[i] for i in n]
    c = []
    d = []
    count = 0
    ab = 1
    #==========================#
    for i in range(len(n)):
        d.append(n[i])
        for j in range(ab,len(n)):
            d.append(n[j])
            if b[i] > b[j]:
                count += 1
        #==========================#
        e = Counter(d)
        f = [fact(i) for i in e.values()]
        g = reduce(lambda x,y : x*y,f)
        #==========================#
        ab +=1
        c.append(count/g)
        d.clear()
        count = 0
    #==========================#
    del d,e,f,g
    d= [fact(i) for i in range(len(c))][::-1]
    e = [c[i] * d[i] for i in range(len(n))]
    f = int(sum(e)) + 1
    return f
    
#excution of function
result = 0
if q == "Non-Repeat Characters":
    result += non_repeat(n)
    
else:
    result += repeat(n)
    
#result
print(result)