from database import select, insert


class Animal:
    def __init__(self) -> None:
        self.id = None
        self.name = ""

    @classmethod
    def get_all(self):
        query = "select id, name from animal"
        result = select(query)
        return result

    def add(self):
        query = 'insert into animal (name) values (%s)'
        id = insert(query, [self.name])
        return id

    def select(name):
        query = "select id, name from animal where name = %s"
        result = select(query, [name])
        return result

    def question(self):
        u_animal = input("Can you feed animal (Y/N): ").strip().lower()
        if u_animal == 'y':
            print("What animal do you prefer to feed:")
            animals = self.get_all()
            for [idx, row] in enumerate(animals):
                s = f"{idx+1}. {row["name"]}"
                print(s)
            v_animal = input("Choose an animal or type a new one: ").strip()
            if v_animal.isdigit():
                # return animals[int(v_animal)-1]['id']
                self.id = animals[int(v_animal)-1]['id']
                return True
            else:
                self.name = v_animal
                id = self.add()
                self.id = id
                return True
        elif u_animal == 'n':
            return False
        else:
            return None
