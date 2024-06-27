from database import select, insert

class VolunteerCar:
    def __init__(self) -> None:
        pass
    
    table_name = 'volunteer_car'
    @classmethod
    def create(self, vol, lan):
        query = f"insert into {self.table_name} (volunteer_id, car_id) values (%s, %s)"
        params = [vol, lan]
        insert(query, params, False)