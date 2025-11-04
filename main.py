from stats import (
        count_words,
        count_char,
        chars_dict_to_sorted_list
)

def main():
    book_path = "books/frankenstein.txt"
    
    word_count = count_words(get_book_text(book_path))
    char_count = count_char(get_book_text(book_path))
    char_sorted_list = chars_dict_to_sorted_list(char_count)

    print_report(book_path, word_count, char_sorted_list)

def get_book_text(file_path):
    with open(file_path) as f: # man with for a description of what the function does
        return f.read()

def print_report(book_path, word_count, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")





main()
