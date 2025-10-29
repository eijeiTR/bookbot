from stats import count_words
from stats import count_char

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    word_count = count_words(get_book_text("books/frankenstein.txt"))
    char_count = count_char(get_book_text("books/frankenstein.txt"))
    print(f"Found {word_count} total words")
    print(char_count)

main()
