# Find the boundary index where the first True value appears in a sorted array of booleans
# In this case we do not save any temporary variable when we find a true value
def find_boundary_1(arr: list[bool]) -> int:
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == False:
            # If the mid value is False, we need to look for True values in the right half
            left = mid + 1
        else:
            # If the mid value is True, we need to look for True values in the left half (including mid)
            right = mid

    if arr[right] == False:
        # If there is no True value in the array, return -1
        return -1
    return right

# Find the boundary index where the first True value appears in a sorted array of booleans
# In this case we save a variable when we find a true value
def find_boundary_2(arr: list[bool]) -> int:
    left = 0
    right = len(arr)-1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        print(f"left {left}, right {right}, mid {mid}")
        if arr[mid] == False:
            # If the mid value is False, we need to look for True values in the right half
            left = mid + 1
            print(f"left updated to {left}, right {right}, mid {mid}")
        else:
            # If the mid value is True, we need to look for True values in the left half
            # We can exclude mid in the next itearion becasue we stored its index in boundary_index
            boundary_index = mid
            right = mid-1
            print(f"left {left}, right updated to {right}, mid {mid},boundary_index updated to {boundary_index}")
    return boundary_index

def main():
    # arr = [False, False, True, True, True]
    # arr = [True]
    # arr = [False, False, False]
    # arr = [True, True, True, True, True]
    # arr = [False, True]
    arr = [False, False, False, False, False, False, False, False, True]
    result = find_boundary_2(arr)
    
    if result != -1:
        print(f"The first true statement is found at index {result}")
    else:
        print(f"There is no true statement in the array")

if __name__ == "__main__":
    main()