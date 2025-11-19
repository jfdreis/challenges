// Find the min value in a sorted array that was rotated
pub fn find_min(arr: &[i32]) -> i32 {
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;
    if left == right {
        // If there is only one element
        return left;
    }
    let mut min = -1;
    while left < right {
        let mid = (left + right) / 2;
        println!("left {left}, right {right}, mid {mid}, min {min}");
        let value = arr[mid as usize];
        // in this case the min must be at mid or to the left of mid because the values are increasing
        if value <= arr[right as usize] {
            min = mid;
            right = mid;
            println!("left {left}, right updated to {right}, mid {mid}, min updated to {min}");
        }
        // arr[mid] > arr[right]
        // The min must be to the right of mid because the values are increasing from left to mid
        // and we know that there is smaller value to the right of mid
        else {
            min = right;
            left = mid + 1;
            println!("left updated to {left}, right {right}, mid {mid}, min updated to {min}");
        }
    }
    min
}

// There is a cleaner way to define this function:
// Just find the first element that is less than or equal to the last element
pub fn find_min_cleaner(arr: &[i32]) -> i32 {
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;
    let mut min = -1;
    while left <= right {
        let mid = (left + right) / 2;
        let value = arr[mid as usize];
        // The min must be at mid or to the left of mid because the values are increasing
        if value <= arr[arr.len() - 1] {
            min = mid;
            right = mid;
        }
        // value > arr[-1]
        else {
            left = mid + 1
        }
    }
    min
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_min() {
        let arr = [40, 50, 10, 20, 30];
        let result = find_min(&arr);
        assert_eq!(result, 2); // index of 10
    }
    #[test]

    fn test_find_min_cleaner() {
        let arr = [40, 50, 10, 20, 30];
        let result = find_min(&arr);
        assert_eq!(result, 2); // index of 10
    }
}
