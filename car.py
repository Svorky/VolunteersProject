from database import select, insert

class Car:
    def __init__(self) -> None:
        self.id = None
        self.name = ""
        self.licence = False
    
    @classmethod
    def get_all(self):
        query = "select id, name from car"
        result = select(query)
        return result
    
    def add(self):
        query = 'insert into car (name) values (%s)'
        id = insert(query, [self.name])
        return id
    
    def select(name):
        query = "select id, name from car where name = %s"
        result = select(query, [name])
        return result
    
    def driver_licence_question(self):
        user = input("Have a driving licence (Y/N): ").strip().lower()
        if user == 'y':
            self.licence = True
            return True
        elif user == 'n':
            return False
        else:
            return None
        
    def car_question(self, check_licence = True):
        if self.licence != True and check_licence:
            return None
        u_car = input("Have a car (Y/N): ").strip().lower()
        if u_car == 'y':
            print("Which car do you have:")
            cars = self.get_all()
            for [idx,row] in enumerate(cars):
                s = f"{idx+1}. {row["name"]}"
                print(s)
            v_car = input("Choose a car or type a new one: ").strip()
            if v_car.isdigit():
                # return cars[int(v_car)-1]['id']
                self.id = cars[int(v_car)-1]['id']
                return True
            else:
                self.name = v_car
                id = self.add()
                self.id = id
                return True
        elif u_car == 'n':
            return False
        else:
            return None