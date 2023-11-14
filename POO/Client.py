from Person import Person
import random

class Client(Person):
    def __init__(self, id, name, last_name, email, password, admission_date):
        super().__init__(id, name, last_name, email, password)
        self._admission_date = admission_date

    @property
    def admission_date(self):
        return self._admission_date

    @admission_date.setter
    def admission_date(self, admission_date):
        self._admission_date = admission_date

    def register(self):
        super().register()
        self.admission_date = input("Enter the admission date: ")

    def view_record(self):
        super().view_record()
        print(f"Admission Date: {self.admission_date}")

    def schedule_appointment(self):
        print("Schedule Appointment:")
        available_dates = Client.generate_available_dates()
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
