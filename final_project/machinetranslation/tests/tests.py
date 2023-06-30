import unittest
from translator import english_to_french, french_to_english


class TranslatorTests(unittest.TestCase):
    """
    Test cases for the Translator module.
    """

    def test_english_to_french_hello(self):
        """
        Test translation from English to French for the word 'Hello'.
        """
        english_text = "Hello"
        expected_translation = "Bonjour"
        translation = english_to_french(english_text)
        self.assertEqual(translation, expected_translation)

    def test_english_to_french_bonjour(self):
        """
        Test translation from English to French for the word 'Bonjour'.
        """
        english_text = "Bonjour"
        expected_translation = "Bonjour"  # Since 'Bonjour' is already a French word
        translation = english_to_french(english_text)
        self.assertEqual(translation, expected_translation)

    def test_french_to_english_bonjour(self):
        """
        Test translation from French to English for the word 'Bonjour'.
        """
        french_text = "Bonjour"
        expected_translation = "Hello"
        translation = french_to_english(french_text)
        self.assertEqual(translation, expected_translation)

    def test_french_to_english_hello(self):
        """
        Test translation from French to English for the word 'Hello'.
        """
        french_text = "Hello"  # Since 'Hello' is not a French word
        expected_translation = "Hello"
        translation = french_to_english(french_text)
        self.assertEqual(translation, expected_translation)


if __name__ == '__main__':
    unittest.main()