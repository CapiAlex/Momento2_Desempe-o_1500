from Employee import Employee
from Person import Person
from Client import Client
import random


class Business:
    @staticmethod
    def register_person():
        print("Person Registration:")
        type = input("Select the type (Employee/Client): ").lower()
        if type == "employee":
            return Business.register_employee()
        elif type == "client":
            return Business.register_client()
        else:
            print("Invalid type.")
            return None

    @staticmethod
    def register_employee():
        employee = Employee(None, None, None, None, None, None, None)
        employee.register()
        return employee

    @staticmethod
    def register_client():
        client = Client(None, None, None, None, None, None)
        client.register()
        return client

    @staticmethod
    def schedule_appointment():
        print("Schedule Appointment:")
        available_dates = Business.generate_available_dates()
        for i, date in enumerate(available_dates):
            print(f"{i + 1}. {date}")
        selection = int(input("Select a date (1-5): "))
        if 1 <= selection <= 5:
            selected_date = available_dates[selection - 1]
            print(f"You have scheduled an appointment for {selected_date}.")
            available_dates.remove(selected_date)
        else:
            print("Invalid selection.")

    @staticmethod
    def generate_available_dates():
        available_dates = []
        for _ in range(5):
            day = random.randint(1, 31)
            month = random.randint(1, 12)
            date = f"{day:02}/{month:02}"
            available_dates.append(date)
        return available_dates
