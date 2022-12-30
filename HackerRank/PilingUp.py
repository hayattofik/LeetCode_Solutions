# Enter your code here. Read input from STDIN. Print output to STDOUT

input_size=int(input())
for i in range(input_size):
    block_size=int(input())
    
    block=list(map(int,input().split()))
    start=0
    end = block_size-1
    current=max(block[start],block[end])
    start=0
    end = block_size
    start+=1
    end-=1
    
    while(True):
       
        check_block = max(block[start],block[end])
        
        if start >= end:
            print("Yes")
            break
        elif check_block > current:
            print("No")
            break
        else:
            current=check_block
            start+=1
            end-=1
   
            
         
        
