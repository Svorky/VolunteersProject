from database import select, insert

class City:
    def __init__(self, name) -> None:
        self.name = name
    
    @classmethod
    def get_all(self):
        query = "select id, name from city"
        result = select(query)
        return result
    
    def add(self):
        query = 'insert into city (name) values (%s)'
        id = insert(query, [self.name])
        return id
    
    def select(name):
        query = "select id, name from city where name = %s"
        result = select(query, [name])
        return result
    
    @classmethod
    def city_question(self):
        cities = self.get_all()
        print("Cities: ")
        for [idx,row] in enumerate(cities):
            s = f"{idx+1}. {row["name"]}"
            print(s)
        v_city = input("Choose city or write a new one: ").strip()
        if v_city.isdigit():
            return cities[int(v_city)-1]['id']
        else:
            city = City(v_city)
            id = city.add()
            return id