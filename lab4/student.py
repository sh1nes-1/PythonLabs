from datetime import date
from person import Person


class Student(Person):
    def __init__(self, last_name, first_name, surname, birthday, faculty, group, studentship, middle_mark):
        Person.__init__(self, last_name, first_name, surname, birthday)

        self.faculty = faculty
        self.group = group
        self.studentship = studentship
        self.middle_mark = middle_mark
