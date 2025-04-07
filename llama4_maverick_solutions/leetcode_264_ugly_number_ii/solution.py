def nthUglyNumber(n: int) -> int:
    """
    Returns the n-th ugly number.

    Args:
    n (int): The index of the ugly number to return.

    Returns:
    int: The n-th ugly number.
    """
    # Initialize the list to store the ugly numbers
    ugly = [1]
    
    # Initialize the pointers for the next possible ugly numbers
    i2, i3, i5 = 0, 0, 0
    
    # Generate the next ugly numbers
    while len(ugly) < n:
        # Calculate the next possible ugly numbers
        next_ugly2, next_ugly3, next_ugly5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
        
        # Generate the next ugly number
        next_ugly = min(next_ugly2, next_ugly3, next_ugly5)
        
        # Add the next ugly number to the list
        ugly.append(next_ugly)
        
        # Update the pointers
        if next_ugly == next_ugly2:
            i2 += 1
        if next_ugly == next_ugly3:
            i3 += 1
        if next_ugly == next_ugly5:
            i5 += 1
    
    # Return the n-th ugly number
    return ugly[-1]

# Test cases
print(nthUglyNumber(10))  # Output: 12
print(nthUglyNumber(1))   # Output: 1
print(nthUglyNumber(1690))  # Output: 2123366400
