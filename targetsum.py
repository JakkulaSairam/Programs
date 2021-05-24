# Python 3 program to find the number of 
# ways to calculate a target number using 
# only array elements and addition or 
# subtraction operator. 

# Function to find the number of ways to 
# calculate a target number using only 
# array elements and addition or 
# subtraction operator. 
def findTotalWays(arr, i, k): 

	# If target is reached, return 1 
	if (k == 0 and i == len(arr)): 
		return 1	

	# If all elements are processed and 
	# target is not reached, return 0 
	if (i >= len(arr)): 
		return 0

	# Return total count of three cases 
	# 1. Don't consider current element 
	# 2. Consider current element and 
	# subtract it from target 
	# 3. Consider current element and 
	# add it to target 
	return (findTotalWays(arr, i + 1, k) +
			findTotalWays(arr, i + 1, k - arr[i]) +
			findTotalWays(arr, i + 1, k + arr[i])) 
def countWays(A, n, target):
     
    # base case: if a target is found
    if target == 0:
        return 1
 
    # base case: no elements are left
    if n < 0:
        return 0
 
    # 1. ignore the current element
    exclude = countWays(A, n - 1, target)
 
    # 2. Consider the current element
    #    2.1. Subtract the current element from the target
    #    2.2. Add the current element to the target
    include = countWays(A, n - 1, target - A[n]) + countWays(A, n - 1, target + A[n])
 
    # Return total count
    return exclude + include

n,k=list(map(int,input().split()))
arr = list(map(int,input().split()))
print(countWays(arr, n-1, k))

	
# This code is contributed by 
# Surendra_Gangwar 
