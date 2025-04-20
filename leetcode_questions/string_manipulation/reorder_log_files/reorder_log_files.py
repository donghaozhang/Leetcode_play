def reorder_log_files(logs):
    """
    You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
    
    Args:
        logs: List[str] - A list of log strings
        
    Returns:
        List[str] - The reordered logs
    """
    # Helper function to return the key for sorting
    def get_key(log):
        identifier, content = log.split(' ', 1)
        # Check if it's a letter-log or digit-log
        if content[0].isalpha():  # letter-log
            # Sort letter-logs by content first, then by identifier
            return (0, content, identifier)
        else:  # digit-log
            # Keep digit-logs in their original order
            return (1,)  # 1 means higher priority than letter-logs
    
    # Sort the logs using the custom key function
    return sorted(logs, key=get_key)

# Test cases
if __name__ == "__main__":
    # Example 1
    logs1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(reorder_log_files(logs1))
    # Output: ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
    
    # Example 2
    logs2 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    print(reorder_log_files(logs2))
    # Output: ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"] 