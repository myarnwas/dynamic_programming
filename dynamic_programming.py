def coin_change(coins, amount):
    """
    حساب عدد الطرق المختلفة لتكوين المبلغ 'amount' باستخدام العملات المتوفرة في 'coins'.
    يستخدم البرمجة الديناميكية لبناء الحل.
    """
    # dp[i] = عدد الطرق لتكوين المبلغ i
    dp = [0] * (amount + 1)
    dp[0] = 1  # طريقة واحدة فقط لتكوين المبلغ 0 (عدم استخدام أي عملة)

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    ways = coin_change(coins, amount)
    print(f"Number of ways to make amount {amount} with coins {coins}: {ways}")
