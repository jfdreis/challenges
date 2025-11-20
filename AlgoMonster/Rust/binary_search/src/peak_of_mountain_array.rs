/*
Assuming the array is a mountain array
A mountain array is defined as an array where elements first strictly increase to a peak and then strictly decrease.
The task is to find the index of the peak element.
We assume that the array is at least 3 elements long and has a valid mountain shape.
*/

pub fn find_peak(arr: &[i32]) -> i32 {
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;
    let mut peak = 0;
    while left < right {
        let mid = (left + right) / 2;
        println!("left {left}, right {right}, mid {mid}, peak {peak}");
        // The peak is to the right of mid
        if arr[mid as usize] < arr[mid as usize + 1] {
            peak = mid + 1;
            left = mid + 1;
            println!("left updated to {left}, right {right}, mid {mid}, peak updated to {peak}");
        }
        // The peak is to the left of mid or it is mid
        else if arr[mid as usize] > arr[mid as usize + 1] {
            peak = mid;
            right = mid; // Cannot do right = mid - 1 because we might miss the peak
            println!("left {left}, right updated to {right}, mid {mid}, peak updated to {peak}")
        }
    }
    peak
}
// def main():
//     arr = [0, 1, 2, 3, 2, 1, 0]
//     result = find_peak(arr)
//     print(f"The minimum value is found at index {result}")

// if __name__ == "__main__":
//     main()

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_find_peak() {
        let arr = [0, 1, 2, 3, 2, 1, 0];
        let result = find_peak(&arr);
        assert_eq!(result, 3); // index of peak value
    }
}
