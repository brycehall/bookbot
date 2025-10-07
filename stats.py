
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

def sort_dict(dictionary):

    def sort_on(items):
        return items["num"]

    dict_list = []
    sorted_dict = {}
    i = 0

    for char in dictionary:
        num = dictionary[char]
        dict_list.append({"char": char , "num": num})

    dict_list.sort(reverse=True, key=sort_on)

    while i < len(dict_list):
        for item in dict_list[i]:
            letter = dict_list[i]['char']
            count = dict_list[i]['num']
            if letter.isalpha():
                sorted_dict[letter] = count
            i += 1

    return sorted_dict