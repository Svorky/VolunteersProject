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