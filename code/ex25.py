def break_words(stuff):
    """
    This function will break up word for us.
    """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """
    Sort the words.
    """
    return sorted(words)
def print_first_word(words):
    """
    Prints the first word after poppit off.
    """
    word = word.pop(-1) # 将列表中的最后一个元素从列表中删除，并将其赋值给了word，这将导致word变为一个单独的元素，而不再是列表或可迭代对象。
    print(words)

def print_last_word(words):
    """Prints the last word a after poping it off."""
    word = words.pop(-1) 
    print(word)

def sort_sentence(sentence):
    """Takes in a fall sentence and ret urns the sorted words"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
        
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words  = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)