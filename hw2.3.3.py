documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    #"name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def docnumber_of_man(data):
    request = input('Введите номер документа: ')
    for document in data:
        if request == document['number']:
            # print('Такого номера документа нет')
            print(f'Документ номер {request} принадлежит: {document["name"]}')
            break
    else:
        print('Такого номера докумета нет')
        # print(f'Документ номер {request} принадлежит: {document["name"]}')


def list_of_all_docs(data):
    for document in data:
        print(
            f'{document["type"]} {document.get("number")} {document["name"]}')


def shelf_of_docnumber(data):
    request = input('Введите номер документа: ')
    for shelf, shelf_content in data.items():
        if request in shelf_content:
            print(f'Документ на полке: {shelf}')
            break
    else:
        print('Такого документа нет')


def add_new_document(docdata, shelfdata):
    input_type = input('Тип документа: ')
    input_number = input('Номер документа: ')
    input_name = input('Имя: ')
    input_shelf = input('На полку 1, 2 или 3?: ')
    docdata[0:0] = [{
        "type": input_type,
        "number": input_number,
        "name": input_name
    }]
    if input_shelf not in shelfdata:
        shelfdata.update({input_shelf: []})
        print(f'Создана новая полка: {input_shelf}')
    for shelf, shelf_content in shelfdata.items():
        if input_shelf in shelf:
            shelf_content.append(input_number)
            print(f'Документ на полке: {shelf}')
            for document in docdata:
                print(f'{document["type"]} {document.get("number")} {document["name"]}')


def delete_docnumber(docdata, shelfdata):
    request = input('Какой номер документа удалить?: ')
    for document in docdata:
        if request == document.get('number'):
            del document["number"]
            print(f'{document["type"]} {document.get("number")} {document["name"]}')
            for shelf, shelf_content in shelfdata.items():
                if request in shelf_content:
                    shelf_content.remove(request)
                    print(f'Номер документа {request} удален с полки {shelf}.')
                    break
            break

    else:
        print('Такого номера документа нет')


def move_number(data):
    request_number = input('Введите номер документа: ')
    request_shelf = input('Ведите номер полки для перемещения: ')
    if request_shelf in data:
        for shelf, shelf_content in data.items():
            if request_number in shelf_content:
                print(f'Документ был на полке: {shelf}')
                shelf_content.remove(request_number)
                if request_shelf in shelf:
                    shelf_content.append(request_number)
                    print(f'Документ перемещен на полку: {shelf}')
                break
        else:
            print('Такого номера документа нет')
    else:
        data.update({request_shelf: []})
        print(f'Создана новая полка: {request_shelf}')
        for shelf, shelf_content in data.items():
            if request_number in shelf_content:
                print(f'Документ был на полке: {shelf}')
                shelf_content.remove(request_number)
                if request_shelf in shelf:
                    shelf_content.append(request_number)
                    print(f'Документ перемещен на полку: {shelf}')

        else:
            print('Такого номера документьа нет')


def add_shelf(data):
    request = input('Введите название новой полки: ')
    if request not in data:
        data.update({request: []})
        print(f'Создана новая полка: {request}')
    else:
        print('Полка уже существует')
    for key, value in data.items():
        print(f'Полка: {key}, содержимое: {value}')

def try_func(data):
    for doc in data:
        try:
            print(doc["name"])
        except KeyError:
            print(f'Документ {doc["number"]} не имеет имени')


while True:
    user_input = input('Введите одну из команд(x,p,l,s,a,d,m,as,q): ')
    if user_input == 'p':
        docnumber_of_man(
            documents
        )  # команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    elif user_input == 'l':
        list_of_all_docs(
            documents
        )  # команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    elif user_input == 's':
        shelf_of_docnumber(
            directories
        )  # команда, которая спросит номер документа и выведет номер полки, на которой он находится
    elif user_input == 'a':
        add_new_document(
            documents, directories
        )  # команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    elif user_input == 'd':
        delete_docnumber(
            documents, directories
        )  # команда, которая спросит номер документа и удалит его из каталога и из перечня полок
    elif user_input == 'm':
        move_number(
            directories
        )  # команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    elif user_input == 'as':
        add_shelf(
            directories
        )  # оманда, которая спросит номер новой полки и добавит ее в перечень
    elif user_input == 'x':
        try_func(documents) # функция для ДЗ 2.3.3
    elif user_input == 'q':
        print('Конец запроса')
        break
