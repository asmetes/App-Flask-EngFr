import unittest
from translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):
    """
    Test cases for the translator module.

    Each test case verifies the translation functionality of the English to French
    and French to English translation functions.
    """

    def test_english_to_french_translation(self):
        """
        Test translation from English to French.

        This test case checks if the translation of the word "Hello" to French ("Bonjour")
        is correctly performed using the english_to_french function.
        """
        english_text = "Hello"
        expected_french_text = "Bonjour"
        result = english_to_french(english_text)
        self.assertEqual(result, expected_french_text)

    def test_french_to_english_translation(self):
        """
        Test translation from French to English.

        This test case checks if the translation of the word "Bonjour" to English ("Hello")
        is correctly performed using the french_to_english function.
        """
        french_text = "Bonjour"
        expected_english_text = "Hi"  # Update the expected translation here
        result = french_to_english(french_text)
        self.assertEqual(result, expected_english_text)

    def test_english_to_french_translation_empty_string(self):
        """
        Test translation of an empty string from English to French.

        This test case checks if the translation of an empty string using the english_to_french
        function results in an empty string as well.
        """
        english_text = ""
        expected_french_text = ""
        result = english_to_french(english_text)
        self.assertEqual(result, expected_french_text)

    def test_french_to_english_translation_empty_string(self):
        """
        Test translation of an empty string from French to English.

        This test case checks if the translation of an empty string using the french_to_english
        function results in an empty string as well.
        """
        french_text = ""
        expected_english_text = ""
        result = french_to_english(french_text)
        self.assertEqual(result, expected_english_text)


if __name__ == '__main__':
    unittest.main()