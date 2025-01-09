coins = [1,2,5,10,20,50,100,200]
target = 200
def count_ways(coins, target):
    if target == 0:
        return 1
    if target < 0 or not coins:
        return 0
    return count_ways(coins, target - coins[0]) + count_ways(coins[1:], target)

print(count_ways(coins, target))
