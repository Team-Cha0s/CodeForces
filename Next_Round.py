"""
Sample Input:
8 5
10 9 8 7 7 7 5 5
"""
"""
Sample Output:
6
"""

NK = input().split()
K = int(NK[1])
Contestants = input().split()
Counter = 0

Kth_Place = int(Contestants[K-1])

for i in range(len(Contestants)):
    if int(Contestants[i]) >= Kth_Place and int(Contestants[i]) > 0:
        Counter += 1
        
print(Counter)
#Accepted
#Time = 154 ms