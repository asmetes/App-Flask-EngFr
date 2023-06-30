<<<<<<< HEAD
=======
"""
Unit tests for translation functions
"""

>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb
import unittest
from translator import english_to_french, french_to_english


<<<<<<< HEAD
class TranslatorTests(unittest.TestCase):
    """
    Test cases for the Translator module.
    """

    def test_english_to_french_hello(self):
        """
        Test translation from English to French for the word 'Hello'.
=======
class TranslationTestCase(unittest.TestCase):
    """
    Test case for translation functions
    """

    def test_english_to_french(self):
        """
        Test translation from English to French
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb
        """
        english_text = "Hello"
        expected_translation = "Bonjour"
        translation = english_to_french(english_text)
        self.assertEqual(translation, expected_translation)

<<<<<<< HEAD
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
=======
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb
        french_text = "Bonjour"
        expected_translation = "Hello"
        translation = french_to_english(french_text)
        self.assertEqual(translation, expected_translation)

<<<<<<< HEAD
    def test_french_to_english_hello(self):
        """
        Test translation from French to English for the word 'Hello'.
        """
        french_text = "Hello"  # Since 'Hello' is not a French word
        expected_translation = "Hello"
        translation = french_to_english(french_text)
=======
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
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb
        self.assertEqual(translation, expected_translation)


if __name__ == '__main__':
<<<<<<< HEAD
    unittest.main()
=======
    unittest.main()
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb
