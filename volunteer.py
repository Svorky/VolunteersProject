from database import select, insert, delete
from typing import Self

class Volunteer:
    table_name = "volunteer"

    def __init__(self, args) -> None:
        self.id = args['id'] if 'id' in args else None
        self.name = args['name'] if 'name' in args else None
        self.birth_date = args['birth_date'] if 'birth_date' in args else None
        self.city_id = args['city_id'] if 'city_id' in args else None
        self.has_driver_licence = args['has_driver_licence'] if 'has_driver_licence' in args else None
        self.has_car = args['has_car'] if 'has_car' in args else None
        self.has_bussiness = args['has_bussiness'] if 'has_bussiness' in args else None
        self.telephone = args['telephone'] if 'telephone' in args else None
        self.love_animals = args["love_animals"] if 'love_animals' in args else None
    
    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def find_volunteer(self):
        pass
    
    @classmethod
    def convert_to_self(self, data):
        result_list = []
        for row in data:
            result_list.append(Volunteer(row))
        return result_list
#{", ".join(list(self.__dict__.keys()))}
    @classmethod
    def get_all(self) -> list[Self]:
        data = select(f"select * from {self.table_name}")
        return self.convert_to_self(data)

    def create(self) -> int:
        volunteer = self.__dict__
        keys = list(volunteer.keys())
        keys.remove('id')
        query = f'''
            insert into volunteer ({", ".join(keys)})
            values
            ({", ".join(["%s" for _ in volunteer.keys()])})
            '''
        id = insert(query, list(volunteer.values()))
        return id

    @classmethod
    def read(self, cols = [], clause = None, params = []):
        query = "select "
        if len(cols) == 0:
            query += ", ".join(list(self.__dict__.keys()))
        else:
            query += ", ".join(cols)
        query += f" from {self.table_name}"
        result = select(query, params)
        return self.convert_to_self(result)

    def delete(self):
        query = f"delete from {self.table_name} where id = %s"
        params = [self.id]
        delete(query, params)

    def get_car(self):
        query = '''
        select car.name
        from car
        where car.id = (
            select car_id
            from volunteer_car
            where volunteer_id = (
                select id
                from volunteer
                where name = %s
            )
        )
        '''
        