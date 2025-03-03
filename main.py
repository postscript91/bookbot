import sys
from stats import count_words, count_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    word_count = count_words(filepath)
    char_count = count_chars(filepath)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in char_count:
        char = entry["char"]
        count = entry["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()