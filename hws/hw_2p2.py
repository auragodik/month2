class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
    def introduce(self):
            print(f"Меня зовут {self.name}, мне {self.birth_date} лет, я занимаюсь {self.occupation}.")
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.group_name = group_name
    def introduce(self):
        print(f"Меня зовут {self.name}, я одноклассник Нурадила, мне {self.birth_date} лет, я занимаюсь {self.occupation}, учились в {self.group_name}.")
class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.hobby = hobby
    def introduce(self):
        print(f"Меня зовут {self.name}, я друг Нурадила, мне {self.birth_date} лет, я занимаюсь {self.occupation}, хобби и есть {self.hobby}.")
cl1 = Classmate('Чынгыз', '17', 'луксмаксингом', '11Ж')
cl2 = Classmate('Барсбек', '17', 'учебой', '11Ж')
fr1 = Friend('Арсен', '16', 'чтением книг', "чтение книг")
fr2 = Friend("Эрасыл", "17", 'моделингом', "моделинг")
fr3 = Friend('Азирет', "17", 'боксом', 'бокс')
for prsn in [cl1, cl2, fr1, fr2, fr3]:
    prsn.introduce()