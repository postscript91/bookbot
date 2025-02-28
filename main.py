def count_words(filepath):
    with open(filepath) as f:
        contents = f.read()
        word_count = len(contents.split())
    return word_count

def main():
    word_count = count_words("books/frankenstein.txt")
    print(f"{word_count} words found in the document")

main()