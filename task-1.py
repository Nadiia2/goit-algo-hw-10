import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    
    return result

amount = 113
greedy_result = find_coins_greedy(amount)
print("Greedy result:", greedy_result)

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result


dp_result = find_min_coins(amount)
print("DP result:", dp_result)

greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
print("Greedy algorithm time:", greedy_time)

dp_time = timeit.timeit(lambda: find_min_coins(amount), number=1000)
print("Dynamic programming algorithm time:", dp_time)