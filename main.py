from stats import get_num_words, get_num_char, sort_dict

def main():

    words = get_num_words("books/frankenstein.txt")
    characters = get_num_char("books/frankenstein.txt")
    sorted_dict = sort_dict(characters)

    print(f"Found {words} total words")
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

main()