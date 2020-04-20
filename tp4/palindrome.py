import unittest  # import de la librairie qui permet de faire des tests unitaires


def is_palindrome(mot):
    isPalindrome = True

    for index in range(0, len(mot)):
        if mot[index] != mot[-index - 1]:
            isPalindrome = False

    return isPalindrome


class PalindromeTest(unittest.TestCase):

    def test_word(self):
        self.assertEqual(True, is_palindrome("kayak"))

    def test_word2(self):
        self.assertEqual(True, is_palindrome("toto"))
