#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        p0= 0
        p1 = 1
        
        while(p1< len(arr)):
            if arr[p0]> arr[p1]:
                return 0
            p0 +=1
            p1 +=1
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends