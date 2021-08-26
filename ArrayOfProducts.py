#O(n) Time | O(n) Space where n is length of array
def arrayOfProducts(array):
    # Write your code here.
    leftProducts = [1 for elem in array]
	product = 1
	for index in range(len(array)):
		leftProducts[index] = product
		product *= array[index]
	product = 1
	for index in reversed(range(len(array))):
		leftProducts[index] *= product
		product *= array[index]
	return leftProducts
