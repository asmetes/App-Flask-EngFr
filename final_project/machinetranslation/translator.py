"""
Translator Module
"""
<<<<<<< HEAD
from translate import Translator
=======

from deep_translator import MyMemoryTranslator
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb


def english_to_french(english_text):
    """
    Translates English text to French.
    """
<<<<<<< HEAD
    translator = Translator(to_lang='fr')
=======
    translator = MyMemoryTranslator(source='en', target='fr')
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb
    french_text = translator.translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English.
    """
<<<<<<< HEAD
    translator = Translator(to_lang='en')
    english_text = translator.translate(french_text)
    return english_text

=======
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb
