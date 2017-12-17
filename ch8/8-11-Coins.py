def makeChange(n, coins, table):
    if n == 0:
        #print("Exactly")
        return 1
    if n < 0:
        #print("Impossible")
        return 0
    if len(coins) == 0:
        #print("No coins")
        return 0

    head = coins[0]
    if (n,head) in table.keys():
        return table[(n,head)]

    upper = n // head
    table[(n, head)] = 0
    #print("head: {}\tUpper:{}".format(head, upper))

    for i in range(upper + 1):
        #print("({} with {}): <- ({} with {} {}): {}".format(n,head, n-i*head, i, head,coins))
        table[(n, head)] += makeChange(n-i*head, coins[1:], table)
    #print("** Result of ({}, {}):".format(n, head), table[(n, head)])
    return table[(n, head)]

if __name__ == "__main__":
    n,m = list(map(int, input().strip().split()))
    coins = list(map(int, input().strip().split()))
    #print("coins", coins)
    table = dict()
    result = makeChange(n, coins, table)
    #result = makeChange(0, [2,3], table)
    print(result)
    #print(table[(n, coins[0])])

