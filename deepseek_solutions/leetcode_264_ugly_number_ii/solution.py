def nthUglyNumber(n: int) -> int:
    ugly = [1]
    i2 = i3 = i5 = 0  # pointers for 2, 3, 5
    for _ in range(1, n):
        next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
        ugly.append(next_ugly)
        if next_ugly == ugly[i2] * 2:
            i2 += 1
        if next_ugly == ugly[i3] * 3:
            i3 += 1
        if next_ugly == ugly[i5] * 5:
            i5 += 1
    return ugly[-1]

# Test cases
print(nthUglyNumber(10))  # Output: 12
print(nthUglyNumber(1))   # Output: 1
