# general purpose tools used elsewhere


# split a string into words based on Regex rules
# 1. split on whitespace - punctuation are not words
# 2. split on hyphens
def splitWords(sentence):
    return str(sentence).split(' ');
