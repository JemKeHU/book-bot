from collections import defaultdict
import re

def count_characters_and_total_words(file_path):
    character_count = defaultdict(int)  # For counting individual characters
    total_word_count = 0                # For counting the total number of words

    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  # Read and convert text to lowercase

            # Character counting
            for char in text:
                if char.isalpha():  # Count only alphabetic characters
                    character_count[char] += 1

            # Word counting
            words = re.findall(r'\b\w+\b', text)  # Extract words using regex
            total_word_count = len(words)         # Total number of words

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except IOError:
        print(f"Error: Could not read the file at {file_path}.")

    return character_count, total_word_count

if __name__ == "__main__":
    book_path = '/home/jemkenu/workspace/github.com/USERNAME/book-bot/books/frankenstein.txt'  # Ensure this path is correct
    character_result, total_word_count = count_characters_and_total_words(book_path)

    # Sort and print character counts
    sorted_characters = sorted(character_result.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of /books/frankenstein.txt ---")
    print(f"{total_word_count} words found in the document\n")
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")

    # Print total word count



# Book reader
# with open(file_path, 'r') as file:
#     contents = file.read()

#     print(contents)

# Word counter
# word_count = 0


# with open(file_path, 'r') as file:
#     for line in file:
#         words = line.split()
#         word_count += len(words)

# print(f"Number of words in the book: {word_count}")