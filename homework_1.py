class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_status = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет! Меня зовут {self.name}, я {self.occupation}. "
              f"Дата рождения: {self.birth_date}. У меня {edu_status}.")
person_1 = Person('Толонбаев Азирет', '2.05.2008', 'лидер', False)
person_2 = Person('Раев Эрасыл', '15.03.2008', 'зам старосты', False)
person_3 = Person('Айдакеев Арсен', '26.12.2008', 'тип', False)
for person in (person_1, person_2, person_3):
    print(f"Имя: {person.name}")
    print(f"Дата рождения: {person.birth_date}")
    print(f"Профессия: {person.occupation}")
    print(f"Высшее образование: {person.higher_education}")
    print("-" * 40)
person_1.introduce()
person_2.introduce()
person_3.introduce()
