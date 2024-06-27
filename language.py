from database import select, insert

class Language:
    def __init__(self, name) -> None:
        self.name = name
    
    @classmethod
    def get_all(self):
        query = "select id, name from language"
        result = select(query)
        return result
    
    def add(self):
        query = 'insert into language (name) values (%s)'
        id = insert(query, [self.name])
        return id
    
    def select(name):
        query = "select id, name from language where name = %s"
        result = select(query, [name])
        return result