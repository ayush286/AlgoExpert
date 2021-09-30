# O(n) Time | O(1) Space, where n is length of input array
def minNumberOfJumps(array):
    # Write your code here.
    index = 0
	jumps = 0
	while index < len(array):
		if index == len(array) - 1:
			return jumps
		maxJump = [0, 0]
		for jump in range(1, array[index] + 1):
			if index + jump >= len(array) - 1:
				return jumps + 1
			jumpCalculate = index + jump + array[index + jump]
			if maxJump[0] < jumpCalculate:
				maxJump[0] = jumpCalculate
				maxJump[1] = index + jump
		index = maxJump[1]
		jumps += 1
	return jumps
