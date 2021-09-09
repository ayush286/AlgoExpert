def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    denoms.sort()
	minChange = minNumberOfCoinsForChangeHelper(n, denoms, 0, {})
	return minChange if minChange is not None else -1
# O(n * m) Time | O(n) Space where n is input and m is length of denoms	
def minNumberOfCoinsForChangeHelper(n, denoms, depth, memo):
	if n in memo:
		return memo[n]
	if n < 0:
		return
	if n == 0:
		return depth
	minDepth = None
	for denom in reversed(denoms):
		remainder = n - denom
		depthReceived = minNumberOfCoinsForChangeHelper(remainder, denoms, depth + 1, memo)
		if depthReceived is not None:
			if minDepth is None:
				minDepth = depthReceived
			else:
				minDepth = min(depthReceived, minDepth)
	memo[n] = minDepth
	return minDepth
