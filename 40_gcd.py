"""Program 40: Find the greatest common divisor of two numbers."""


def gcd(a, b):
    """Return the greatest common divisor of two numbers."""
    a = abs(a)
    b = abs(b)

    while b:
        a, b = b, a % b

    return a


if __name__ == "__main__":
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))

    print("Greatest Common Divisor:", gcd(first, second))