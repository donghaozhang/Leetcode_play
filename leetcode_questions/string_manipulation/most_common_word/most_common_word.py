from typing import List

def most_common_word(paragraph: str, banned: List[str]) -> str:
    """
    Find the most frequent word in the paragraph that is not in the banned list.
    
    Args:
        paragraph: String containing words and punctuation
        banned: List of banned words
        
    Returns:
        The most frequent non-banned word (in lowercase)
    """
    # Replace all punctuation with spaces
    paragraph = paragraph.replace('!', ' ').replace('?', ' ').replace(';', ' ') \
                        .replace('.', ' ').replace(',', ' ').replace('\'', ' ')
    
    # Count word frequencies
    word_counts = {}
    for word in paragraph.split():
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Find the most frequent non-banned word
    max_count = 0
    result = ''
    for word, count in word_counts.items():
        if word not in banned and count > max_count:
            result = word
            max_count = count
    
    return result

# Test cases
if __name__ == "__main__":
    # Example 1
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    print(most_common_word(paragraph1, banned1))  # Output: "ball"
    
    # Example 2
    paragraph2 = "a."
    banned2 = []
    print(most_common_word(paragraph2, banned2))  # Output: "a"
    
    # Additional test case
    paragraph3 = "Bob. hIt, ball! BALL, flew? far; after. it. was hit."
    banned3 = ["hit", "bob"]
    print(most_common_word(paragraph3, banned3))  # Output: "ball" 