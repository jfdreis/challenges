// Find the boundary index where the first True value appears in a sorted array of booleans
// In this case we do not save any temporary variable when we find a true value

pub fn find_boundary_1(arr: &[bool]) -> i32 {
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;
    while left < right {
        let mid = (left + right) / 2;
        let value = arr[mid as usize];
        // If the mid value is False, we need to look for True values in the right half
        if !value {
            left = mid + 1;
        }
        // If the mid value is True, we need to look for True values in the left half (including mid)
        else {
            right = mid;
        }
        // If there is no True value in the array, return -1
    }
    // Test entry has value false
    if !arr[right as usize] {
        return -1;
    }
    right
}

// Find the boundary index where the first True value appears in a sorted array of booleans
// In this case we save a variable when we find a true value
pub fn find_boundary_2(arr: &[bool]) -> i32 {
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;
    let mut boundary_index = -1;
    while left <= right {
        let mid = (left + right) / 2;
        let value = arr[mid as usize];
        // println!("left {left}, right {right}, mid {mid}");
        // If the mid value is False, we need to look for True values in the right half
        if !value {
            left = mid + 1;
            // println!("left updated to {left}, right {right}, mid {mid}");
        }
        // If the mid value is True, we need to look for True values in the left half
        //  We can exclude mid in the next itearion because we store its index in boundary_index
        else {
            boundary_index = mid;
            right = mid - 1;
            // println!(
            //     "left {left}, right updated to {right}, mid {mid},boundary_index updated to {boundary_index}"
            // );
        }
    }
    boundary_index
}

#[cfg(test)]
mod tests {

    use super::*;
    #[test]
    fn test_find_boundary_1() {
        let cases: &[(&[bool], i32)] = &[
            (&[false, false, true, true, true], 2),
            (&[true], 0),
            (&[false, false, false], -1),
            (&[true, true, true, true, true], 0),
            (&[false, true], 1),
            (
                &[false, false, false, false, false, false, false, false, true],
                8,
            ),
        ];

        for (input, expected) in cases {
            let result = find_boundary_1(&input);
            assert_eq!(result, *expected);
        }
    }

    #[test]
    fn test_find_boundary_2() {
        let cases: &[(&[bool], i32)] = &[
            (&[false, false, true, true, true], 2),
            (&[true], 0),
            (&[false, false, false], -1),
            (&[true, true, true, true, true], 0),
            (&[false, true], 1),
            (
                &[false, false, false, false, false, false, false, false, true],
                8,
            ),
        ];

        for (input, expected) in cases {
            let result = find_boundary_2(&input);
            assert_eq!(result, *expected);
        }
    }

    // Test both function at once
    #[test]
    fn test_find_boundary_both() {
        // Array of function pointers, each taking &[bool] and returning i32
        let funcs: &[(&str, fn(&[bool]) -> i32)] = &[
            ("find_boundary_1", find_boundary_1),
            ("find_boundary_2", find_boundary_2),
        ];
        let cases: &[(&[bool], i32)] = &[
            (&[false, false, true, true, true], 2),
            (&[true], 0),
            (&[false, false, false], -1),
            (&[true, true, true, true, true], 0),
            (&[false, true], 1),
            (
                &[false, false, false, false, false, false, false, false, true],
                8,
            ),
        ];
        for (name, func) in funcs {
            for (input, expected) in cases {
                let result = func(&input);
                assert_eq!(
                    result, *expected,
                    "Function {} falide for input {:?}",
                    name, input
                );
            }
        }
    }
}
