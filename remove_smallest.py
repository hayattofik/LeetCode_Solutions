def remove_smallest(lis):
    lis.sort()
    left=0
    right=1
    while right<len(lis):
        if abs(lis[right]-lis[left])<=1:
            if lis[right]<lis[left]:
                lis.remove(right)
            else:
                lis.remove(left)
        else:
            left+=1
            right+=1
    if len(lis)<=1:
        return "YES"
    else:
        return "NO"
 
for i in range(int(input())):
    size=input()
    lis=list(map(int,input().split()))
    print(remove_smallest(lis))
