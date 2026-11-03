"""Program 37: Rotate a string by K positions."""


def rotate_string(text, k):
    """Return the string rotated to the right by K positions."""
    if not text:
        return text

    k = k % len(text)

    return text[-k:] + text[:-k] if k != 0 else text


if __name__ == "__main__":
    text = input("Enter a string: ")
    k = int(input("Enter number of positions: "))

    print("Rotated string:", rotate_string(text, k))