
def tribonacci(n):
    return _tribonacci(n, {}) 

def _tribonacci(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0 
    
    if n == 1:
        return 0 

    if n == 2:
        return 1 

    memo[n] = _tribonacci(n-1, memo) + _tribonacci(n-2, memo) + _tribonacci(n-3, memo)
    return memo[n]

if __name__ == "__main__":
    # Test case 01 
    print(tribonacci(0)) # -> 0

    # Test case 02 
    print(tribonacci(1)) # -> 0

    # Test case 03
    print(tribonacci(2)) # -> 1

    # Test case 04
    print(tribonacci(5)) # -> 4

    # Test case 05
    print(tribonacci(7)) # -> 13

    # Test case 06
    print(tribonacci(14)) # -> 927

    # Test case 07
    print(tribonacci(20)) # -> 35890

    # Test case 08
    print(tribonacci(37)) # -> 1132436852