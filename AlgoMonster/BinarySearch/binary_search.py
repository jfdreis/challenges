# Define a function to perform binary search on a sorted array
def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)-1
    while left <= right: 
        mid = (left + right) // 2
        if arr[mid] == target: 
            # If the target is found, return its index
            return mid
        elif arr[mid] < target:
            # If the target is greater than the value in the middle, ignore the left half
            left = mid + 1
        else:
            # If the target is smaller than the value in the middle, ignore the right half
            right = mid - 1
    return -1

def main():
    arr = [2, 8, 89, 120, 1000]
    target = 120
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Target {target} found at index {result}")
    else:
        print(f"Target {target} not found in the array")

if __name__ == "__main__":
    main()