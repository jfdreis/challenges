"""Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.

Input: [0, 0, 1, 1, 1, 2, 2].

Output: 3.

Your function should modify the list in place so that the first three elements become 0, 1, 2. Return 3 because the new length is 3."""


def remove_duplicates_on_to_2(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    left = 0 # Points to the last unique element found
    right = 1 # Points to the element to be compared with arr[left]
    # Debug Print 
    print(f"Initial array: \n{arr}")
    while right < len(arr):
        #Debug Print
        print(f"left index: {left}, right index: {right}")
        if arr[left] != arr[right]:
            # Found a new unique value. Move both pointers one unit to the right
            right += 1
            left += 1
        else: # Found a duplicate. Remove it by popping from the array
            arr.pop(right)
            #Deprinting the array to see how it looks after popping
            print(f"Duplicate found. Removed value at index {right}.")
            print(f"New array: \n{arr}")
            # Note: We do not move the right pointer one unit to the right because it is alreay
            # point to what the next element is after popping
    return right

def remove_duplicates_on(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    left = 0 # Points to the last unique element found
    print(f"Initial array: \n{arr}")

    # right pointer scans the array
    for right in range(1,len(arr)):
        # Debug Print
        print(f"left index: {left}, right index: {right}")
        if arr[left] != arr[right]:
            #Found a new unique value, move left pointer and overwrite the value at arr[left]
            left += 1
            arr[left] = arr[right]
        # else: A duplicate is found, do nothing and continue (right moves automatically)
            
    # As left is an index, and we want to return the length
    print(f"Final array without duplicates: \n{arr[:left+1]}")
    return left + 1 

def main():
    arr = [0, 1, 1, 2, 2, 5, 5, 5, 6]
    print(f"The original length of the array is {len(arr)}")
    result = remove_duplicates_on_to_2(arr)
    print(f"The len of the array without duplicates is {result}")
    print("-------")
    arr = [0, 1, 1, 2, 2, 5, 5, 5, 6]
    result = remove_duplicates_on(arr)
    print(f"The len of the array without duplicates is {result}")

if __name__ == "__main__":
    main()