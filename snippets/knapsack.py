def knapsack_0_1(weights, prices, weight_limit):
    num_items = len(weights)
    max_price = [0] * (weight_limit + 1)
    for i in range(num_items):
        for w in range(weight_limit, 0, -1):
            put_out = max_price[w]
            if weights[i] <= w:
                put_in = prices[i] + max_price[w - weights[i]]
            else:
                put_in = 0
            max_price[w] = max([put_out, put_in])
    return max_price[weight_limit]


def knapsack_unbounded(weights, prices, weight_limit):
    num_items = len(weights)
    max_price = [0] * (weight_limit + 1)
    put_out, put_in = 0, [0] * num_items
    for w in range(1, weight_limit + 1):
        put_out = max_price[w - 1]
        for i in range(num_items):
            if weights[i] <= w:
                put_in[i] = prices[i] + max_price[w - weights[i]]
            else:
                put_in[i] = 0
        max_price[w] = max([put_out, max(put_in)])
    return max_price[weight_limit]


print knapsack_0_1([4,5,6,2,2], [6,4,5,3,6],10)