def count_ways(n):
    
    if n <= 0:
        return 0
    if n == 1:
        return 1

    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]



n = int(input("계단의 개수를 입력하시오: "))


result = count_ways(n)
print(f"{n}개의 계단을 오르는 방법의 수는 {result}가지입니다.")