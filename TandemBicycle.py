# O(n) Time | O(1) Speed, where n is length of redShirtSpeeds
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	totalSpeed = 0
	riders = len(redShirtSpeeds)
	if fastest:
		for index in range(riders):
			totalSpeed += max(redShirtSpeeds[index], blueShirtSpeeds[riders - index - 1])
	else:
		for index in range(riders):
			totalSpeed += max(redShirtSpeeds[index], blueShirtSpeeds[index])
	return totalSpeed
