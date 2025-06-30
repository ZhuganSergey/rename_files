import os
import re 
from translitua import translit as translit_ua
from transliterate import translit as translit_ru

inbox_path = './inbox'

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я,іІїЇєЄ]', text))

def main():
    contents = os.listdir(inbox_path)
   
    for file in contents:
        if has_cyrillic(file):
            filename_without_ua_symbols = translit_ua(file)
            filename_without_ua_ru_symbols = translit_ru(filename_without_ua_symbols, language_code='ru', reversed=True)

            os.rename(os.path.join(inbox_path, file), os.path.join(inbox_path, filename_without_ua_ru_symbols))
            
            print(f'file: {file}, renamed to : {filename_without_ua_ru_symbols}')
            
if __name__ == "__main__":
    main()
