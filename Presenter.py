import View
import Model
import Menu


def starts():
    while True:
        select = View.menu()
        match select:
            case 1:
                if Model.new_file():
                    View.print_message(Menu.new_succesful)
                else:
                    View.print_message(Menu.error_load)
            case 2:
                if Model.open_file():
                    View.print_message(Menu.load_succesful)
                else:
                    View.print_message(Menu.error_load)
            case 3:
                if Model.save_file():
                    View.print_message(Menu.save_succesful)
                else:
                    View.print_message(Menu.error_save)
            case 4:
                View.show_notebook(Model.notebook, Menu.empty_book)
            case 5:
                new = View.add_notebooks()
                Model.add_notebook(new)
                View.print_message(Menu.add_succesful(new.get('Название заметки')))
            case 6:
                word = View.search_word()
                result = Model.search(word)
                View.show_notebook(result, Menu.empty_search(word))
            case 7:
                word = View.search_word()
                result = Model.search(word)
                View.show_notebook(result, Menu.empty_search(word))
                if result!= {}:
                    id_cnt = View.change_notebook()
                    change_ct = View.change_ct()
                    Model.change_notebook(id_cnt, change_ct)
                    View.print_message(Menu.change_finish)
            
            case 8:
                word = View.search_word()
                result = Model.search(word)
                View.show_notebook(result, Menu.empty_search(word))
                if result!= {}:
                    id_cnt = View.remove_notebook()
                    if id_cnt != None:
                        Model.remove_notebook(id_cnt)
                        View.print_message(Menu.remove_finish)
                    else:
                        View.print_message(Menu.remove_repeal)
            case 9:
                break