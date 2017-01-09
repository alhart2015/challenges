from data import DICTIONARY, LETTER_SCORES

def only_letters(word):
    if word.isalpha():
        return word
    return ''.join([char for char in word if char.isalpha()])

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        all_words = [only_letters(row) for row in f]
    return all_words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    letter_scores = [LETTER_SCORES[char.upper()] for char in word]
    return sum(letter_scores)

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = words[0]
    max_score = calc_word_value(max_word)

    for word in words:
        if calc_word_value(word) > max_score:
            max_score = calc_word_value(word)
            max_word = word

    return max_word

if __name__ == "__main__":
    # run unittests to validate
    all_words = load_words()
    for i in range(10):
        print all_words[i], calc_word_value(all_words[i])
    print max_word_value()
