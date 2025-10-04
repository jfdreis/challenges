# Assuming the array is a mountain array
# A mountain array is defined as an array where elements first strictly increase to a peak and then strictly decrease.
# The task is to find the index of the peak element.
# We assume that the array is at least 3 elements long and has a valid mountain shape.
def find_peak(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    peak = 0
    while left < right:
        mid = (left + right) // 2
        print(f"left {left}, right {right}, mid {mid}, peak {peak}")
        if arr[mid] < arr[mid + 1]:
            # The peak is to the right of mid
            peak = mid + 1
            left = mid + 1
            print(f"left updated to {left}, right {right}, mid {mid}, peak updated to {peak}")
        elif arr[mid] > arr[mid + 1]:
            # The peak is to the left of mid or it is mid
            peak = mid
            right = mid # Cannot do right = mid - 1 because we might miss the peak
            print(f"left {left}, right updated to {right}, mid {mid}, peak updated to {peak}")
    return peak

def main():
    arr = [0, 1, 2, 3, 2, 1, 0]
    result = find_peak(arr)
    print(f"The minimum value is found at index {result}")

if __name__ == "__main__":
    main()