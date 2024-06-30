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
    
    @classmethod
    def language_question(self):
        print("Which languages do volunteer speaks:")
        languages = self.get_all()
        for [idx,row] in enumerate(languages):
            s = f"{idx+1}. {row["name"]}"
            print(s)
        v_language = input("Choose an language or type a new one: ").strip()
        if v_language.isdigit():
            return languages[int(v_language)-1]['id']
        else:
            language = Language(v_language)
            id = language.add()
            return id