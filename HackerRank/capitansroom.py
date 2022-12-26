# Enter your code here. Read input from STDIN. Print output to STDOUT
grp_size=int(input())
countDic={}
roomsize=list(map(int,input().split()))

for i in range(len(roomsize)):
    if roomsize[i] in countDic:
        countDic[roomsize[i]]+=1
    else: 
        countDic[roomsize[i]]=1

for key in countDic.keys():
    if countDic[key] != grp_size:
        print(key)