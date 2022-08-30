""" 
Write a function, combine_intervals, that takes in a list of intervals as an argument. Each interval 
is a tuple containing a pair of numbers representing a start and end time. Your function should 
combine overlapping intervals and return a list containing the combined intervals.

Algorithm:

1. Sort the input intervals
2. take the first interval as the last_start, last_end 
3. Compare last_start, last_end with current_start, current_end 
4. last_end > current_start and current_end > last_end
"""

def combine_intervals(intervals):

    sorted_intervals = sorted(intervals) 
    combined = [sorted_intervals[0]]

    for sorted_interval in sorted_intervals[1:]:
        current_start, current_end = sorted_interval 
        last_start, last_end = combined[-1]

        if last_end >= current_start:
            if current_end > last_end:
                combined[-1] = (last_start, current_end)
            else:
                combined.append(sorted_interval)

    return combined


if __name__ == "__main__":
    intervals = [
    (1, 4),
    (12, 15),
    (3, 7),
    (8, 13),
    ]
    print(combine_intervals(intervals))
    # -> [ (1, 7), (8, 15) ]