from menu import *

def menu():
    while True:
        print("Select what you whant to do:")
        print('''
            1. Add a new volunteer.
            2. Show all volunteers.
            3. Find a volunteer.
            4. Update a volunteer.
            5. Delete a volunteer.
            6. Exit.
            ''')
        user = input("What you want to do? ").strip()
        if user == '':
            return None
        match int(user):
            case 1:
                add_volunteer()
            case 2:
                show_all()
                input("Press Enter...")
            case 3:
                find()
            case 4:
                update()
            case 5:
                delete()
            case 6:
                print("Bye bye.")
                break
            case _:
                print(f"There is no a key {user}")

def main():
    print('This program helps you to manage volunteers.')
    menu()

if __name__ == '__main__':
    main()