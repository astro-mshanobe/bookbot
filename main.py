import sys
from stats import get_num_words, get_num_characters, get_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def main():
    text = get_book_text(path)
    num_words = get_num_words(text)
    unique_char = get_num_characters(text)
    sorted_dicts = get_sorted_list(unique_char)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_dicts:
        char = item["char"]
        count = item["count"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

main()
