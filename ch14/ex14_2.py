''' pickle is GREAT for this saving specified data structure task.
'''
import pickle
from collections import defaultdict

def load_words(filename="words.txt"):
    try:
        with open(filename) as f:
            for word in f:
                yield word.rstrip()  # return a generator
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

def all_anagram(l):
    '''Reads a list and return a set of anagram words
    
    l: list
    
    Returns: set
    '''
    d = defaultdict(list)  # avoid KeyError in dict()
    for word in l:
        signature = "".join(sorted(word))  # sorted: leave the original word untouched
        d[signature].append(word)

    for k, v in d.items():  # remove d[k] if there is only one value corresponding to the key which means there is no anagram for the word 
        if len(v) == 1:
            del d[k]

    return d

def save_dict(d):
    try:
        with open('shelf.pkl', 'wb') as f:  # wb for write byte
            pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)
    except IOError:
        print("Error: Could not save dictionary to 'shelf.pkl'.")

def look_up_dict(word):
    try:
        # look up a word and return its anagram in the 'shelf'
        with open('shelf.pkl', 'rb') as f:  # rb for read byte
            d = pickle.load(f)
        for k, v in d.items():
            for i in v:
                if i == word:
                    return v
    except IOError:
        print("Error: Could not load dictionary from 'shelf.pkl'.")

if __name__ == '__main__':
    books = all_anagram(load_words())
    if books:  # Only save if the dictionary is successfully loaded
        save_dict(books)
        print('')
        print(look_up_dict('tired'))
        print(look_up_dict('cosets'))
