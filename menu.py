# import VolunteersManager
from volunteer import Volunteer
from city import City
# import Car
# import Bussiness
# import Animal
# import Language
from database import select, insert

def add_volunteer() -> dict:
    print("You choose to add a new volunteer.")
    print("Please, type the following attributes.")
    print("If you don't want to fill some information leave a space (press Enter)")
    # v_name = input("Name: ").strip()
    # v_birth = input("Birth date (dd/mm/yyyy): ").strip()
    # v_city = input("City: ").strip()
    volunteer = {
        'name': input("Name: ").strip(),
        'birth_date': input("Birth date (dd/mm/yyyy): ").strip(),
        'telephone': input("Telephone: ").strip(),
        'city_id': city_question(),
        # 'language': language_question(),
        'has_driver_licence': input("Have a driving licence (Y/N): ").strip(),
        # 'car': car_question(),
        # 'has_bussiness': bussiness_question(),
        # "love_animals": animal_question()
    }
    query = f'''insert into volunteer ({", ".join(list(volunteer.keys()))})
    values
    ({", ".join(["%s" for _ in volunteer.keys()])})'''
    insert(query, list(volunteer.values()))
    return volunteer

def show_all() -> list:
    result = select("select * from volunteer")
    pretty_print(result)

def find() -> Volunteer:
    print("Find by: ")
    print('''
          1. By name
          2. By age
          3. By language
          4. By driving licence
          5. By car
          6. By animal
          7. By bussiness
          ''')

def update():
    vol = input("Type a name of volunteer to update")

def delete():
    user = input('''Do you want to choose a volunteer or delete by name:
                 1. Choose
                 2. I know name
                 ''').strip()
    if int(user) == 1:
        query = 'select id, name from volunteer'
        result = select(query)
        for row in result:
            print(f"{row['id']}. {row['name']}")
    else:
        name = "%"
        name += input("Type a name: ").strip()
        query = "select id from volunteer where name ilike %s"
        name += "%"
        result = select(query, [name])
        pretty_print(result)

def car_question():
    car = input("Have a car (Y/N): ").strip().lower()
    if car == 'y':
        print("Which car do you have:")
        Car.get_all()
        v_car = input("Choose a car or type a new one: ").strip()
        if v_car.isdigit():
            pass
        else:
            Car.add()
    return {
        "has_car": car,
        "car": v_car
    }
    
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
    print("Which languages do you love:")
    Language.get_all()
    v_language = input("Choose an language or type a new one: ").strip()
    if v_language.isdigit():
        pass
    else:
        Language.add()
    return {
        "language": v_language
    }
    
def city_question():
    cities = City.get_all()
    print("Cities: ")
    for row in cities:
        s = f"{row['id']}. {row["name"]}"
        print(s)
    v_city = input("Choose city or write a new one: ").strip()
    if v_city.isdigit():
        return int(v_city)
    else:
        city = City(v_city)
        id = city.add()
        return id
    
def pretty_print(data) -> None:
    for row in data:
        print(dict(row))