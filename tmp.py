import textwrap
import re


def text_formatting():
    text = "34234   ,, , , , , , , , , ,, import textwrap. I!!! have ,,,,,,,    imported .,.,.,.,.,. .,.,!!!aaa list of names from a csv file and want to print each name a new line, how would i go about this as the program i have wrote prints it all on one line?"
    text=textwrap.shorten(text, width=99999999999)
    text=textwrap.fill(text)
    word_list = re.sub(r'[^\w\s]+|[\d]+', r'', text).replace('\n', '')   #.split(' ')
    word_list = textwrap.shorten(word_list, width=99999999999).split(' ')
    print(word_list)
    return word_list
text_formatting()