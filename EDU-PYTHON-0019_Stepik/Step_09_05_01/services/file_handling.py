import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:

    list_breakers = [',', '.', '!', ':', ';', '?']

    end_text = text[start:start+size+1]

    if(start+size> len(text)):
        return [end_text, len(end_text)]

    crnt_dot = False
    for i in range(0, len(list_breakers)-1):
        if text[start+size+1] == list_breakers[i]:
            crnt_dot = True

    next_dot = False
    if(start+size+2>len(text)):
        next_dot = False
    else:
        for i in range(0, len(list_breakers)-1):
            if text[start+size+1] == list_breakers[i]:
                next_dot = True

#    print(end_text)
    end_ind = start+size
    if(crnt_dot and next_dot or not(crnt_dot)):
        end_prob = end_text.rfind(' ')
#        print(end_prob)
        end_ind = start + end_prob

    end_text = text[start:end_ind]

#    print(text[start+size],'@',end_ind,'@',crnt_dot,'@',next_dot,'@',end_text,'@', sep = '')
    pageend_ind=0
    for i in range(0, len(list_breakers)-1):
        ind = end_text.rfind(list_breakers[i])

        if ind> pageend_ind:
            pageend_ind = ind
        
    end_text = text[start:start+pageend_ind+1]
    return [end_text, pageend_ind+1]

def prepare_book(path: str) -> None:
    start = 0
    page_number = 1
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    while start < len(text):
        page_text, length = _get_part_text(text, start, PAGE_SIZE)
        if page_text:
            book[page_number] = page_text.lstrip()
            page_number += 1
            start += length
        else:
            break

prepare_book(
    os.path.join(sys.path[0], os.path.normpath(BOOK_PATH))
    )