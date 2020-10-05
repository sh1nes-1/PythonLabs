from datetime import datetime, date


class Person:
    def __init__(self, last_name, first_name, surname, birthday):
        self.last_name = last_name
        self.first_name = first_name
        self.surname = surname
        self.birthday = birthday

    def get_age(self):
        return (datetime.now() - self.birthday).days // 365.25
