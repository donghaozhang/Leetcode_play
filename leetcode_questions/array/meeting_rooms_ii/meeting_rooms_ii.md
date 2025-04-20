# Meeting Rooms II

## Problem

Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of conference rooms required.

## Examples

**Example 1:**
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

Explanation:
- Meeting 1: [0,30]
- Meeting 2: [5,10]
- Meeting 3: [15,20]
We need at least 2 rooms because meetings 1 and 2 overlap, and meetings 1 and 3 overlap.

**Example 2:**
```
Input: intervals = [[7,10],[2,4]]
Output: 1
```

Explanation:
- Meeting 1: [7,10]
- Meeting 2: [2,4]
These meetings don't overlap, so we can use the same room.

## Approach: Min Heap

The key insight is to track which meetings are currently happening and make efficient decisions about when a room can be reused.

1. Sort all meetings by start time.
2. Use a min-heap to track the end times of ongoing meetings.
3. For each meeting:
   - Check if the earliest finishing meeting has already ended by the start time of the current meeting.
   - If yes, we can reuse that room (pop from heap).
   - Add the current meeting's end time to the heap.
4. The final size of the heap is the number of rooms needed.

This approach works because:
- The heap always contains the rooms that are currently in use.
- The earliest ending meeting is at the top of the heap.
- If we can't reuse a room, we add a new one to the heap.

## Solution

```python
def min_meeting_rooms(intervals: List[List[int]]) -> int:
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
```

## Time Complexity

- Sorting takes O(n log n) time, where n is the number of meetings.
- We process each meeting once and perform heap operations (push/pop) which take O(log n) time each.
- Overall: O(n log n)

## Space Complexity

- O(n) for storing the heap in the worst case (when all meetings overlap).

## Alternative Approaches

### Chronological Ordering

Another approach is to separate all start and end times and process them in chronological order:

1. Create two separate arrays, one for start times and one for end times.
2. Sort both arrays.
3. Use two pointers to process these sorted arrays.
4. When we encounter a start time, we need a new room.
5. When we encounter an end time, a room becomes available.

```python
def min_meeting_rooms_chronological(intervals):
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])
    
    start_ptr = 0
    end_ptr = 0
    rooms_needed = 0
    
    while start_ptr < len(intervals):
        if start_times[start_ptr] >= end_times[end_ptr]:
            # A meeting has ended, so we free up a room
            rooms_needed -= 1
            end_ptr += 1
        
        # We need a new room for this meeting
        rooms_needed += 1
        start_ptr += 1
    
    return rooms_needed
```

This approach also has O(n log n) time complexity due to sorting.

## Real-world Applications

- Conference room scheduling systems
- Resource allocation in operating systems
- Time slot allocation in appointment systems
- Job/task scheduling with limited resources 