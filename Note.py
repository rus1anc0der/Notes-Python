from datetime import datetime
from random import randint


class Note:
    """Заметки"""

    def __init__(self, title, text_notes):
        self.id = randint(0, 100000)
        self.date_of_creation = datetime.now().strftime("%d/%m/%y %I:%M")
        self.text_notes = text_notes
        self.date_of_change = datetime.now().strftime("%d/%m/%y %I:%M")
        self.title = title
