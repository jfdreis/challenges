// Define a function to perform binary search on a sorted array
pub fn binary_search(arr: &[i32], target: i32) -> i32 {
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;
    while left <= right {
        let mid = (left + right) / 2;
        // If the target is found, return its index
        let value = arr[mid as usize];
        if value == target {
            return mid;
        }
        // If the target is greater than the value in the middle, ignore the left half
        else if value < target {
            left = mid + 1;
        }
        // If the target is smaller than the value in the middle, ignore the right half
        else {
            right = mid - 1;
        }
    }
    -1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_binary_search_found() {
        let arr = [2, 8, 89, 120, 1000];
        let result = binary_search(&arr, 120);
        assert_eq!(result, 3); // index of 120
    }

    #[test]
    fn test_binary_search_not_found() {
        let arr = [2, 8, 89, 120, 1000];
        let result = binary_search(&arr, 500);
        assert_eq!(result, -1); // index not found
    }
}
