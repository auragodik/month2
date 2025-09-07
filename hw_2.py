class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
    def introduce(self):
            print(f"Меня зовут {self.name}, мне {self.birth_date} лет, я занимаюсь {self.occupation}.")
class Classmate(Person):
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
    def introduce(self):
        print(f"Меня зовут {self.name}, я одноклассник Нурадила, мне {self.birth_date} лет, я занимаюсь {self.occupation}.")
class Friend(Person):
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
    def introduce(self):
        print(f"Меня зовут {self.name}, я друг Нурадила, мне {self.birth_date} лет, я занимаюсь {self.occupation}.")
cl1 = Classmate('Чынгыз', '17', 'луксмаксингом')
cl2 = Classmate('Барсбек', '17', 'учебой')
fr1 = Friend('Арсен', '16', 'чтением книг')
fr2 = Friend("Эрасыл", "17", 'моделингом')
fr3 = Friend('Азирет', "17", 'боксом')
cl1.introduce()
cl2.introduce()
fr1.introduce()
fr2.introduce()
fr3.introduce()