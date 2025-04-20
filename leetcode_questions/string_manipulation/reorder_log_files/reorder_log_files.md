# Reorder Log Files

## Problem

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:
- Letter-logs: All words (except the identifier) consist of lowercase English letters.
- Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
1. The letter-logs come before all digit-logs.
2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3. The digit-logs maintain their relative ordering.

Return the final order of the logs.

## Approach

1. Define a custom sorting function that separates letter-logs and digit-logs.
2. For letter-logs, sort by content first, then by identifier.
3. For digit-logs, maintain their original order.
4. Sort the entire array using the custom sorting function.

## Solution

```python
def reorder_log_files(logs):
    def get_key(log):
        identifier, content = log.split(' ', 1)
        if content[0].isalpha():  # letter-log
            return (0, content, identifier)
        else:  # digit-log
            return (1,)
    
    return sorted(logs, key=get_key)
```

## Time Complexity

- O(m × n log n), where n is the number of logs and m is the maximum length of a single log.
  - The sorting operation takes O(n log n) comparisons.
  - Each comparison requires splitting strings and comparing contents, which takes O(m) time.

## Space Complexity

- O(m × n) for the sorting algorithm's intermediate space.

## Notes

1. The key insight is to create a custom sorting key that properly implements the ordering rules.
2. We assign letter-logs a tuple starting with 0 to ensure they come before digit-logs (which start with 1).
3. For letter-logs, we include the content and identifier in the sorting tuple to follow the lexicographical ordering requirements.
4. For digit-logs, we only need to return a tuple with a "1" to indicate they should be after letter-logs, and their relative order is maintained. 