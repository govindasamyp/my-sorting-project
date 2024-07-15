__version__ = "1.1.0"

def sort_numbers(numbers, order="asc"):
    if order == "desc":
        return sorted(numbers, reverse=True)
    return sorted(numbers)

if __name__ == "__main__":
    print(f"Sorting Program Version: {__version__}")
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    order = input("Enter sorting order (asc/desc): ").strip().lower()
    print("Original list:", numbers)
    sorted_numbers = sort_numbers(numbers, order)
    print(f"Sorted list ({order}):", sorted_numbers)