from stats import get_num_words, get_num_char

def main():

    words = get_num_words("books/frankenstein.txt")
    characters = get_num_char("books/frankenstein.txt")
    
    print(f"Found {words} total words")
    print(characters)

main()