from django.test import TestCase

from .tools import splitWords, isSimilar


class AppTestCase(TestCase):
    def test_ok(self):
        self.assertTrue(True)

    def test_split_words(self):
        test_case = [
            {'sentence': 'Hello world', 'count': 2},
            {'sentence': 'Hello, world', 'count': 2},
            {'sentence': 'Hello-world', 'count': 2},
            {'sentence': 'Hello, world\'s', 'count': 2},
            {'sentence': 'Hello, world\'s ?', 'count': 2},
        ]
        for case in test_case:
            words = splitWords(case['sentence'])
            self.assertEqual(len(words), case['count'], 'Expected {expected} words instead of {actual} for sentence: "{sentence}" list is {list}'.format(
                expected=case['count'], actual=len(words), sentence=case['sentence'], list=words))

    def test_similar_words(self):
        old_messages = [ 'This is a nice garden to walk in', 'How nice! You planted a garden...', 'My car is red.', 'The sky is usually blue.']
        new_message = 'It\'s nice to wander in this garden.'

        self.assertTrue(isSimilar(new_message, old_messages[:3]))
        self.assertFalse(isSimilar(new_message, old_messages))
