# Enter your code here. Read input from STDIN. Print output to STDOUT
def Union(A,B):
    return set(A + B)
NA = int(input())
A = list(map(int,input().split()))
NB = int(input())
B = list(map(int,input().split()))

print(len(Union(A,B)))