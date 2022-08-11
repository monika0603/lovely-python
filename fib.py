
def fib(n):
    return _fib(n, {}) 

def _fib(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0 

    if n == 1:
        return 1 

    memo[n] = _fib(n-1, memo) + _fib(n-2, memo) 
    return memo[n]

# Driver code 
# Test case 01
if __name__ == "__main__":
    print(fib(0)) # -> 0 

    # Test case 02 
    print(fib(1)) # -> 1

    # Test case 03 
    print(fib(2)) # -> 1

    # Test case 04 
    print(fib(46)) # -> 1836311903

    # Test case 05
    print(fib(35)) # -> 9227465

    # Test case 06 
    print(fib(5)) # -> 5