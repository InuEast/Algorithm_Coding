n = int(input())
coins = [500, 100, 50, 10, 5, 1]
rest = 1000 - n
count = 0

for coin in coins:
    count += (rest // coin)
    rest %= coin
    
print(count)