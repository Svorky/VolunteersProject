from database import select, insert
from helpers import print_rows, pretty_print
from language import Language
from car import Car
from animal import Animal
from city import City


class Find:
    def __init__(self) -> None:
        pass

    @classmethod
    def by_name(self):
        vol = '%'
        vol += input("Type a name or a part of name: ")
        vol += '%'
        query = '''
        SELECT
	volunteer.name AS volunteer,
	city.name AS city,
	volunteer.telephone,
	language.name AS language,
	animal.name AS animal,
	car.name AS car
FROM
	city
	INNER JOIN volunteer
	 ON city.id = volunteer.city_id
	LEFT OUTER JOIN volunteer_animal
	 ON volunteer.id = volunteer_animal.volunteer_id
	LEFT OUTER JOIN volunteer_car
	 ON volunteer.id = volunteer_car.volunteer_id
	LEFT OUTER JOIN volunteer_language
	 ON volunteer.id = volunteer_language.volunteer_id
	LEFT OUTER JOIN language
	 ON volunteer_language.language_id = language.id
	LEFT OUTER JOIN car
	 ON volunteer_car.car_id = car.id
	LEFT OUTER JOIN animal
	 ON volunteer_animal.animal_id = animal.id
WHERE
	volunteer.name ILIKE %s
        '''
        data = select(query, [vol])
        pretty_print(data)
        # choise = input("Type a number: ").strip()
        # v = data[int(choise)-1]
        # pretty_print(v)
        input("Press Enter...")

    @classmethod
    def by_language(self):
        print("Choose language:")
        data = Language.get_all()
        print_rows(data)
        choise = input("Type a number: ").strip()
        lan_id = data[int(choise)-1]["id"]
        query = f'''
        SELECT
        volunteer.name AS volunteer,
        language.name AS language,
        city.name AS city,
        volunteer.telephone
FROM
        volunteer
        INNER JOIN volunteer_language
         ON volunteer.id = volunteer_language.volunteer_id
        INNER JOIN language
         ON volunteer_language.language_id = language.id
        INNER JOIN city
         ON volunteer.city_id = city.id
WHERE
        language.id = %s
        '''
        vols = select(query, [lan_id])
        pretty_print(vols)
        input("Press Enter to continue...")

    @classmethod
    def by_driving_licence(self):
        query = '''
        SELECT
	volunteer.name AS volunteer
FROM
	volunteer
WHERE
	volunteer.has_driver_licence = true
        '''
        vols = select(query)
        pretty_print(vols)
        input("Press Enter to continue...")

    @classmethod
    def by_car(self):
        query = '''
        SELECT
	volunteer.name AS volunteer,
	car.name AS car,
	city.name AS city,
	volunteer.telephone
FROM
	volunteer
	INNER JOIN city
	 ON volunteer.city_id = city.id
	INNER JOIN volunteer_car
	 ON volunteer.id = volunteer_car.volunteer_id
	INNER JOIN car
	 ON volunteer_car.car_id = car.id
        '''
        res = select(query)
        pretty_print(res)
        print()
        want_car = input("Do you want to choose a car? (Y/N) ").strip().lower()
        if want_car == 'y':
            print("Choose a car:")
            data = Car.get_all()
            print_rows(data)
            choise = input("Type a number: ").strip()
            car_id = data[int(choise)-1]["id"]
            query = '''
            SELECT
        volunteer.name AS volunteer,
        car.name AS car,
        city.name AS city,
        volunteer.telephone
    FROM
        volunteer
        INNER JOIN city
        ON volunteer.city_id = city.id
        INNER JOIN volunteer_car
        ON volunteer.id = volunteer_car.volunteer_id
        INNER JOIN car
        ON volunteer_car.car_id = car.id
    WHERE
        volunteer_car.car_id = %s
            '''
            vols = select(query, [car_id])
            if len(vols) == 0:
                print("There is no data.")
            else:
                pretty_print(vols)
            input("Press Enter to continue...")
        else:
            return None

    @classmethod
    def by_animal(self):
        query = '''
        SELECT
	volunteer.name AS volunteer,
	animal.name as animal,
	city.name as city,
	volunteer.telephone,
	volunteer.has_car
FROM
	volunteer
	INNER JOIN volunteer_animal
	 ON volunteer.id = volunteer_animal.volunteer_id
	INNER JOIN animal
	 ON volunteer_animal.animal_id = animal.id
	INNER JOIN city
	 ON volunteer.city_id = city.id
        '''
        res = select(query)
        pretty_print(res)
        print()
        want_animal = input("Do you want to choose an animal? (Y/N) ").strip().lower()
        if want_animal == 'y':
            print("Choose an animal:")
            data = Animal.get_all()
            print_rows(data)
            choise = input("Type a number: ").strip()
            animal_id = data[int(choise)-1]["id"]
            query += '''
    WHERE
        volunteer_animal.animal_id = %s
            '''
            vols = select(query, [animal_id])
            if len(vols) == 0:
                print("There is no data.")
            else:
                pretty_print(vols)
            input("Press Enter to continue...")
        else:
            return None

    @classmethod
    def by_city(self):
        print("Choose a car:")
        data = City.get_all()
        print_rows(data)
        choise = input("Type a number: ").strip()
        city_id = data[int(choise)-1]["id"]
        query = '''
        SELECT
	volunteer.name AS volunteer,
	city.name AS city,
	volunteer.telephone,
	language.name AS language,
	car.name AS car,
	animal.name AS animal
FROM
	city
	INNER JOIN volunteer
	 ON city.id = volunteer.city_id
	LEFT OUTER JOIN volunteer_car
	 ON volunteer.id = volunteer_car.volunteer_id
	LEFT OUTER JOIN volunteer_animal
	 ON volunteer.id = volunteer_animal.volunteer_id
	LEFT OUTER JOIN volunteer_language
	 ON volunteer.id = volunteer_language.volunteer_id
	LEFT OUTER JOIN language
	 ON volunteer_language.language_id = language.id
	LEFT OUTER JOIN animal
	 ON volunteer_animal.animal_id = animal.id
	LEFT OUTER JOIN car
	 ON volunteer_car.car_id = car.id
WHERE
	volunteer.city_id = %s
        '''
        vols = select(query, [city_id])
        if len(vols) == 0:
            print("There is no data.")
        else:
            pretty_print(vols)
        input("Press Enter to continue...")

# SELECT v.name as volunteer, l.name as language, car.name as car, city.name as city
# FROM volunteer v
# left join volunteer_language vl
# on v.id = vl.volunteer_id
# left join language l
# on vl.language_id = l.id
# left join volunteer_car vc
# on vc.volunteer_id = v.id
# left join car
# on vc.car_id = car.id
# left join city
# on city.id = v.city_id
