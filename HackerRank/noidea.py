# Enter your code here. Read input from STDIN. Print output to STDOUT
check_size,ABsize=map(int,input().split())
check_list=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
happy=0
for value in check_list:
    if value in A:
        happy+=1
    elif value in B:
        happy-=1
print(happy)
# n, m = map(int, input().split())
# happiness = 0
# elements = list(map(int, input().split()))
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# for i in elements:
#     if i in a:
#         happiness += 1
#     elif i in b:
#         happiness -= 1
# print(happiness)
