from Business import Business
from News import News


def main_menu():
    print("Main Menu")
    print("1. Employee")
    print("2. Person")
    print("3. Client")
    print("4. Exit")

    while True:
        option = input("Select an option: ")

        if option == "1":
            employee = Business.register_employee()
            if employee is not None:
                employee_menu(employee)
        elif option == "2":
            person = Business.register_person()
            if person is not None:
                person_menu(person)
        elif option == "3":
            client = Business.register_client()
            if client is not None:
                client_menu(client)
        elif option == "4":
            print("Exiting the program")
            break
        else:
            print("Invalid option. Please select a valid option.")


def employee_menu(employee):
    while True:
        print("\nEmployee Menu")
        print("1. View record")
        print("2. Schedule work hours")
        print("3. Exit")
        option = input("Select an option: ")

        if option == "1":
            employee.view_record()
        elif option == "2":
            employee.schedule_work_hours()
        elif option == "3":
            print("Exiting the Employee menu")
            break


def person_menu(person):
    while True:
        print("\nPerson Menu")
        print("1. View record")
        print("2. News")
        print("3. Exit")
        option = input("Select an option: ")

        if option == "1":
            person.view_record()
        elif option == "2":
            News.show_news(person)
        elif option == "3":
            print("Exiting the Person menu")
            break


def client_menu(client):
    while True:
        print("\nClient Menu")
        print("1. View record")
        print("2. Schedule appointment")
        print("3. Exit")
        option = input("Select an option: ")

        if option == "1":
            client.view_record()
        elif option == "2":
            client.schedule_appointment()
        elif option == "3":
            print("Exiting the Client menu")
            break


if __name__ == "__main__":
    main_menu()
