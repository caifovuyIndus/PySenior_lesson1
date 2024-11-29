class Student:
    def __init__(self, name, money=100, knowledge=50, fatigue=0):
        self.name = name
        self.money = money
        self.knowledge = knowledge
        self.fatigue = fatigue

    def work(self):
        self.money += 50
        self.fatigue += 20
        print(f"{self.name} поработал и заработал деньги. Деньги: {self.money}, усталость: {self.fatigue}")

    def study(self):
        """Студент учится, увеличивая знания, но также усталость."""
        if self.fatigue < 70:
            self.knowledge += 10
            self.fatigue += 15
            print(f"{self.name} учился. Знания: {self.knowledge}, усталость: {self.fatigue}")
        else:
            print(f"{self.name} слишком устал, чтобы учиться.")

    def rest(self):
        if self.money >= 10:
            self.money -= 10
            self.fatigue -= 30
            self.fatigue = max(0, self.fatigue)
            print(f"{self.name} отдыхал. Деньги: {self.money}, усталость: {self.fatigue}")
        else:
            print(f"{self.name} недостаточно денег для отдыха.")

    def live_one_day(self):
        if self.money < 20:
            print(f"{self.name} решил работать, чтобы заработать денег.")
            self.work()
        elif self.knowledge < 70:
            print(f"{self.name} решил учиться, чтобы улучшить знания.")
            self.study()
        else:
            print(f"{self.name} решил отдохнуть.")
            self.rest()

    def live_one_year(self):
        for day in range(365):
            print(f"\nДень {day + 1}: ")
            self.live_one_day()
            if self.fatigue >= 100:
                print(f"{self.name} слишком устал и заболел! Отдыхает неделю.")
                for _ in range(7):
                    self.rest()

student = Student(name="Єгор")
student.live_one_year()