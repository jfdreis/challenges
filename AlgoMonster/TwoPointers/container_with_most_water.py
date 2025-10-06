"""
container with most water

you are given an array of non-negative integers height, where each element represents a vertical line drawn on the x-axis at that index. two lines, together with the x-axis, form a container.

return the maximum amount of water a container can store.

example:

input: height = [1,8,6,2,5,4,8,3,7]
output: 49

"""


def area(h_l: int, h_r: int, l: int, r: int) -> int:
    return min(h_l,h_r) * (r-l)

def maximum_water_on_to_2(arr: list[int]) -> int:
        if len(arr) <=1 :
            return 0
        left = 0
        right = len(arr)-1
        temp_right = right
        max_area = 0
        while left < right:
            for i in range(left+1,right+1):
                new_area = area(arr[left],arr[i], left, i)
                print(f"For {left} and {i} New area is {new_area}")
                if new_area > max_area:
                    print(f"Max area was updated to {new_area}")
                    temp_right = i
                    max_area = new_area
            right = temp_right
            left += 1
        return max_area

def maximum_water_optimized(arr: list[int]) -> int:
        if len(arr) <=1 :
            return 0
        left = 0
        right = len(arr)-1
        max_area = area(arr[left],arr[right], left, right)
        while left < right:
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
            new_area = area(arr[left],arr[right], left, right)
            if new_area > max_area:
                max_area = new_area
        return max_area

def main():
    examples = [
        [1,8,6,2,5,4,8,3,7],
        [1,1]
    ]

    for arr in examples:
        print(f"The max area is  {maximum_water_optimized(arr)}")
        print("-" * 30)

if __name__ == "__main__":
    main()
             

