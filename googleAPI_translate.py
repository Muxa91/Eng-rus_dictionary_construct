import re
from googletrans import Translator
from tkinter import *
import textwrap


text = input("Вставьте текст для перевода   ")

def text_formatting(self):
    text = self
    text=textwrap.shorten(text, width=99999999999)
    text=textwrap.fill(text)
    word_list = re.sub(r'[^\w\s]+|[\d]+', r'', text).replace('\n', '').split(' ')
    print(word_list)
    return word_list


# Переводим и записываем в файл "Текст"
def translate_list(self):
    translator = Translator()
    list = text_formatting(self)
    result = []
    for word in list:
        r = open('text.txt', 'r', encoding='UTF-8')
        old_text = r.read().split('\n')
        r.close()
        translation = translator.translate(word, src='en', dest='ru').text
        if word == translation:
            pass
        else:
            dict = str({word: translation})
            if str(dict in old_text) == 'True':
                pass
            else:
                result.append(dict)
                f = open('text.txt', 'a', encoding='UTF-8')
                f.write(str(dict) + '\n')
                f.close()
                print(dict)
    return result


text = translate_list(text)
print(text)
