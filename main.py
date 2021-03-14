import tkinter as tk
import re
from googletrans import Translator
import textwrap

# Берем напечатаный текст в input_text и разбивем его на слова удаляя все символы  и пробелы
# наличие текста
def text_formatting():
    text = input_text.get('1.0', 'end-1c')
    text=textwrap.shorten(text, width=99999999999)
    text=textwrap.fill(text)
    word_list = re.sub(r'[^\w\s]+|[\d]+', r'', text).replace('\n', '').split(' ')
    print(word_list)
    return word_list


# Переводим и записываем в файл "Текст"
def translate_list():
    # проверка на наличие текста в input_text
    if input_text.get('1.0', 'end-1c') == '':
        pass
    # перевод текста вывод в output_text и сохранение в text.txt
    else:
        translator = Translator()
        list = text_formatting()
        result = []
        for word in list:
            r = open('text.txt', 'r', encoding='UTF-8')
            old_text = r.read().split('\n')
            r.close()
            translation = translator.translate(word, src='en', dest='ru').text
            if word == translation:
                pass
            else:
                dict = str(word + '  -  ' + translation)
                if str(dict in old_text) == 'True':
                    pass
                else:
                    output_text.insert(0.0, dict + '\n')
                    result.append(dict)
                    f = open('text.txt', 'a', encoding='UTF-8')
                    f.write(str(dict) + '\n')
                    f.close()
                    print(dict)
        return result


window = tk.Tk()
window.title('Переводчик')
window.geometry('800x600+400+200')

lbl = tk.Label(window, text="Введите текст для перевода", font=("Arial Bold", 10))
lbl.place(x=1, y=2)

input_text = tk.Text(window, width=40, height=35)
input_text.place(x=3, y=30)

output_text = tk.Text(window, width=40, height=35)
output_text.place(x=450, y=30)
# кнопка "перевод"
btnStart = tk.Button(window, text='Перевести', command=translate_list)
btnStart.place(x=350, y=300)
# # Кнопка "Сохранить"
# btnSave = tk.Button(window, text="Сохранить", underline=0)
# btnSave.place(x=350, y=400)




window.mainloop()
