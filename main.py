from stats import get_num_words

def main():

    words = get_num_words("books/frankenstein.txt")

    print(f"Found {words} total words")

main()