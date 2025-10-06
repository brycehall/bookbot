
def get_num_words(filepath):

    with open(filepath) as f:

        file_contents = f.read()
        word_count = len(file_contents.split())
        
        return word_count

def get_num_char(filepath):
    
    char_dict = {}
    
    with open(filepath) as f:

        contents = f.read().lower()
        for character in contents:
            if character in char_dict:
                char_dict[character] += 1
            else:
                char_dict[character] = 1

    return char_dict