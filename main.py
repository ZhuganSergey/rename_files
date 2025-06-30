import os
from translitua import translit

inbox_path = './inbox'

import re 
def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def main():
    contents = os.listdir(inbox_path)
   
    for file in contents:
        if has_cyrillic(file):
            new_file_name = translit(file)
            os.rename(os.path.join(inbox_path, file), os.path.join(inbox_path, new_file_name))
            
            print(f'file: {file}, renamed to : {new_file_name}')
            
if __name__ == "__main__":
    main()
