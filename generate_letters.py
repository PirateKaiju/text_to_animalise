from gtts import gTTS

import os

import string

alphabet = string.ascii_lowercase

lang = 'en'

for letter in alphabet:
    gtts_obj = gTTS(text=letter, lang=lang, slow=False)
    gtts_obj.save('./res/'+letter+'.mp3')

    os.popen("sox " + './res/' + letter + ".mp3 " + './res/' + letter + ".mp3 silence 1 0.1 0.1%"+" reverse silence 1 0.1 0.1%"+" reverse")