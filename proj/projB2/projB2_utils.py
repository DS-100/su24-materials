import numpy as np

def words_in_texts(words, texts):
    '''
    Args:
        words (list): words to find.
        texts (Series): strings to search in.
    
    Returns:
        A 2D NumPy array of 0s and 1s with shape (n, p) where n is the
        number of texts, and p is the number of words.
    '''
    indicator_array = 1 * np.array([texts.str.contains(word) for word in words]).T
    return indicator_array
