"""
Sample Input:
3+2+1
"""
"""
Sample Output:
1+2+3
"""

Calc = list(input())
del Calc[1::2]
Calc = list(map(int, Calc))
Calc.sort()
Calc = list(map(str, Calc))
Calc = list('+'.join(Calc))
print(''.join(Calc))

#Accepted
#Time = 124 ms
