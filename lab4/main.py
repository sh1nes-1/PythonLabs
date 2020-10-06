from datetime import datetime
from student import Student

students = []

with open('data.csv', 'r', encoding='utf-8') as dataFile:
    for line in dataFile:
        words = line.split(';')
        s = Student(
            words[0],
            words[1],
            words[2],
            datetime(year=int(words[3]), month=int(words[4]), day=int(words[5])),
            words[6],
            int(words[7]),
            int(words[8]),
            int(words[9]),
        )

        students.append(s)

all_studentship = 0
all_age = 0

for student in students:
    all_studentship += student.studentship
    all_age += student.get_age()

middle_age = all_age / len(students)

print('All studentship: ', all_studentship)
print('Middle age: ', middle_age)