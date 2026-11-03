"""Program 38: Find the missing number using XOR."""


def missing_number(numbers):
    """Return the missing number from a sequence of 0 to N."""
    n = len(numbers)
    result = n

    for index, number in enumerate(numbers):
        result ^= index
        result ^= number

    return result


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print("Missing number:", missing_number(numbers))