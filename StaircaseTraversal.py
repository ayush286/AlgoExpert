# O(h*m) Time | O(h) Space, where h is height and m is length of maxSteps
def staircaseTraversal(height, maxSteps):
    # Write your code here.
	
	steps = [0 for _ in range(height + 1)]
	steps[0] = 1
	for index in range(1, height + 1):
		x = index - maxSteps 
		if x < 0:
			x = 0
		steps[index] = (sum(steps[(x):index]))
	return steps[height]	
