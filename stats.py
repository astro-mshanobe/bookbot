def get_num_words(text_as_string):
    words = text_as_string.split()
    total_words = len(words)
    return total_words

def get_num_characters(text_as_string):
    char_dict = {}
    text_lower = text_as_string.lower()

    for char in text_lower:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def get_sorted_list(dict_of_chars):
    chars_list = []
    for char, count in dict_of_chars.items():
        chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=lambda x: x["count"])
    return chars_list
