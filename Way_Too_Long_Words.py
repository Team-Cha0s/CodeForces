"""
Sample Input:
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
"""
"""
Sample Output:
word
l10n
i18n
p43s
"""

N = int(input())
str1 = " " 

for i in range(N):
    The_Word = input()
    if len(The_Word) > 10:
        Temp_List = []
        list(The_Word)
        Temp_List.append(The_Word[0])  
        Temp_List.append(1)  
        Temp_List.append(The_Word[-1])
        Length = len(The_Word) - 2
        Temp_List[1] = Length    
        print(''.join(map(str, Temp_List)))
    else:
        print(The_Word)
        
#Accepted
#Time = 62 ms