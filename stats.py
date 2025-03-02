def count_words(filepath):
    with open(filepath) as f:
        contents = f.read()
        word_count = len(contents.split())
    return word_count

def get_count(item):
    return item["count"]

def count_chars(filepath):
    with open(filepath) as f:
        contents = f.read()
        contents_lower = contents.lower()
        char_count = {}
        for char in contents_lower:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        sorted_list = []
        for char, count in char_count.items():
            sorted_list.append({"char": char, "count": count})
        sorted_list.sort(key=get_count, reverse=True)
    return sorted_list


