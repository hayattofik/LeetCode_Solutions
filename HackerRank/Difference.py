# Enter your code here. Read input from STDIN. Print output to STDOUT

def Difference(A,B):
    count=0
    for num in A:
        if num not in B:
            count+=1
    return count
N=int(input())
A=set(map(int,input().split()))
N2 = int(input())
B = set(map(int,input().split()))
print(Difference(A,B))
        