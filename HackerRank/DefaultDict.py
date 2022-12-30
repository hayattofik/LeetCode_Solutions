# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

A,B = map(int,input().split())
Adic=defaultdict(list)

for i in range(A): 
    letter=input()
    Adic[letter].append(str(i+1))
for j in range(B):
    letter=input()
    if letter in Adic.keys():
        print(' '.join(Adic[letter]))
    else:
        print(-1)

    