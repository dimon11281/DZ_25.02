from model import load_base, add_shoes, edit_base, del_base

def com_with_user():
    comm = input("""
        1. Просмотр базы обуви
        2. Добавление обуви в базу
        3. Редактирование позиции в базе
        4. Удаление позиции из базы
    """)
    if comm == "1":
        load_base()
    elif comm == "2":
        add_shoes()
    elif comm == "3":
        edit_base()
    elif comm == "4":
        del_base()
    else:
        return com_with_user()


com_with_user()