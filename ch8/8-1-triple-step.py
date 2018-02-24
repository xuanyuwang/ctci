def solve_recursion(n, memo):
    """
    Dynamic programming in a recursive way.
    The problem is that if the n is very large, the call-stack will be very deep,
    even beyond the limit of Python can provide.
    """
    if n == 1 or n == 2 or n == 3:
        return memo[n]
    else:
        if memo[n-1] == 0:
            memo[n-1] = solve_recursion(n-1, memo)
        if memo[n-2] == 0:
            memo[n-2] = solve_recursion(n-2, memo)
        if memo[n-3] == 0:
            memo[n-3] = solve_recursion(n-3, memo)
        memo[n] = memo[n-1] + memo[n-2] + memo[n-3]
    return memo[n]

def solve_iter(n, memo):
    """
    Dynamic programming in a down-top way.
    The function can be enhanced by only store three elements, which can save sapce usage.
    """
    if n == 1 or n == 2 or n == 3:
        return memo[n]
    else:
        for i in range(4, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]

def tripleStep(n):
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4
    # result = solve_recursion(n, memo)
    result = solve_iter(n, memo)
    return result

if __name__ == "__main__":
    print(tripleStep(4))
    print(tripleStep(5))
    print(tripleStep(5000))
