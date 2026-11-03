"""Program 32: Count the number of words in a sentence."""


def count_words(sentence):
    """Return the number of words in the sentence."""
    words = sentence.split()

    return len(words)


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Number of words:", count_words(text))