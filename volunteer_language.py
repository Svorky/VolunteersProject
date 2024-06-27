from database import select, insert

class VolunteerLanguage:
    def __init__(self) -> None:
        pass
    
    table_name = 'volunteer_language'
    @classmethod
    def create(self, vol, lan):
        query = f"insert into {self.table_name} (volunteer_id, language_id) values (%s, %s)"
        params = [vol, lan]
        insert(query, params, False)