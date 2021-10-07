# O(nlogn) Time | O(1) Space, where n is length of coins 
def nonConstructibleChange(coins):
    # Write your code here.
    canConstructUpto = 0
	coins.sort()
	for coin in coins:
		if coin > canConstructUpto + 1:
			break
		else:
			canConstructUpto += coin
	return canConstructUpto + 1	

# O(n*n^n) Time | O(n) Space, where n is length of coins
def nonConstructibleChange(coins):
    # Write your code here.
	coins.sort()
    sumCoins = sum(coins)
	for index in range(sumCoins):
		isPossible = canConstruct(index, coins)
		if not isPossible:
			return index
	return sumCoins + 1

def canConstruct(target, coins):
	if target < 0:
		return False
	if target == 0:
		return True
	for index in range(len(coins)):
		newTarget = target - coins[index]
		if newTarget < 0:
			continue
		isPossible = canConstruct(newTarget, coins[:index] + coins[index + 1:])
		if isPossible:
			return True
	return False

