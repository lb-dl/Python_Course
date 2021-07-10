"""
Task 7_2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.

Create basic class Employee and declare following content:
• Attributes – `name` (str), `salary` and `bonus` (int), set with property decorator
• Constructor - parameters `name` and `salary`
• Method `bonus` - sets bonuses to salary, amount of which is delegated as `bonus`
• Method `to_pay` - returns the value of summarized salary and bonus.

Create class SalesPerson as class Employee inheritor and declare within it:
• Constructor with parameters: `name`, `salary`, `percent` – percent of plan performance (int, without the % symbol), first two of which are passed from basic class constructor
• Redefine method of parent class `bonus` in the following way: if the sales person completed the plan more than 100%, their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3)

Create class Manager as Employee class inheritor, and declare within it:
• Constructor with parameters: `name`, `salary` and `client_number` (int, number of served clients), first two of which are passed to basic class constructor.
• Redefine method of parent class `bonus` in the following way: if the manager served over 100 clients, their bonus is increased by 500, and if more than 150 clients – by 1000.

Create class Company and declare within it:
• Constructor with parameters: `employees` – list of company`s employees (made up of Employee/SalesPerson/Manager classes instances) with arbitrary length `n`
• Method `give_everybody_bonus` with parameter company_bonus (int) that sets the amount of basic bonus for each employee.
• Method `total_to_pay` that returns total amount of salary of all employees including awarded bonus
• Method `name_max_salary` that returns name of the employee, who received maximum salary including bonus.

Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within `return`
"""


class Employee:
    def __init__(self, name,  salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._bonus = value

    def to_pay(self):

        return self.salary + self._bonus



class SalesPerson(Employee):
    def __init__(self, name, salary, percent):
        super().__init__(self, name, salary)
        self.percent = percent

    def bonus(self):
        if 100 < self.percent < 200:
            self._bonus *= 2
        elif self.percent > 200:
            self._bonus *= 3
        return self._bonus


class Manager(Employee):
    def __init__(self, name, salary, client_number):
        super().__init__(self, name, salary)
        self.client_number = client_number

    def bonus(self):
        if 100 < self.client_number < 150:
            self._bonus += 500
        elif self.client_number > 150:
            self.bonus += 1000
        return self.bonus


class Company:

    def give_everybody_bonus(self, employees, company_bonus):
        for employee in employees:
            employee.bonus = company_bonus


    def total_to_pay(self, employees):
        total_salary = 0
        for employee in employees:
            total_salary += employee.salary + employee.bonus()
        return total_salary

    def name_max_salary(self, employees):
        max_salary = 0
        name = ''
        for employee in employees:
            salary = employee.salary + employee.bonus()
            if salary > max_salary:
                max_salary = salary
                name = employee.name

        return name
