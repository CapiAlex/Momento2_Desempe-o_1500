class Payroll:

    def __init__(self):
        self.employees = {}
        self.minimum_salary = 1000000  # 2 minimum wages
        self.transportation_allowance = 106454  # Value of transportation allowance

    def register_employee(self, id, name, last_name, position, department, salary):
        self.employees[id] = {
            "name": name,
            "last_name": last_name,
            "position": position,
            "department": department,
            "salary": salary
        }
        print("Employee registered successfully.")

    def list_employees(self):
        return self.employees

    def calculate_net_salary(self, employee_id):
        employee = self.employees.get(employee_id)
        if not employee:
            return "Employee not found."

        salary = employee["salary"]
        net_salary = salary + (self.transportation_allowance if salary < 2 * self.minimum_salary else 0)
        return net_salary

    def print_payslip(self, employee_id):
        employee = self.employees.get(employee_id)
        if employee:
            net_salary = self.calculate_net_salary(employee_id)

            print("Payslip for the employee:")
            print(f"ID: {employee_id}")
            print(f"Name: {employee['name']} {employee['last_name']}")
            print(f"Position: {employee['position']}")
            print(f"Department: {employee['department']}")
            print(f"Gross Salary: {employee['salary']}")
            print(f"Net Salary: {net_salary}")
        else:
            print("Employee not found.")

    def sum_payroll(self):
        total_payroll = sum(self.calculate_net_salary(employee_id) for employee_id in self.employees)
        return total_payroll


if __name__ == "__main__":
    payroll = Payroll()

    while True:
        print("\nMAIN MENU:")
        print("1. Human Resources Analyst")
        print("2. Employee")
        print("3. Sum Total Payroll")
        print("4. Exit")

        main_menu_option = input("Select an option: ")

        if main_menu_option == "1":
            while True:
                print("\nHUMAN RESOURCES ANALYST MENU:")
                print("1. Register Employee")
                print("2. List Employees")
                print("3. Search Payslip")
                print("4. Search Employee")
                print("5. Exit")

                analyst_menu_option = input("Select an option: ")

                if analyst_menu_option == "1":
                    id = int(input("Employee ID: "))
                    name = input("Name: ")
                    last_name = input("Last Name: ")
                    position = input("Position: ")
                    department = input("Department: ")
                    salary = float(input("Salary: "))
                    payroll.register_employee(id, name, last_name, position, department, salary)

                elif analyst_menu_option == "2":
                    employees = payroll.list_employees()
                    for employee_id, employee_info in employees.items():
                        print(f"ID: {employee_id}, Name: {employee_info['name']} {employee_info['last_name']}")

                elif analyst_menu_option == "3":
                    employee_id = int(input("Employee ID: "))
                    payroll.print_payslip(employee_id)

                elif analyst_menu_option == "4":
                    employee_id = int(input("Employee ID: "))
                    if employee_id in payroll.employees:
                        print(
                            f"Employee found: {payroll.employees[employee_id]['name']} {payroll.employees[employee_id]['last_name']}")
                    else:
                        print("Employee not found.")

                elif analyst_menu_option == "5":
                    break

        elif main_menu_option == "2":
            while True:
                print("\nEMPLOYEE MENU:")
                print("1. Search and Print Payslip")
                print("2. Exit")

                employee_menu_option = input("Select an option: ")

                if employee_menu_option == "1":
                    employee_id = int(input("Employee ID: "))
                    payroll.print_payslip(employee_id)

                elif employee_menu_option == "2":
                    break

        elif main_menu_option == "3":
            total_payroll = payroll.sum_payroll()
            print(f"Total Payroll: {total_payroll}")

        elif main_menu_option == "4":
            break
