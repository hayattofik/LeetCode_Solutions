super_list=set(map(int,input().split()))
no_inputs=int(input())
check=True
for i in range(no_inputs):
    subset=set(map(int,input().split()))
    if len(subset)>=len(super_list):
        print(False)
        exit(0)
    
    count=0
    for num in subset:
        if num not in super_list:
            check=False