from googletrans import Translator
import wordfreq
import random
import threading

lang_dict = {'Bulgarian': 'bg', 'Catalan': 'ca',
             'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Finnish': 'fi', 'French': 'fr', 
             'German': 'de', 'Greek': 'el', 'Hungarian': 'hu', 'Indonesian': 'id', 
             'Italian': 'it', 'Latvian': 'lv', 'Macedonian': 'mk', 'Malay': 'ms', 
             'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru', 
             'Serbian': 'sr', 'Spanish': 'es', 'Swedish': 'sv', 'Turkish': 'tr', 'Ukrainian': 'uk'}
translator = Translator()
# with open("list.txt") as f:
#     r = f.read().split("\n")
#     r = [list(filter(lambda x: x!="", l.split(" "))) for l in r]
#     r = [l[0:2] for l in r]
#     for l in r:``
#         lang_dict[l[0]] = l[1]
#     print(lang_dict)

def get_word_pair(language):
    lang = lang_dict[language]
    lang_word = wordfreq.random_words(lang, nwords=1)
    eng_word = translator.translate(lang_word, src=lang, dest='en').text
    if len(lang_word) > 10 or len(eng_word) > 10 or (len(lang_word) == 1 and len(eng_word) == 1) \
        and lang_word not in ["00:00", "0:00", "000.000"]:
        lang_word, eng_word = get_word_pair(language)

    return lang_word, eng_word

class WordGenerator:
    def __init__(self, language):
        self.language = language
        self.dict = {}

        for i in range(20):
            pair = get_word_pair(language)
            self.dict[pair[0]] = pair[1]


    def get_word(self):
        return random.choice(list(self.dict.items()))

    
