"""
Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the non-zero elements. Do this in-place using constant auxiliary space.

Input:

[1, 0, 2, 0, 0, 7]
Output:

[1, 2, 7, 0, 0, 0]
"""

def move_zeros(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    left = 0 
    right = 0
    # Debug Print 
    print(f"Initial array: \n{arr}")
    while right < len(arr):
        if arr[left] != 0:
            left += 1
            right += 1
        else:
            if arr[right] == 0:
                right += 1
            else:
                # Swap the elements at left and right
                arr[left] = arr[right]
                arr[right] = 0
                left += 1
                right += 1
    return arr

def move_zeros_optimized(arr: list[int]) -> list[int]:
    write_position = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write_position], arr[i] = arr[i], arr[write_position]
            write_position += 1
    return arr


def main():
    examples = [
        [2],
        [0, 1, 0, 3, 4],
        [0, 1, 2, 0, 0, 0,  3, 4, 5, 0],   
        [1, 2, 3, 4, 5],      # no zeros
        [0, 0, 0, 0],         # all zeros
        [],                   # empty list
        [1],                  # single element
    ]

    for arr in examples:
        print(f"The array after moving zeros to the end is {move_zeros(arr)}")
        print("-" * 30)

    print("Using the optimized version")
    for arr in examples:
        print(f"The array after moving zeros to the end is {move_zeros_optimized(arr)}")
        print("-" * 30)


if __name__ == "__main__":
    main()