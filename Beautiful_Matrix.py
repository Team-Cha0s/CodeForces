"""
Sample Input:
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
"""
"""
Sample Output:
3
"""

Grid = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

Counter = 0

#Take care of input
for i in range(5):
    Grid[i] = list(map(int, input().split()))

#Taking care of the vertical part of the 2d list
if 1 in Grid[0]:
    Counter += 2
elif 1 in Grid[1]:
    Counter += 1
elif 1 in Grid[3]:
    Counter += 1
elif 1 in Grid[4]:
    Counter += 2
    
#Taking care of the horizontal part of the 2d list
for i in range(5):
    if 1 == Grid[i][0]:
        Counter += 2
    elif 1 == Grid[i][1]:
        Counter += 1
    elif 1 == Grid[i][3]:
        Counter += 1
    elif 1 == Grid[i][4]:
        Counter += 2
    
print(Counter)

#Accepted
#Time = 124 ms