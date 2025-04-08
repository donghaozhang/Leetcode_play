def letterCombinations(digits):
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, current_combination):
        if index == len(digits):
            result.append(''.join(current_combination))
            return
        
        current_digit = digits[index]
        for letter in digit_to_letters[current_digit]:
            current_combination.append(letter)
            backtrack(index + 1, current_combination)
            current_combination.pop()
    
    backtrack(0, [])
    return result
