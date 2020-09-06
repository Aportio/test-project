# general purpose tools used elsewhere
import re
import string

# split a string into words based on Regex rules
# 1. split on blanks - punctuation are not words
# 2. split on hyphens
def splitWords(sentence):
    rePunctuation = r'[{p}]'.format(p=string.punctuation)
    reSplit = r'[\s+]'
    s = str(sentence).replace('-', ' ') # force to string and convert hyphens to spce to separate words
    s = re.sub(rePunctuation, '', s).strip() # remove all punctuation and strip trailing whitespace
    return re.split(reSplit, s, flags=re.IGNORECASE)
