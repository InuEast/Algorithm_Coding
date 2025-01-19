n = int(input())
time = sorted(map(int, input().split()))
wait = 0
result = 0

for i in range(n):
    wait += time[i]
    result += wait

print(result)