import sys
from stats import count_words, count_characters, sort_on

def get_book_text(filepath):
    """Reads contents of the file and returns it as a string"""
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File not found at path '{book_path}'")
        sys.exit(1)

    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_char_data = sort_on(char_counts)

    print(f"Found {num_words} total words\n")

    for entry in sorted_char_data:
        print(f"{entry['char']}: {entry['num']}")

if __name__ == "__main__":
    main()
