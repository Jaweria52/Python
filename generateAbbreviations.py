def generate_abbreviations(word, length, current='', index=0):
    if len(current) == length:
        return [current]

    if index == len(word):
        return []

    # Include the current letter
    abbreviations_include = generate_abbreviations(word, length, current + word[index], index + 1)
    # Skip the current letter
    abbreviations_skip = generate_abbreviations(word, length, current, index + 1)
    return abbreviations_include + abbreviations_skip
