#Solution 1
#O(n^2) Time | O(1) Space where n is number of cities
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
	for city in range(len(distances)):
		capacity = 0
		nextCity = city + 1
		capacity += (fuel[city] * mpg) - distances[city]
		citiesVisited = 0
		while capacity >= 0 and citiesVisited < len(distances):
			citiesVisited += 1
			currentCity = nextCity
			nextCity += 1
			if currentCity >= len(distances):
				currentCity -= len(distances)
			capacity += (fuel[currentCity] * mpg) - distances[currentCity]
			
		if citiesVisited == len(distances):
			return city


#Solution 2
#O(n) Time | O(1) Space where n is length of fuel list
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
	potentialValidCity = 0
	capacity = (fuel[0] * mpg) - distances[0]
	lowestCapacity = capacity 
	for index in range(1, len(fuel)):
		print("index or city name is: " + str(index))
		print(capacity)
		
		capacity = capacity + (fuel[index] * mpg) - distances[index]
		if capacity < lowestCapacity:
			lowestCapacity = capacity
			potentialValidCity = index
		
    if potentialValidCity + 1 < len(fuel):
		return potentialValidCity + 1
	else:
		return potentialValidCity - len(fuel) + 1
