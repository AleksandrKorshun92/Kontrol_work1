import json
notebook ={}
path = 'notebook.json'

def new_file():
    try:
        with open(path,'w', encoding='UTF-8') as file:
            json.dump(notebook, file, ensure_ascii=False)
        return True
    except:
        return False

def open_file():
    global notebook
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            notebook = json.load(file)
        return True
    except:
        return False

def save_file():
    try:
        with open(path,'w', encoding='UTF-8') as file:
            json.dump(notebook, file, ensure_ascii=False)
        return True
    except:
        return False


def search(word: str) -> dict[int:dict[str,str]]:
    result = {}
    for i, f in notebook.items():
        if word.lower() in ' '.join(f.values()).lower():
            result[i] = f
    return result


def check_id():
    if notebook:
        return max(list(map(int, notebook))) + 1
    return 1

def add_notebook(new:dict[str,str]):
    new_notebook = {check_id(): new}
    notebook.update(new_notebook)

def change_notebook(id_cnt, change_ct):
    notebook[id_cnt] = change_ct
    notebook.update(notebook)
    

def remove_notebook(id_cnt):
        notebook.pop(id_cnt)