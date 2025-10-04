# Find the min value in a sorted array that was rotated
def find_min(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    if left == right:
        # If there is only one element
        return left
    min = -1
    while left < right:
        mid = (left + right) // 2
        print(f"left {left}, right {right}, mid {mid}, min {min}")
        if arr[mid] <= arr[right]:
            # The min must be at mid or to the left of mid because the values are increasing
            min = mid
            right = mid
            print(f"left {left}, right updated to {right}, mid {mid}, min updated to {min}")
        else: # arr[mid] > arr[right]
            # The min must be to the right of mid because the values are increasing from left to mid 
            # and we know that there is smaller value to the right of mid
            min = right
            left = mid+1
            print(f"left updated to {left}, right {right}, mid {mid}, min updated to {min}")
    return min

## There is a cleaner way to define this function:
## Just find the first element that is less than or equal to the last element
def find_min_cleaner(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    min = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
            # The min must be at mid or to the left of mid because the values are increasing
            min = mid
            right = mid
        else: # arr[mid] > arr[-1]
            left = mid+1
    return min

def main():
    arr = [40, 50, 10, 20, 30]
    result = find_min(arr)
    print(f"The minimum value is found at index {result}")

if __name__ == "__main__":
    main()