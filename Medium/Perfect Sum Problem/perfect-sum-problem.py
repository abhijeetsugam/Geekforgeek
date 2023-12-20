#User function Template for python3
class Solution:
    def perfectSum(self, ar, n, sum):
        
        dp = [[0 for _ in range(sum + 1)] for _ in range(n + 1)]
        MOD = pow(10, 9) + 7
        
        # Populate base condition
        
        for i in range(0, n + 1):
            for j in range(0, sum + 1):
                if (i == 0):
                    dp[i][j]= 0
                if (j == 0):
                    dp[i][j]= 1                
            
        # Populate table
        for i in range(1, n + 1):
            for j in range(0, sum + 1):
                
                if ar[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-ar[i-1]])%MOD
                else:
                    dp[i][j] = dp[i-1][j] 
                    
        return dp[n][sum] 








#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends