"""
Unit tests for translation functions
"""

import unittest
from translator import english_to_french, french_to_english


class TranslationTestCase(unittest.TestCase):
    """
    Test case for translation functions
    """

    def test_english_to_french(self):
        """
        Test translation from English to French
        """
        english_text = "Hello"
        expected_translation = "Bonjour"
        translation = english_to_french(english_text)
        self.assertEqual(translation, expected_translation)

        french_text = "Bonjour"
        expected_translation = "Hello"
        translation = french_to_english(french_text)
        self.assertEqual(translation, expected_translation)

    def test_french_to_english(self):
        """
        Test translation from French to English
        """
        english_text = "Hello"
        expected_translation = "Bonjour"
        translation = french_to_english(english_text)
        self.assertEqual(translation, expected_translation)

        french_text = "Bonjour"
        expected_translation = "Hello"
        translation = english_to_french(french_text)
        self.assertEqual(translation, expected_translation)


if __name__ == '__main__':
    unittest.main()
