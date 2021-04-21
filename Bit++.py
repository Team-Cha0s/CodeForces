"""
Sample Input:
1
++X
"""
"""
Sample Output:
1
"""

N = int(input())
integer = 0

for i in range(N):
    bit = input()
    if "+" in bit:
        integer += 1
    else:
        integer -= 1
        
print(integer)
    
#Accepted
#Time = 62 ms    
    