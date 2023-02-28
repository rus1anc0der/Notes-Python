import json
from pprint import pprint
from Note import Note

class CreateNote:
    """Сохранение заметок"""
    def __init__(self):
        self.data = {
            "Notes": [],
        }
        self.file_name = "notes.json"

    # Cоздание файла
    def create(self):
        self.data = json.dumps(self.data)
        self.data = json.loads(str(self.data))
        with open(self.file_name, 'w', encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    # Чтение из файла
    def read(self):
        try:
            with open(self.file_name, 'r', encoding="utf-8") as file:
                return pprint(json.load(file))
        except FileNotFoundError:
            print("Для начала нужно добавить заметку! ")

    # Изменения заголовка
    def changeTitle(self,i):
        title = input('Введите изменения: ')
        self.data['Notes'][i]['title'] = title

    # Изменения тела заметки
    def changeText(self, i):
        text = input('Введите изменения: ')
        self.data['Notes'][i]['text_notes'] = text

    # Добавить заметку
    def createNote(self, note):
        self.data['Notes'].append(note.__dict__)

    # Удаление заметки
    def delNote(self, index):
        self.data['Notes'].pop(index)





test = CreateNote()
# test_note = Note('1', '2')
# for i in range(5):
#     test.data["Notes"].append(Note("123", "123").__dict__)
# test.create()
#
# # test.read()
# # можно заменить любые значения
# # print(test.data['Notes'][0])
# test.data['Notes'][0]['id'] = 777
# # print(test.data['Notes'][0])
# test.changeText(0, 'ololololo')
# test.changeTitle()
# test.read()
# test.create()
#
# print(test.data['Notes'][0])
# if test.data['Notes'][0]['id']  == 777:
#     test.data['Notes'].pop(0)
#
#
#
# test.create()
# test.read()