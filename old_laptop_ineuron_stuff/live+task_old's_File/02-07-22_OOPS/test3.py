def peopleAwareOfSecret( n, delay, forget):
    mod = 10 ** 9 + 7
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n + 1):
        for j in range(max(1, i - forget + 1), i - delay + 1):
            dp[i] += (dp[j] % mod)
    ans = sum(dp[n - forget + 1:])
    return ans % mod

print(peopleAwareOfSecret(6,2,4))