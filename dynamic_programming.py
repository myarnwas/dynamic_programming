def LIS_length(arr):
    n = len(arr)
    dp = [1] * n  # dp[i] = طول LIS الذي ينتهي عند i

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp, max(dp)

if __name__ == "__main__":
    arr = [23, 4, 1, 2, 3, 1]
    dp, max_len = LIS_length(arr)

    print("DP table:", dp)
    print("Length of LIS:", max_len)
