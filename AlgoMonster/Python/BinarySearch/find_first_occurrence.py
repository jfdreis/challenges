# Find the first occurance of a value in an monotically increasing array
def find_first_occurrence(arr: list[int], target : int) -> int:
    left = 0
    right = len(arr)-1
    first_occurence = -1 # Default value if target is not found
    while left <= right:
        mid = (left + right) // 2
        print(f"left {left}, right {right}, mid {mid}")
        if arr[mid] == target:
            # If we found the target, we store its index and continue searching in the left half
            first_occurence = mid
            right = mid-1
            print(f"left {left}, right updated to {right}, mid {mid}, first_occurence updated to {first_occurence}")
        elif arr[mid] < target:
            # If the target is greater than the mid value, we need to search in the right half
            left = mid + 1
            print(f"left updated to {left}, right {right}, mid {mid}, first_occurence updated to {first_occurence}")
        else:
            # If the target is less than the mid value, we need to search in the left half
            right = mid - 1
            print(f"left {left}, right updated to {right}, mid {mid}, first_occurence updated to {first_occurence}")    
    return first_occurence

def main():
    arr = [2, 3, 5, 7, 11]
    target = 2
    result = find_first_occurrence(arr,target)
    
    if result != -1:
        print(f"The first true statement is found at index {result}")
    else:
        print(f"There is no true statement in the array")

if __name__ == "__main__":
    main()