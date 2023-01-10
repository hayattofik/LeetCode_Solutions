input_size = int(input())
for i in range(input_size):
    list_size = int(input())
    num_list = list(map(int,input().split()))
    let_lis =input()
    let_lis = list(let_lis)
   
 
    checkdict={}
    allfine= True
 
    for num in range(list_size):
        if num_list[num] not in checkdict:
            checkdict[num_list[num]] = let_lis[num]
    for j in range(list_size):
        if checkdict[num_list[j]] != let_lis[j]:
            allfine =False
    if allfine:
        print("YES")
    else:
        print("NO")
