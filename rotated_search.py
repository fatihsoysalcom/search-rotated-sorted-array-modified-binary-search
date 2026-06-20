def rotated_binary_search(arr, target):
    """Searches for a target value in a rotated sorted array using a modified binary search.

    Args:
        arr: A list of integers representing the rotated sorted array.
        target: The integer value to search for.

    Returns:
        The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # If target is found at mid
        if arr[mid] == target:
            return mid

        # Determine which half is sorted
        # Left half is sorted
        if arr[left] <= arr[mid]:
            # Target is in the sorted left half
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            # Target is in the unsorted right half
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Target is in the sorted right half
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            # Target is in the unsorted left half
            else:
                right = mid - 1

    # Target not found
    return -1

# Example Usage:
rotated_array = [4, 5, 6, 7, 0, 1, 2]
target_value = 0

index = rotated_binary_search(rotated_array, target_value)

if index != -1:
    print(f"Target {target_value} found at index: {index}")
else:
    print(f"Target {target_value} not found in the array.")

target_value = 3
index = rotated_binary_search(rotated_array, target_value)

if index != -1:
    print(f"Target {target_value} found at index: {index}")
else:
    print(f"Target {target_value} not found in the array.")
