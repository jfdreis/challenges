/*
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
*/

pub fn can_distribute(newspapers_read_times: &[i32], num_coworkers: i32, max_time: i32) -> bool {
    let mut reader_count = 1;
    let mut current_time = 0;
    for time in newspapers_read_times {
        if current_time + time <= max_time {
            current_time += time;
        } else {
            reader_count += 1;
            current_time = *time;
            if reader_count > num_coworkers {
                return false;
            }
        }
    }
    true
}

pub fn time_to_read(nums: &[i32], k: i32) -> i32 {
    let mut left = *nums.iter().max().unwrap();
    let mut right = nums.iter().copied().sum();
    let mut result = right;
    while left <= right {
        let mid = (left + right) / 2;
        if can_distribute(nums, k, mid) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    result
}

#[cfg(test)]
mod tests {

    use super::*;
    #[test]
    fn test_time_to_read() {
        let cases = [
            // (array of newspaper time, num workers, expected result)
            ([7, 2, 5, 10, 8], 2, 18),
            ([1, 2, 3, 4, 5], 2, 9),
        ];

        for (news_time, num_workers, expected) in cases {
            let result = time_to_read(&news_time, num_workers);
            assert_eq!(result, expected);
        }
    }
}
