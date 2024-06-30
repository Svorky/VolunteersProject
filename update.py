from database import select, update, select_volunteer, insert, delete
from helpers import pretty_print
from city import City
from language import Language
from car import Car
from animal import Animal

class Update:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def name(self, row):
        print(f"Name of this volunteer is {row['volunteer_name']}")
        new_value = input("Type a new name: ").strip()
        update("volunteer", "name", 'id', [new_value, row['id']])
        print("Record was updated.")
        res = select_volunteer({"volunteer.id = %s":row['id']})
        pretty_print(res)
        
    @classmethod
    def birth_date(self, row):
        print(f"Birth date of this volunteer is {row['birth_date']}")
        new_value = input("Type a new birth date (dd/mm/yyyy): ").strip()
        update("volunteer", "birth_date", 'id', [new_value, row['id']])
        print("Record was updated.")
        res = select_volunteer({"volunteer.id = %s":row['id']})
        pretty_print(res)
        
    @classmethod
    def city(self, row):
        print(f"City of this volunteer is {row['city']}")
        city_id = City.city_question()
        update("volunteer", "city_id", 'id', [city_id, row['id']])
        print("Record was updated.")
        res = select_volunteer({"volunteer.id = %s":row['id']})
        pretty_print(res)
        
    @classmethod
    def telephone(self, row):
        print(f"Telephone of this volunteer is {row['telephone']}")
        new_value = input("Type a new telephone: ").strip()
        update("volunteer", "telephone", 'id', [new_value, row['id']])
        print("Record was updated.")
        res = select_volunteer({"volunteer.id = %s":row['id']})
        pretty_print(res)
        
    @classmethod
    def language(self, row):
        print(f"Telephone of this volunteer is {row['language']}")
        lan_id = Language.language_question()
        vl = select("select * from volunteer_language where volunteer_id = %s", [row['id']])
        if len(vl) == 0:
            query = "insert into volunteer_language (volunteer_id, language_id) values(%s, %s)"
            insert(query, [row['id'], lan_id], False)
        else:
            update("volunteer_language", "language_id", 'volunteer_id', [lan_id, row['id']])
        print("Record was updated.")
        res = select_volunteer({"volunteer.id = %s":row['id']})
        pretty_print(res)
    
    @classmethod
    def has_driver_licence(self,row):
        print(f"Status of driving licenece is {row['has_driving_licence']}")
        new_value = input("Type a new status (Y/N): ").strip()
        update("volunteer", "has_driver_licence", 'id', [new_value, row['id']])
        print("Record was updated.")
        res = select_volunteer({"volunteer.id = %s":row['id']})
        pretty_print(res)
    
    @classmethod
    def has_car(self,row):
        print(f"Car of this volunteer is {row['car']}")
        car = Car()
        has = car.car_question(check_licence = False)
        vl = select("select * from volunteer_car where volunteer_id = %s", [row['id']])
        if has and len(vl) == 0:
            query = "insert into volunteer_car (volunteer_id, car_id) values(%s, %s)"
            insert(query, [row['id'], car.id], False)
            update("volunteer", "has_car", "id", [has, row['id']])
        elif has:
            update("volunteer_car", "car_id", 'volunteer_id', [car.id, row['id']])
            update("volunteer", "has_car", "id", [has, row['id']])
        else:
            update("volunteer", "has_car", "id", [has, row['id']])
            delete("delete from volunteer_car where volunteer_id = %s", [row['id']])
        print("Record was updated.")
        res = select_volunteer({"volunteer.id = %s":row['id']})
        pretty_print(res)
        
    @classmethod
    def love_animals(self,row):
        if row['love_animals']:
            print(f"This volunteer loves animals and he/she loves {row['animal']}")
        else:
            print("This volunteer doesn't love animals now")
        animal = Animal()
        love = animal.question()
        vl = select("select * from volunteer_animal where volunteer_id = %s", [row['id']])
        if love and len(vl) == 0:
            query = "insert into volunteer_animal (volunteer_id, animal_id) values(%s, %s)"
            insert(query, [row['id'], animal.id], False)
            update("volunteer", "love_animals", "id", [love, row['id']])
        elif love:
            update("volunteer_animal", "animal_id", 'volunteer_id', [animal.id, row['id']])
            update("volunteer", "love_animals", "id", [love, row['id']])
        else:
            update("volunteer", "love_animals", "id", [love, row['id']])
            delete("delete from volunteer_animal where volunteer_id = %s", [row['id']])
        print("Record was updated.")
        res = select_volunteer({"volunteer.id = %s":row['id']})
        pretty_print(res)