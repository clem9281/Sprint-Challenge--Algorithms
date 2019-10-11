'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    counter = 0
    if len(word) <= 1:
        return counter
    elif word[0] + word[1] == 'th':
        counter = count_th(word[1:]) + 1
    else:
        counter = count_th(word[1:])
    return counter