N = int(input())

# [1] dp[n]: 1에서 n을 만들때 사용되는 연산의 최소회수
# [2] dp테이블 생성 및 초기화
dp = [0]*(N+1)
dp[1] = 0 # 1부터 시작하므로 이곳은 연산회수 0

for i in range(2, N+1):
    dp[i]=dp[i-1]+1
    if i%2==0: # 2의 배수인 경우에만 처리
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0: # 3의 배수인 경우에만 처리
        dp[i] = min(dp[i], dp[i//3]+1)
        
ans = dp[N]
print(ans)