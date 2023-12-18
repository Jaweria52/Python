data = {'A': 25, 'B': 8, 'C': 8, 'D': 9, 'E': 35, 'F': 7, 'G': 9, 'H': 7, 'I': 25,
        'J': 3, 'K': 6, 'L': 15, 'M': 8, 'N': 15, 'O': 20, 'P': 8, 'Q': 1, 'R': 15,
        'S': 15, 'T': 15, 'U': 20, 'V': 7, 'W': 7, 'X': 3, 'Y': 7, 'Z': 1}

def calculate_letter_score(letter, is_first, is_last,word):
    if is_first:
        return 0
    elif is_last :
        if(letter==word[len(word)-1]):
            if(letter == 'E'):
                return 20
            else:
                return 5
        else:
            return data.get(letter)+word.index(letter)
    else:
        return data.get(letter, 0) +word.index(letter)

def calculate_abbreviation_score(abbreviation, word):
    score = 0
    for i, letter in enumerate(abbreviation):
        is_first = i == 0
        is_last = i == len(abbreviation) - 1
        score += calculate_letter_score(letter, is_first, is_last, word)
        # print(score)
    return score