import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('en')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(18, 60),
        salary=random.randint(20000, 50000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )


def generated_file():
    path = rf'C:\Users\user\PycharmProjects\Automation_python\filetest{random.randint(0, 100)}.txt'
    # r - regular expression
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 100)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=['White', 'Blue', 'Green', 'Black']
    )


def generated_date():
    yield Date(
        year=fake_en.year(),
        month=fake_en.month_name(),
        day=fake_en.day_of_month(),
        time='12:00'

    )
