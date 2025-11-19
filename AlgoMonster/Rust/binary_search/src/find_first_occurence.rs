// Find the first occurance of a value in an monotically increasing array
pub fn find_first_occurrence(arr: &[i32], target: i32) -> i32 {
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;
    // Default value if target is not found
    let mut first_occurence = -1;
    while left <= right {
        let mid = (left + right) / 2;
        println!("left {left}, right {right}, mid {mid}");
        let value = arr[mid as usize];
        // If we found the target, we store its index and
        // continue searching to the left
        if value == target {
            first_occurence = mid;
            right = mid - 1;
            println!(
                "left {left}, \
                   right updated to {right}, \
                   mid {mid}, \
                   first_occurence updated to {first_occurence}"
            );
        } else if value < target {
            // If the target is greater than the mid value,
            // we need to search to the right
            left = mid + 1;
            println!(
                "left updated to {left}, \
                    right {right}, \
                    mid {mid}, \
                    first_occurence updated to {first_occurence}"
            );
        } else {
            // If the target is less than the mid value,
            // we need to search in the left half
            right = mid - 1;
            println!(
                "left {left}, \
                    right updated to {right}, \
                    mid {mid}, \
                    first_occurence updated to {first_occurence}"
            )
        }
    }
    first_occurence
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_first_occurrence_found() {
        let arr = [2, 2, 5, 7, 11];
        let target = 2;
        let result = find_first_occurrence(&arr, target);
        assert_eq!(result, 0) //index of the first 2
    }

    #[test]
    fn test_find_first_occurrence_not_found() {
        let arr = [2, 2, 5, 7, 11];
        let target = 2;
        let result = find_first_occurrence(&arr, target);
        assert_eq!(result, 0) //index of the first 2
    }
}
