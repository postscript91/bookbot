from stats import count_words
from stats import count_chars

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count = count_words("books/frankenstein.txt")
    char_count = count_chars("books/frankenstein.txt")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in char_count:
        char = entry["char"]
        count = entry["count"]
        if char.isalpha() == True:
            print(f"{char}: {count}")
    print("============= END ===============")
main()