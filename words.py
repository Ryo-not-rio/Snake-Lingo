from googletrans import Translator
import wordfreq
import random
import threading
import pygame as py
import os
import pickle

lang_dict = {'Bulgarian': 'bg', 'Catalan': 'ca',
             'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Finnish': 'fi', 'French': 'fr', 
             'German': 'de', 'Greek': 'el', 'Hungarian': 'hu', 'Indonesian': 'id', 
             'Italian': 'it', 'Latvian': 'lv', 'Macedonian': 'mk', 'Malay': 'ms', 
             'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru',
             'Spanish': 'es', 'Swedish': 'sv', 'Turkish': 'tr', 'Ukrainian': 'uk'}
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
    try:
        lang_word = wordfreq.random_words(lang, nwords=1)
        while lang_word is None:
            lang_word = wordfreq.random_words(lang, nwords=1)
        eng_word = translator.translate(lang_word, src=lang, dest='en').text
        
        # Recursion happening here
        if len(lang_word) > 10 or len(eng_word) > 10 or (len(lang_word) == 1 and len(eng_word) == 1) \
            or (language != "English" and lang_word == eng_word) or lang_word[0].isupper():
            lang_word, eng_word = get_word_pair(language)
    except:
        with open("words.pkl", "rb") as f:
            dictionary = pickle.load(f)
        lang_word, eng_word = random.choice(dictionary[language])

    return lang_word, eng_word

def create_local_file(num):
    save_dict = {}
    for language, lang in lang_dict.items():
        save_dict[language] = []
        for j in range(num):
            lang_word = wordfreq.random_words(lang, nwords=1)
            while lang_word is None:
                lang_word = wordfreq.random_words(lang, nwords=1)
            eng_word = translator.translate(lang_word, src=lang, dest='en').text
            
            # Recursion happening here
            if len(lang_word) > 10 or len(eng_word) > 10 or (len(lang_word) == 1 and len(eng_word) == 1) \
                or (language != "English" and lang_word == eng_word) or lang_word[0].isupper():
                lang_word, eng_word = get_word_pair(language)

            save_dict[language].append((lang_word, eng_word))
    with open("words.pkl", "wb") as f:
        pickle.dump(save_dict, f)

class WordGenerator:
    def __init__(self, language, stats_collector, reversed=False):
        self.learnt_sound = py.mixer.Sound(os.path.join("sounds", "learnt.wav"))

        self.reverse = reversed
        self.stats_collector = stats_collector

        self.language = language
        self.dict = {}
        self.correct_row_dict = {}
        self.wrong_list = []
        self.use_wrong_list = False

        for i in range(20):
            pair = get_word_pair(language)
            self.dict[pair[0]] = pair[1]


    def correct(self, word):
        event = ["correct"]
        if self.use_wrong_list:
            self.wrong_list.remove(word)
            if len(self.wrong_list) == 0:
                self.use_wrong_list = False
        else:
            if word in self.correct_row_dict.keys():
                self.correct_row_dict[word] += 1
                if self.correct_row_dict[word] == 3:
                    ### learnt!! ###
                    py.mixer.Sound.play(self.learnt_sound)

                    del self.dict[word]
                    while word in self.wrong_list:
                        wrong_list.remove(word)

                    event.append("learnt")

                    def temp():
                        pair = get_word_pair(self.language)
                        self.dict[pair[0]] = pair[1]
                    
                    t = threading.Thread(target=temp)
                    t.start()               
            else:
                self.correct_row_dict[word] = 1

        self.stats_collector.events.append(event)

    
    def wrong(self, word):
        event = ["wrong"]
        if word in self.correct_row_dict.keys():
            del self.correct_row_dict[word]

        if not self.use_wrong_list:
            self.wrong_list.append(word)
            if len(self.wrong_list) >= 4:
                self.use_wrong_list = True
        self.stats_collector.events.append(event)

    def get_word(self, answer=False):
        if not self.reverse:
            if self.use_wrong_list and answer:
                lang_word = random.choice(self.wrong_list)
                return (lang_word, self.dict[lang_word])
            return random.choice(list(self.dict.items()))
        
        if self.use_wrong_list and answer:
            lang_word = random.choice(self.wrong_list)
            return (self.dict[lang_word], lang_word)
        return reversed(random.choice(list(self.dict.items()))[:])

    
if __name__ == "__main__":
    create_local_file(100)