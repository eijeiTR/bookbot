# takes the contents of a file (path) as input.
# separates each word delimited by spaces.
# iterates through the info stored in the words variable.
# returns the total count of words.
def count_words(file_contents):
    text = file_contents
    words = text.split()
    count = 0

    for word in words:
        count += 1
    return count

# takes the contents of a file (path) as input.
# sets all the text to lowercase to keep uniqueness.
# iterates through the info stored in the text variable.
# increments the count if char matches the dict key.
# initializes a unique dictionary key->value pair ({char:count}) if not present.
def count_char(file_contents):
    text = file_contents.lower()
    char_count_dict = {}

    for char in text:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict
