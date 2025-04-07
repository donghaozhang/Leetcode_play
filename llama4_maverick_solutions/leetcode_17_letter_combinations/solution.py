def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []

    # Mapping of digits to their corresponding letters
    phone_mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(combination, next_digits):
        # If there is no more digits to process, append the current combination to the output
        if len(next_digits) == 0:
            output.append(combination)
        # Otherwise, process the next available digit
        else:
            for letter in phone_mapping[next_digits[0]]:
                # Recursively call the function with the current combination and the remaining digits
                backtrack(combination + letter, next_digits[1:])

    output = []
    backtrack("", digits)
    return output

# Test Cases
print(letterCombinations("23"))  # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations(""))    # Expected: []
print(letterCombinations("2"))   # Expected: ["a","b","c"]
