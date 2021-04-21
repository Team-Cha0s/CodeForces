"""
Sample Input:
3
1 1 0
1 1 1
1 0 0
"""
"""
Sample Output:
2
"""

N = int(input())
Overall = 0

for i in range(N):
    Var, Var1, Var2 = map(int,input().split())
    Counter = 0
    if Var == 1:
        Counter += 1
    if Var1 == 1:
        Counter += 1
    if Var2 == 1:
        Counter += 1
    if Counter > 1:
        Overall += 1
        
print(Overall)

    
#Accepted
#Time = 124 ms