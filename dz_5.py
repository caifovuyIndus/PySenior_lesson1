import inspect

class Person:
    name: str
    surname: str
    age: int

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def info_person(self):
        print(f'Особистість: {self.name} | {self.surname} | {self.age}')

class Teacher(Person):
    subject: str
    hours: int

    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_teacher(self):
        print(f'Вчитель: {self.subject} | {self.hours}')

    def info_all(self):
        self.info_person()
        self.info_teacher()

class Group:
    name: str
    student_count: int
    age_category: str

    def __init__(self, name: str, student_count: int, age_category: str):
        self.name = name
        self.student_count = student_count
        self.age_category = age_category

    def info_group(self):
        print(f'Група: {self.name} | Студенти: {self.student_count} | Вікова категорія: {self.age_category}')

class Student(Person):
    progress: float
    group: Group

    def __init__(self, name: str, surname: str, age: int, progress: float, group: Group):
        super().__init__(name=name, surname=surname, age=age)
        self.progress = progress
        self.group = group
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        self.pensione = value >= 60

    def info_student(self):
        print(f'Студент: Успішність: {self.progress}')
        self.group.info_group()

    def info_all(self):
        self.info_person()
        self.info_student()

class Worker(Person):
    position: str
    duties: str

    def __init__(self, name: str, surname: str, age: int, position: str, duties: str):
        super().__init__(name=name, surname=surname, age=age)
        self.position = position
        self.duties = duties
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        self.pensione = value >= 60

    def info_worker(self):
        print(f'Працівник: Посада: {self.position} | Обов’язки: {self.duties}')

    def info_all(self):
        self.info_person()
        self.info_worker()

# Інтроспекція
classes = [Student, Worker, Teacher, Person]

for cls in classes:
    print(f'Клас: {cls.__name__}')
    attributes = [name for name, value in inspect.getmembers(cls) if not callable(value) and not name.startswith("__")]
    methods = [name for name, value in inspect.getmembers(cls) if callable(value) and not name.startswith("__")]

    print("Атрибути:", attributes)
    print("Методи:", methods)
    print("-")
