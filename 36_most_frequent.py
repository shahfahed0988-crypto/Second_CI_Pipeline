"""Program 36: Find the most frequent element in a list."""


def most_frequent(numbers):
    """Return the element that occurs most frequently."""
    if not numbers:
        return None

    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    return max(frequency, key=frequency.get)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    result = most_frequent(numbers)
    print("Most frequent element:", result)