def count_words(text):
    word_count = text.split()
    return len(word_count)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(char_counts):
    char_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list