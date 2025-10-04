"""
You've begun your new job to organize newspapers. Each morning, you are to separate the newspapers into smaller piles and assign each pile to a co-worker. This way, your co-workers can read through the newspapers and examine their contents simultaneously.

Each newspaper is marked with a read time to finish all its contents. A worker can read one newspaper at a time, and, when they finish one, they can start reading the next. Your goal is to minimize the amount of time needed for your co-workers to finish all newspapers. Additionally, the newspapers came in a particular order, and you must not disarrange the original ordering when distributing the newspapers. In other words, you cannot pick and choose newspapers randomly from the whole pile to assign to a co-worker, but rather you must take a subsection of consecutive newspapers from the whole pile.

What is the minimum amount of time it would take to have your coworkers go through all the newspapers? That is, if you optimize the distribution of newspapers, what is the longest reading time among all piles?

Constraints
1 <= newspapers_read_times.length <= 10^5

1 <= newspapers_read_times[i] <= 10^5

1 <= num_coworkers <= 10^5

Examples
Example 1:
Input: newspapers_read_times = [7,2,5,10,8], num_coworkers = 2
Output: 18
Explanation:
Assign first 3 newspapers to one coworker then assign the rest to another. The time it takes for the first 3 newspapers is 7 + 2 + 5 = 14 and for the last 2 is 10 + 8 = 18.

Example 2:
Input: newspapers_read_times = [2,3,5,7], num_coworkers = 3
Output: 7
Explanation:
Assign [2, 3], [5], and [7] separately to workers. The minimum time is 7.
"""

def can_distribute(newspapers_read_times: list[int], num_coworkers: int, max_time: int) -> bool:
    reader_count = 1
    current_time = 0
    for time in newspapers_read_times:
        if current_time + time <= max_time:
            current_time += time
        else:
            reader_count += 1
            current_time = time
            if reader_count > num_coworkers:
                return False
    return True
    
class Solution:
    def time_to_read(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        result = right
        while left <= right:
            mid = (left + right) // 2
            if can_distribute(nums, k, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

def main():
    arr = [7,2,5,10,8]
    arr = [1,2,3,4,5]
    workers = 2
    result = Solution().time_to_read(arr, workers)
    print("Input:", arr)
    print("Number of coworkers:", workers)
    print(f"Time to read all newspapers with optimal distribution: {result}")

if __name__ == "__main__":
    main()