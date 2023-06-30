from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
<<<<<<< HEAD
    french_translation = english_to_french(textToTranslate)
    return french_translation
=======
    translation = translator.english_to_french(textToTranslate)
    return translation
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
<<<<<<< HEAD
    english_translation = french_to_english(textToTranslate)
    return english_translation
=======
    translation = translator.french_to_english(textToTranslate)
    return translation
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb

@app.route("/")
def renderIndexPage():
    # Write the code to render template
<<<<<<< HEAD
    return render_template('index.html')
=======
    return render_template("index.html")
>>>>>>> a49869bbfd5c91ee84d1a293250963c54fda1aeb

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
