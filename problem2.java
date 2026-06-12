def problem2(revenues):
    if not revenues:
        return 0
    if len(revenues) == 1:
        return revenues[0]

    prev2, prev1 = revenues[0], max(revenues[0], revenues[1])

    for i in range(2, len(revenues)):
        prev2, prev1 = prev1, max(prev1, prev2 + revenues[i])

    return prev1
