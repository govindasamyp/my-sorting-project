def sort_numbers(numbers):
    return sorted(numbers)

if __name__ == "__main__":
    numbers = [34, 1, 23, 4, 3, 8, 12]
    print("Original list:", numbers)
    sorted_numbers = sort_numbers(numbers)
    print("Sorted list:", sorted_numbers)