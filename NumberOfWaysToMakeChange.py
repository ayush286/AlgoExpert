#O(n*d) Time | O(n) Space, where d is length of denoms and n is input n
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [ 0 for index in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for wayIdx in range(1, len(ways)):
            remainder = wayIdx - denom
            if remainder >= 0:
                ways[wayIdx] += ways[wayIdx - denom]
    return ways[n]
