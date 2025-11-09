def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    count = {}
    for char in text.lower():
        count[char] = count.get(char, 0) + 1
    return count

def sort_on(characters):
    return characters["num"]

def sort_character_counts(counts_dict):
    characters = []
    for char, num in counts_dict.items():
        characters.append({"char": char, "num": num})
    characters.sort(key=sort_on, reverse=True)
    return characters