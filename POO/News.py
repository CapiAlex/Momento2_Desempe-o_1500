from Employee import Employee
from Client import Client


class News:
    @staticmethod
    def show_news(person):
        if isinstance(person, Employee):
            print("News for Employees:")
            print("1. Welcome to our team.")
            print("2. Employee meeting this week.")
        elif isinstance(person, Client):
            print("News for Clients:")
            print("1. Special discount for frequent clients.")
            print("2. New services available for you.")

        option = input("Select a news item (1/2): ")
        if option == "1":
            print("Thank you for choosing us!")
        elif option == "2":
            print("Don't miss the important meeting this week.")
        else:
            print("Invalid option.")
