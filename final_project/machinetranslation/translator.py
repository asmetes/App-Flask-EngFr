"""
Translator Module
"""
from translate import Translator


def english_to_french(english_text):
    """
    Translates English text to French.
    """
    translator = Translator(to_lang='fr')
    french_text = translator.translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English.
    """
    translator = Translator(to_lang='en')
    english_text = translator.translate(french_text)
    return english_text

