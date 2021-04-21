"""
Sample Input:
aaaa
aaaA
"""
"""
Sample Output:
0
"""

St1 = input().lower()
St2 = input().lower()

if St1 == St2:
    print(0)
elif St1 > St2:
    print(1)
else:
    print(-1)
    
#Accepted
#Time = 124 ms