"""
Sample Input:
2 4
"""
"""
Sample Output:
4
"""

MN = input().split()
M = int(MN[0])
N = int(MN[1])

Domino_area = 2 
Grid_area = M * N
Counter = Grid_area // Domino_area

print(Counter)

#Accepted
#Time = 124 ms