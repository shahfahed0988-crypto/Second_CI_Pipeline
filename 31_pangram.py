"""Program 31: Check whether a sentence is a pangram."""
import string


def is_pangram(sentence):
    """Return True if the sentence contains every letter of the alphabet."""
    sentence = sentence.lower()

    for letter in string.ascii_lowercase:
        if letter not in sentence:
            return False

    return True


if __name__ == "__main__":
    text = input("Enter a sentence: ")

    if is_pangram(text):
        print("The sentence is a pangram.")
    else:
        print("The sentence is not a pangram.")