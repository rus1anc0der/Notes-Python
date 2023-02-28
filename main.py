from datetime import datetime
from pprint import pprint

from Note import Note
from createNote import CreateNote

note = CreateNote()


def menu():
    while True:
        print("Консольное приложение Заметки\n"
              "Введите команду:  \n"
              "1) Посмотреть все заметки\n"
              "2) Добавить заметку\n")
        try:
            i = int(input())
        except ValueError:
            print("Введите номер команды")
            menu()
        match i:
            case 1:
                note.read()
                nextMenu()
            case 2:
                title = input("Введите заголовок: \n")
                text = input("Введите тело заметки: \n")
                note.createNote(Note(title, text))
                note.create()
                print("Заметка успешно записана! ")


def nextMenu():
    while True:
        print("1) Удалить \n"
              "2) Изменить \n"
              "3) Сортировать по дате\n"
              "\n4) назад")
        try:
            j = int(input())
        except ValueError:
            print("Введите номер команды")
            nextMenu()
        match j:
            case 1:
                num = int(input("Введите ID заметки для удаления: "))
                for i in range(0, len(note.data['Notes'])):
                    if note.data['Notes'][i]['id'] == num:
                        note.delNote(i)
                        note.create()
                note.read()
                menu()
            case 2:
                num = int(input('Введите ID заметки для изменения: '))
                for i in range(0, len(note.data['Notes'])):
                    if note.data['Notes'][i]['id'] == num:
                        k = int(input('Что будем изменять?\n'
                                      '1) Заголовок\n'
                                      '2) Тело заметки\n'))
                        match k:
                            case 1:
                                note.changeTitle(i)
                                note.data['Notes'][i]["date_of_change"] = datetime.now().strftime("%d/%m/%y %I:%M")
                                note.create()
                            case 2:
                                note.changeText(i)
                                note.data['Notes'][i]["date_of_change"] = datetime.now().strftime("%d/%m/%y %I:%M")
                                note.create()
            case 3:
                pprint(note.data['Notes'])
            case 4:
                menu()



menu()
