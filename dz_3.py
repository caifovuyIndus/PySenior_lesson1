class StudySubject:
    name: str
    hours: int
    enable: bool

    def __init__(self, name: str, hours: int, enable: bool):
        self.name = name
        self.hours = hours
        self.enable = enable

    def info_study(self):
        print(f'Study: {self.name} | {self.hours}')

class Student:
    name: str
    surname: str
    studies: list

    def __init__(self, name: str, surname: str, studies: list):
        self.name = name
        self.surname = surname
        self.studies = studies

    def info_student(self):
        print(f'Student: {self.name} | {self.surname}')

    def info_all(self):
        self.info_student()
        for study in self.studies:
            study.info_study()

class Group:
    name: str
    age_category: str
    students: list

    def __init__(self, name: str, age_category: str, students: list):
        self.name = name
        self.age_category = age_category
        self.students = students

    @property
    def student_count(self):
        return len(self.students)

    def info_group(self):
        print(f'Group: {self.name} | Age Category: {self.age_category} | Students: {self.student_count}')
        for student in self.students:
            student.info_all()

num_subjects = int(input("Введіть кількість предметів: "))
subjects = []
for _ in range(num_subjects):
    name = input("Введіть назву предмета: ")
    hours = int(input("Введіть кількість годин: "))
    enable = input("Чи активний цей предмет (так/ні): ").lower() == "yes"
    subjects.append(StudySubject(name=name, hours=hours, enable=enable))

num_students = int(input("Введіть кількість студентів: "))
students = []
for _ in range(num_students):
    name = input("Введіть ім'я студента: ")
    surname = input("Введіть прізвище студента: ")
    student_subjects = []
    for subject in subjects:
        if input(f"Чи повинен студент вивчати {subject.name}? (так/ні): ").lower() == "yes":
            student_subjects.append(subject)
    students.append(Student(name=name, surname=surname, studies=student_subjects))

group_name = input("Введіть назву групи: ")
age_category = input("Введіть вікову категорію: ")
group = Group(name=group_name, age_category=age_category, students=students)

group.info_group()
