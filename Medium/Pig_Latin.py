"""
Pig Latin
You have two friends who are speaking Pig Latin to each other! Pig Latin is the same words in the same order except that you take the first letter of each word and put it on the end, then you add 'ay' to the end of that. ("road" = "oadray") 



Task
Your task is to take a sentence in English and turn it into the same sentence in Pig Latin! 

Input Format 
A string of the sentence in English that you need to translate into Pig Latin. (no punctuation or capitalization)

Output Format 
A string of the same sentence in Pig Latin.

Sample Input 
"nevermind youve got them"

Sample Output 
"evermindnay ouveyay otgay hemtay"

Explanation
The output should be the original sentence with each word changed so that they first letter is at the end and then -ay is added after that.
"""
#user input
user = input().split()
#pig latin
user_items = []
#functionality
def string(str):
    first = str
    letter = str[0]    
    string = str[1:]
    string += letter
    total = add(string)
    user_items.append(total)
def add(str):
    return str+"ay"    
#for-loop integration
for i in user:
    string(i)
user_items = " ".join(user_items)
print(user_items)
"""
nevermind youve got them
"""