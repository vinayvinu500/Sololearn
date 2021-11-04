""""
Task:

Given multiple words, you need to find the longest string that is a substring of all words. 


Input Format:
A string of words, separated by spaces. The string can also contain numbers.

Output Format:
A string, representing the longest common substring. 
If there are multiple longest common substrings, output the smallest one in alphabetical order.

Sample Input:
SoloLearn Learning LearningIsFun Learnable

Sample Output:
Learn

Explanation: 
Learn is the longest common substring for the words SoloLearn Learning LearningIsFun Learnable.
""""


#user
u = input().split()

#other code = wiki.longest_common_substring
def lcs(S,T): 
    m = len(S) 
    n = len(T) 
    counter = [[0]*(n+1) for x in range(m+1)] 
    longest = 0 
    lcs_set = set() 
    for i in range(m): 
        for j in range(n): 
            if S[i] == T[j]: 
                c = counter[i][j] + 1 
                counter[i+1][j+1] = c 
                if c > longest: 
                    lcs_set = set() 
                    longest = c 
                    lcs_set.add(S[i-c+1:i+1]) 
                elif c == longest: 
                    lcs_set.add(S[i-c+1:i+1]) 
    return lcs_set 
    
#result
if len(u) == 4:
    res1 = lcs(u[0],u[1])
    res2= lcs(u[2],u[3])
    res = lcs(list(res1)[0],list(res2)[0])
    print(list(res)[0])
else:
    res = lcs(u[0],u[1])
    print(list(res)[0])