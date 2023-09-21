#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # table create
        dp =[[-1 for _ in range(W+1)] for _ in range(n+1)]
        return self.helperfunc(W, wt, val, n,dp)
    
    
    def helperfunc(self,W, wt, val, n,dp):    
        
        #base case
        if n==0 or W ==0:
            return 0
            
        #Return the value if its already in table
        if dp[n][W] != -1:
            return dp[n][W]
        
        # Recursive case    
        if wt[n-1] <= W:
        
            dp[n][W] = max(val[n-1] + self.helperfunc(W-wt[n-1],wt,val,n-1,dp),
            self.helperfunc(W,wt,val,n-1,dp))
        else:
            dp[n][W] = self.helperfunc(W,wt,val,n-1,dp)
            
        return dp[n][W]
            
            
# class Solution:
    
#     def __init__(self):
#         # Initialize the memoization table
#         self.dp = None
    
#     # Function to return max value that can be put in knapsack of capacity W.
#     def knapSack(self, W, wt, val, n):
#         # Initialize the dp table if it hasn't been initialized yet
#         if self.dp is None:
#             self.dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
        
#         # Base case
#         if n == 0 or W == 0:
#             return 0
        
#         # Return the stored value if it's already computed
        
#         if self.dp[n][W] != -1:
#             return self.dp[n][W]
        
#         # Recursive case
#         if wt[n - 1] <= W:
#             self.dp[n][W] = max(val[n - 1] + self.knapSack(W - wt[n - 1], wt, val, n - 1),
#                                 self.knapSack(W, wt, val, n - 1))
#         else:
#             self.dp[n][W] = self.knapSack(W, wt, val, n - 1)
        
#         return self.dp[n][W]




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends