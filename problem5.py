def problem5(items, capacity):
    n = len(items)
    K = [[0] * (n + 1) for _ in range(capacity + 1)]

    for j in range(1, n + 1):
        weight, value = items[j-1]
        for w in range(capacity + 1):
            if weight > w:
                K[w][j] = K[w][j-1]
            else:
                K[w][j] = max(K[w][j-1], K[w - weight][j-1] + value)

    return K[capacity][n]
