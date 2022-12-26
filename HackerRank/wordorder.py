# Enter your code here. Read input from STDIN. Print output to STDOUT
size=int(input())
countDic={}
for i in range(size):
    take=input()
    if take in countDic:
        countDic[take]+=1
    else:
        countDic[take]=1
print(len(countDic))
output=list(countDic.values())
for outp in output:
    print(outp,end=" ")