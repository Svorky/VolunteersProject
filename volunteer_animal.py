from database import select, insert

class VolunteerAnimal:
    def __init__(self) -> None:
        pass
    
    table_name = 'volunteer_animal'
    @classmethod
    def create(self, vol, lan):
        query = f"insert into {self.table_name} (volunteer_id, animal_id) values (%s, %s)"
        params = [vol, lan]
        insert(query, params, False)