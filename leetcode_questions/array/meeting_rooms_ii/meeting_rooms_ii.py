from typing import List
import heapq

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Find the minimum number of conference rooms required for meetings.
    
    Args:
        intervals: List of meeting time intervals [start, end]
        
    Returns:
        Minimum number of conference rooms required
    """
    # If there are no meetings, we don't need any rooms
    if not intervals:
        return 0
    
    # Sort meetings by start time
    intervals.sort(key=lambda x: x[0])
    
    # Initialize a min heap to track end times of rooms in use
    free_rooms = []
    
    # Add the end time of the first meeting
    heapq.heappush(free_rooms, intervals[0][1])
    
    # Process the rest of the meetings
    for i in range(1, len(intervals)):
        # If the earliest ending room is free for this meeting
        if free_rooms[0] <= intervals[i][0]:
            # Remove the earliest ending meeting (room becomes available)
            heapq.heappop(free_rooms)
        
        # Add the current meeting's end time to the heap
        # (either reusing a room or allocating a new one)
        heapq.heappush(free_rooms, intervals[i][1])
    
    # The size of the heap represents the number of rooms needed
    return len(free_rooms)

# Test cases
if __name__ == "__main__":
    # Example 1
    intervals1 = [[0, 30], [5, 10], [15, 20]]
    print(min_meeting_rooms(intervals1))  # Expected output: 2
    
    # Example 2
    intervals2 = [[7, 10], [2, 4]]
    print(min_meeting_rooms(intervals2))  # Expected output: 1
    
    # Additional test cases
    intervals3 = [[1, 5], [8, 9], [8, 15]]
    print(min_meeting_rooms(intervals3))  # Expected output: 2
    
    intervals4 = [[1, 5], [5, 10]]
    print(min_meeting_rooms(intervals4))  # Expected output: 1
    
    intervals5 = [[1, 10], [2, 11], [3, 12], [4, 13]]
    print(min_meeting_rooms(intervals5))  # Expected output: 4 