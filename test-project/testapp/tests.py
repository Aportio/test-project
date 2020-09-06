from django.test import TestCase

from .tools import splitWords


class AppTestCase(TestCase):
    def test_ok(self):
        self.assertTrue(True)

    def test_split_words(self):
        test_case = [
            {'sentence': 'Hello world', 'count': 2},
            {'sentence': 'Hello, world', 'count': 2},
            {'sentence': 'Hello-world', 'count': 2}
        ]
        for case in test_case:
            words = splitWords(case['sentence'])
            self.assertEqual(len(words), case['count'], 'Expected {expected} words instead of {actual} for sentence: {sentence}'.format(
                expected=case['count'], actual=len(words), sentence=case['sentence']))
