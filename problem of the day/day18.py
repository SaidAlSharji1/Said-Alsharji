def max_meetings(start, end):
    # Create a list of tuples where each tuple contains (start_time, end_time, meeting_index)
    meetings = [(start[i], end[i], i) for i in range(len(start))]

    # Sort meetings by their end times
    meetings.sort(key=lambda x: x[1])

    max_meetings_count = 0  # Initialize the count of maximum meetings
    selected_meetings = []  # Initialize the list to store the selected meetings

    # Select meetings one by one
    end_time = -1  # Initialize the end time of the previous meeting
    print("(start, end , no of meeting)")    
    for meeting in meetings:
        if meeting[0] >= end_time:
            selected_meetings.append(meeting[2])
            end_time = meeting[1]
            max_meetings_count += 1
            print (meeting)

    return max_meetings_count

# Example usage:
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]

max_count = max_meetings(start_times, end_times)
print("\nMaximum number of meetings:", max_count)
