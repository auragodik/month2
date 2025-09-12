class Person:
    def __init__(self, name, birth_date, occupation, high_education=False):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__high_education = high_education
    def introduce(self):
        edu = "есть высшее образование" if self.__high_education else "нет высшего образования"
        print(f"Меня зовут {self.name}, мне {self.birth_date} лет, "
              f"я занимаюсь {self.__occupation}, у меня {edu}")
    def get_occupation(self):
        return self.__occupation
    def has_higher_education(self):
        return self.__high_education
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, high_education=False):
        super().__init__(name, birth_date, occupation, high_education)

    def introduce(self):
        edu = "есть высшее образование" if self.has_higher_education() else "нет высшего образования"
        print(f"Меня зовут {self.name}, я одноклассник Нурадила, "
              f"мне {self.birth_date} лет, я занимаюсь {self.get_occupation()}, у меня {edu}.")
class Friend(Person):
    def __init__(self, name, birth_date, occupation, high_education=False):
        super().__init__(name, birth_date, occupation, high_education)

    def introduce(self):
        edu = "есть высшее образование" if self.has_higher_education() else "нет высшего образования"
        print(f"Меня зовут {self.name}, я друг Нурадила, "
              f"мне {self.birth_date} лет, я занимаюсь {self.get_occupation()}, у меня {edu}.")
cl1 = Classmate('Чынгыз', '17', 'луксмаксингом', high_education=False)
cl2 = Classmate('Барсбек', '17', 'учебой', high_education=False)
fr1 = Friend('Арсен', '16', 'чтением книг', high_education=False)
fr2 = Friend("Эрасыл", "17", 'моделингом', high_education=False)
fr3 = Friend('Азирет', "17", 'боксом', high_education=False)

cl1.introduce()
cl2.introduce()
fr1.introduce()
fr2.introduce()
fr3.introduce()
