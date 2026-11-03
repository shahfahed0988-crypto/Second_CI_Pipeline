"""Program 33: Find the first non-repeating character in a string."""


def first_non_repeating(text):
    """Return the first character that appears only once."""
    for character in text:
        if text.count(character) == 1:
            return character

    return None


if __name__ == "__main__":
    text = input("Enter a string: ")
    result = first_non_repeating(text)

    if result is not None:
        print("First non-repeating character:", result)
    else:
        print("No non-repeating character found.")