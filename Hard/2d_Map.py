"""
2D Map
You're given a representation of a 5x5 2D map, and if you can only move left, right, up, or down, determine how many moves you would have to make to get between two points on the map.



Task:
 Determine the total number of moves that are needed between two points on a map.  The points that you move between are marked with a P and the spaces in between are marked with X.

Input Format: 
A string that represents the 2D space starting at the top left.  Each level from top to bottom is separated by a comma.

Output Format: 
An integer that represents the total number of moves that you had to make.

Sample Input: 
XPXXX,XXXXX,XXXXX,XXXPX,XXXXX

Sample Output: 
5

Explanation:
The map looks as:
XPXXX
XXXXX
XXXXX
XXXPX
XXXXX

You had to move right 2 spaces, then down 3 spaces for a total of 5 moves.
"""
#user
u = input().split(',')
u = [list(i) for i in u]
c = 0
d = []
map = ''
for i in u:
    if 'P' in i:
        # if P are in same level
        if i.count('P') == 2:
            map +=  'S' #same_level
            l = i.index('P')
            d.append(l)
            i[l] = 'A'
            #two-way process
            l = i.index('P')
            d.append(l)
            i[l] = 'B'
            
        #if P are in another level
        else:
            k = i.index('P')
            d.append([k,c])
    #print(i) #printing
    c+=1
    
#print(d) #(index,column)
if map == 'S':
    e = abs(d[0] - d[1])
    print(e)
else:
    e = sum([abs(d[0][0]-d[1][0]),abs(d[0][1]-d[1][1])])
    print(e)
    
"""
XPXXX,XXXXX,XXXXX,XXXPX,XXXXX # 5
PPXXX,XXXXX,XXXXX,XXXXX,XXXXX # 1
PXXXX,XXXXX,XXXXX,XXXXX,XXXXP # 8
XXXPX,XXXXX,XXXXX,PXXXX,XXXXX # 6
"""