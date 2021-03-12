#Binary Search Function

def binarySearch(sorted_list, number):
    low = 0
    high = len(sorted_list) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If number is greater, ignore left half
        if sorted_list[mid] < number:
            low = mid + 1

        # If number is smaller, ignore right half
        elif sorted_list[mid] > number:
            high = mid - 1

        # means number is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


sorted_list = list(map(int, input().split()))
sorted_list = sorted(sorted_list)
number = int(input())

result = binarySearch(sorted_list, number)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("NIL")