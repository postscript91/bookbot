def count_words(filepath):
    with open(filepath) as f:
        contents = f.read()
        word_count = len(contents.split())
    return word_count