def zero_one_knapsack(cargo):
    capacity = 15
    dp = []

    for i in range(len(cargo) + 1):
        dp.append([])
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dp[i].append(0)
            elif cargo[i - 1][0] <= j:
                dp[i].append(
                    max(
                        cargo[i - 1][0] + dp[i - 1][j - cargo[i - 1][1]],
                        dp[i - 1][j],
                    )
                )
            else:
                dp[i].append(dp[i - 1][j])

    return dp[-1][-1]


cargo = [(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)]
print(zero_one_knapsack(cargo))
