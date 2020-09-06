# general purpose tools used elsewhere
import re
import string

from .constants import MAX_SIMILAR_WORDS_RATIO, MAX_SENTENCE_MATCH_RATIO

# split a string into words based on Regex rules
# 1. split on blanks - punctuation are not words
# 2. split on hyphens
def splitWords(sentence):
    rePunctuation = r'[{p}]'.format(p=string.punctuation)
    reSplit = r'[\s+]'
    s = str(sentence).replace('-', ' ') # force to string and convert hyphens to spce to separate words
    s = re.sub(rePunctuation, '', s).strip() # remove all punctuation and strip trailing whitespace
    return re.split(reSplit, s, flags=re.IGNORECASE)


# test whether the words in the input sentence are too similar to the sentences in the list
def isSimilar(sentence, old_messages=[]):
    count_similar_messages = 0

    new_words = splitWords(sentence.lower())
    new_words_set = set(new_words)
    new_word_count = len(new_words)
    if new_word_count < 1:
        # fail any empty sentences
        return True

    count_old_messages = len(old_messages)
    if count_old_messages < 1:
        # we can't be too similar if no other messages
        return False

    for msg in old_messages:
        msg_words = splitWords(msg.lower())
        common_words = list(new_words_set.intersection(set(msg_words)))

        # check if too much of new message is in the common words list
        match_percent = len(common_words) / new_word_count
        if match_percent > MAX_SIMILAR_WORDS_RATIO:
            count_similar_messages = count_similar_messages +1

    # check if the message is too similar to too many old messages
    match_old_messages = count_similar_messages / count_old_messages
    if match_old_messages > MAX_SENTENCE_MATCH_RATIO:
        return True

    return False
