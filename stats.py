def count_words(file_contents):
    text = file_contents
    words = text.split()
    count = 0

    for word in words:
        count += 1
    return count

def count_char(file_contents):
    text = file_contents.lower()
    unique_char = set()
    char_count_dict = {}

    for char in text:
        unique_char.add(char)
    for char in unique_char:
        if char in unique_char:
            count = char_count_dict[char]
            #print(f"CHAR: {char}, COUNT: {count}")
        return char_count_dict
    
