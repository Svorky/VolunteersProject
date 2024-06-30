from find import Find
from volunteer import Volunteer
from city import City
from car import Car
from volunteer_car import VolunteerCar
# import Bussiness
from animal import Animal
from volunteer_animal import VolunteerAnimal
from language import Language
from volunteer_language import VolunteerLanguage
from database import select, select_volunteer
from helpers import pretty_print
from update import Update


def add_volunteer() -> int:
    print("You choose to add a new volunteer.")
    print("Please, type the following attributes.")
    print("If you don't want to fill some information leave a space (press Enter)")
    car = Car()
    animal = Animal()
    volunteer = {
        'name': input("Name: ").strip(),
        'birth_date': input("Birth date (dd/mm/yyyy): ").strip(),
        'telephone': input("Telephone: ").strip(),
        'city_id': city_question(),
        'language': language_question(),
        'has_driver_licence': car.driver_licence_question(),
        'has_car': car.car_question(),
        # 'has_bussiness': bussiness_question(),
        "love_animals": animal.question()
    }
    v = Volunteer(volunteer)
    id = v.create()
    VolunteerLanguage.create(id, volunteer['language'])
    if car.id:
        VolunteerCar.create(id, car.id)
    if animal.id:
        VolunteerAnimal.create(id, animal.id)
    vol = select_volunteer({"volunteer.id = %s":id})
    pretty_print(vol)


def show_all() -> None:
    result = Volunteer.get_all()
    pretty_print(result)


def find() -> Volunteer:
    print("Find by: ")
    print('''
          1. By name
          2. By language
          3. By driving licence
          4. By car
          5. By animal
          6. By city
          ''')
    user = input().strip()
    if user == '':
        return None
    match int(user):
        case 1:
            Find.by_name()
        case 2:
            Find.by_language()
        case 3:
            Find.by_driving_licence()
        case 4:
            Find.by_car()
        case 5:
            Find.by_animal()
        case 6:
            Find.by_city()
        case _:
            print("Wrong number.")


def update():
    # user = input('''Do you want to choose a volunteer or type a name:
    #              1. Choose
    #              2. I know name
    #              ''').strip()
    # if int(user) == 1:
    result = Volunteer.get_all()
    # for idx, row in enumerate(result):
    #     print(f"{idx+1}. {row['name']}")
    print("Choose a volunteer:")
    pretty_print(result)
    id = input("Type number: ").strip()
    v = result[int(id)-1]
    print()
    pretty_print([v])
    print()
    print("What you want to change?")
    keys = list(v.keys())
    keys.remove('id')
    for [idx, key] in enumerate(keys):
        print(f"{idx+1}. {key}")
    col = int(input().strip())
    col_name = keys[col-1]
    match col_name:
        case "volunteer_name":
            Update.name(v)
        case "birth_date":
            Update.birth_date(v)
        case "city":
            Update.city(v)
        case "telephone":
            Update.telephone(v)
        case "language":
            Update.language(v)
        case 'has_driver_licence':
            Update.has_driver_licence(v)
        case 'has_car':
            Update.has_car(v)
        case 'car':
            Update.has_car(v)
        case 'love_animals':
            Update.love_animals(v)
        case 'animal':
            Update.love_animals(v)
        case _:
            print("There is no such column.")

    # else:
    #     name = "%"
    #     name += input("Type a name: ").strip()
    #     query = "select id, name from volunteer where name ilike %s"
    #     name += "%"
    #     result = select(query, [name])
    #     v_result = Volunteer.convert_to_self(result)
    #     pretty_print(v_result)
    #     for idx, row in enumerate(v_result):
    #         print(f"{idx+1}. {row.name}")
    #     id = input("Type number: ").strip()
    #     v_result[int(id)-1].delete()
    #     print(f"{v_result[int(id)-1].name} was removed.")
    #     input("Press Enter...")


def delete():
    user = input('''Do you want to choose a volunteer or type a name:
                 1. Choose
                 2. I know name
                 ''').strip()
    if int(user) == 1:
        result = Volunteer.get_all()
        pretty_print(result)
        id = input("Type number: ").strip()
        vid = result[int(id)-1]['id']
        Volunteer.get_by_id(vid)[0].delete()
        print(f"{result[int(id)-1]['volunteer_name']} was removed.")
        input("Press Enter...")
    else:
        name = "%"
        name += input("Type a name: ").strip()
        query = "select id, name from volunteer where name ilike %s"
        name += "%"
        result = select_volunteer({"volunteer.name ilike %s": name})
        if len(result) == 0:
            print("There is no volunteer with such name.")
            input("Press Enter to continue...")
            return None
        v_result = Volunteer.convert_to_self(result)
        pretty_print(result)
        # for idx, row in enumerate(v_result):
        #     print(f"{idx+1}. {row.name}")
        id = input("Type number: ").strip()
        v_result[int(id)-1].delete()
        print(f"{result[int(id)-1]['volunteer_name']} was removed.")
        input("Press Enter...")


def bussiness_question():
    buss = input("Have a bussiness (Y/N): ").strip().lower()
    if buss == 'y':
        print("Which bussiness do you have:")
        Bussiness.get_all()
        v_buss = input("Choose a bussiness or type a new one: ").strip()
        if v_buss.isdigit():
            pass
        else:
            Bussiness.add()
    return {
        "has_bussiness": buss,
        "bussiness": v_buss
    }


def animal_question():
    animal = input("Love animals (Y/N): ").strip().lower()
    if animal == 'y':
        print("Which animals do you love:")
        Animal.get_all()
        v_animal = input("Choose an animal or type a new one: ").strip()
        if v_animal.isdigit():
            pass
        else:
            Animal.add()
    return {
        "has_animal": animal,
        "animal": v_animal
    }


def language_question():
    print("Which languages do volunteer speaks:")
    languages = Language.get_all()
    for [idx, row] in enumerate(languages):
        s = f"{idx+1}. {row["name"]}"
        print(s)
    v_language = input("Choose an language or type a new one: ").strip()
    if v_language.isdigit():
        return languages[int(v_language)-1]['id']
    else:
        language = Language(v_language)
        id = language.add()
        return id


def city_question():
    cities = City.get_all()
    print("Cities: ")
    for [idx, row] in enumerate(cities):
        s = f"{idx+1}. {row["name"]}"
        print(s)
    v_city = input("Choose city or write a new one: ").strip()
    if v_city.isdigit():
        return cities[int(v_city)-1]['id']
    else:
        city = City(v_city)
        id = city.add()
        return id

# def pretty_print(data) -> None:
#     for row in data:
#         print(row)
