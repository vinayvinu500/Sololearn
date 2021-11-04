"""
Poker Hand
You are playing poker with your friends and need to evaluate your hand. 

A hand consists of five cards and is ranked, from lowest to highest, in the following way:

High Card: Highest value card (from 2 to Ace).
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: 10, Jack, Queen, King, Ace, in same suit. 

Task:
Output the rank of the give poker hand. 

Input Format: 
A string, representing five cards, each indicating the value and suite of the card, separated by spaces. 
Possible card values are: 2 3 4 5 6 7 8 9 10 J Q K A
Suites:  H (Hearts), D (Diamonds), C (Clubs), S (Spades)
For example, JD indicates Jack of Diamonds. 

Output Format:
A string, indicating the rank of the hand (in the format of the above description). 

Sample Input:
JS 2H JC AC 2D

Sample Output: 
Two Pairs

Explanation: The hand includes two Jacks and two 2s, resulting in Two Pairs.
"""

#data
v = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14} #values
s = ['H','D','C','S'] #suits
r = {
1:"One Pair",2:"Two Pairs",3:"Three of a Kind",4:"Four of a Kind",5:"Flush",6:"Straight Flush",7:"Royal Flush",8:"Straight",9:"Full House",10:"High Card"} #ranks

#function-integration

def one_pair(a):
    #Two cards of the same value.
    b = list(set([ (j,l) for i,k in a for j,l in a 
    if i == j and k != l ]))
    b = [''.join(i) for i in b]
    return len(b) == 2

def two_pair(a):
    #Two different pairs  
    b = list(set([ (j,l) for i,k in a for j,l in a 
    if i == j and k != l ]))
    c = [i for i,j in b]
    c = 0 if len(b) == 0 else c.count(c[0])
    b = list(set([''.join(i) for i in b]))
    return len(b) == 4 and c == 2

def three_kind(a):
    #Three cards of the same value. 
    b = list(set([ (j,l) for i,k in a for j,l in a 
    if i == j and k != l ]))
    b = list(set([''.join(i) for i in b]))
    return len(b) == 3
    
def four_kind(a):
    #Four cards of the same value.
    b = list(set([ (j,l) for i,k in a for j,l in a 
    if i == j and k != l ]))
    c = [i for i,j in b]
    c = 0 if len(b) == 0 else c.count(c[0])
    b = list(set([''.join(i) for i in b]))
    return len(b) == 4 and c == 4
    
def flush(a):
    #All cards of the same suit
    b = a[0][1]
    c = sorted([v[i] for i,k in a if b == k])
    d = sorted(range(min(c),max(c)+1))
    e = [j for i in c for j,k in v.items() if i == k]
    return len(e) == 5 and c != d

def straight_flush(a):
    #All cards are consecutive values of same suit.
    b = a[0][1]
    c = sorted([v[i] for i,k in a if b == k])
    d = sorted(range(min(c),max(c)+1))
    e = d == [10,11,12,13,14]
    f = [j for i in c for j,k in v.items() if i == k]
    return len(f) == 5 and c == d and not(e)
    
def royal_flush(a):
    #10, Jack, Queen, King, Ace, in same suit.
    b = a[0][1]
    c = sorted([v[i] for i,k in a if b == k])
    d = sorted(range(min(c),max(c)+1))
    e = d == [10,11,12,13,14]
    f = [j for i in c for j,k in v.items() if i == k]
    return len(f) == 5 and c == d and e
    
def straight(a):
    #All cards are consecutive values.
    b = all([a[i][1] != a[i+1][1] 
    for i in range(len(a)-1)])
    c = a[0][1]
    d = sorted([v[i] for i,k in a])
    e = sorted(range(min(d),max(d)+1))
    return b and d == e
    
def full_house(a):
    #Three of a kind and a pair.
    b = list(set([ (j,l) for i,k in a for j,l in a 
    if i == j and k != l ]))
    c = [i for i,j in b]
    d = list(set(c))
    d1 = 0 if len(b) == 0 else c.count(d[0])
    d2 = 0 if len(b) == 0 else c.count(d[-1])
    e = (d1 == 2 and d2 == 3) or (d1 == 3 and d2 == 2)
    b = list(set([''.join(i) for i in b]))
    return len(b) == 5 and e
    
def high_card(a):
    #Highest value card (from 2 to Ace).
    b = sorted([v[i] for i,j in a])
    c = max(b)
    d = [j for i in b for j,k in v.items() if i == k]
    return d[-1]
    

#conditional-integration
def cards(a):
    if one_pair(a):
        return r[1]
    elif two_pair(a):
        return r[2]
    elif three_kind(a):
        return r[3]
    elif four_kind(a):
        return r[4]
    elif flush(a):
        return r[5]
    elif straight_flush(a):
        return r[6]
    elif royal_flush(a):
        return r[7]
    elif straight(a):
        return r[8]
    elif full_house(a):
        return r[9]
    elif high_card(a):
        return r[10]
    else:
        return r[10]
        
#user
u = input().split()
a = [[i[0:-1],i[-1]] for i in u]

#result
print(cards(a))

"""
Examples
JS 2H JC KD 4S #one_pair
JS 2H JC AC 2D #two_pair
QS 8S QD 1C QH #three_kind
JD JC 2S JS JH #four_kind
AH QD AS QH QC #full_house
5C 2C KC AC 7C #flush
JC 10C 9C 8C 7C #straight_flush
10D 9S 8H 7D 6C #straight
AH QH 10H KH JH #royal_flush
AS 7D 4H 2C KD #high_card
"""