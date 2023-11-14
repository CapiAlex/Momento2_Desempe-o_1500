from Person import Person
import random

class Employee(Person):
    def __init__(self, id, name, last_name, email, password, salary, position):
        super().__init__(id, name, last_name, email, password)
        self._position = position
        self._salary = salary
        self._work_schedule = {}

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def register(self):
        super().register()
        self.position = input("Enter the Position: ")
        self.salary = float(input("Enter the Salary: "))

    def view_record(self):
        super().view_record()
        print(f"Position: {self.position} Salary: {self.salary}")

    def log_in(self):
        registered_email = input("Enter the registered email: ")
        registered_password = input("Enter the registered password: ")

        if registered_email == self.email and registered_password == self.password:
            print(f"Welcome {self._name}")
            return True
        else:
            print("Validate your credentials")
            return False

    def schedule_work_hours(self):
        print("Scheduling work hours...")

        # Days of the week
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        for day in weekdays:
            # Generate a random time for the day
            start_time = random.randint(8, 12)  # Example: From 8 AM to 12 PM
            end_time = start_time + random.randint(1, 4)  # Example: Duration of 1 to 4 hours

            # Add the schedule to the dictionary
            self._work_schedule[day] = f"{start_time}:00 AM - {end_time}:00 PM"

        print("Work schedule scheduled:")
        for day, schedule in self._work_schedule.items():
            print(f"{day}: {schedule}")

    def initiate_employee_business(self, log_in, view_record):
        init = log_in()

        while init:
            print("1: View user data 2: Schedule work hours 3: Exit")
            option = int(input("Select an option: "))

            if option == 1:
                print("View User Data")
                view_record()
            elif option == 2:
                self.schedule_work_hours()
            elif option == 3:
                print("Exit")
                init = False
            else:
                print("Select a correct option")
