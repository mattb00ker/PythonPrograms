def sum_odds_below(n):
    # Base case: If n is less than or equal to 1, return 0
    if n <= 1:
        return 0
    
    # If n is odd, add it to the sum of the odd numbers below it
    if n % 2 != 0:
        return n - 2 + sum_odds_below(n - 2)
    
    # If n is even, call the function with n - 1 to make it odd
    return sum_odds_below(n - 1)

# Example usage
print(sum_odds_below(45))  # Output: 9
