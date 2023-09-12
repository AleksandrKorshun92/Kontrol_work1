import Menu

def menu() -> int:
    print(Menu.main_menu[0])
    for i in range(1, len(Menu.main_menu)):
        print(f'\t{i}.{Menu.main_menu[i]}')
    while True:
        select = input(Menu.select_menu)
        if select.isdigit() and 0<int(select)<int(len(Menu.main_menu)):
            return int(select)
        print(Menu.input_error)

def show_notebook(book: dict[int:dict[str,str]], message):
    if book:
        max_name = []
        max_comment = []
        for cnt in book.values():
            max_name.append(len(cnt.get('Дата заметки')))
            max_comment.append(len(cnt.get('Заметка')))
        size_name = max(max_name)
        size_comment = max(max_comment)
        print('\n'+'='*(size_name + size_comment +7))
        for index, contact in book.items():
            print(f'{index:>3}. {contact.get("Дата заметки"):<{size_name+1}} {contact.get("Заметка"):<{size_comment+1}}')
        print('=' * (size_name +  size_comment + 7) + '\n')
                      
    else:
        print(message)

def print_message(message: str):
    print('\n'+'='*len(message))
    print(message)
    print('='*len(message)+'\n')

def add_notebooks():
    new = {}
    for key, value in Menu.new_book.items():
        new[key] = input(value)
    return new


def search_word() ->str:
    return input(Menu.search_word)

def remove_notebookt():
        a = input(Menu.remove_contact)
        b = int(input(Menu.remove_danger))
        if b == 1:
            return a     

def change_notebook():
    return input(Menu.change)

def change_ct():
    new = {}
    for key, value in Menu.change_contact.items():
        new[key] = input(value)
    return new
