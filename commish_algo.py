# what's the core problem we're solving?
# finding a simpler way to calculate one's commission in after-tax dollars
# how are we going to do that?
# how do we calculate commission today? ...
# average contract value x salesperson commission (percentages) = gross commission + base-salary - deductions = net pay

# class is a code template for creating objects, where objects have variables and behaviors associated with them
# in object-oriented programming, a class is an extensible program-code-template for creating objects, providing initial
# values for state (member variables) and implementations of behaviors (member functions / methods)
# object-oriented programming is a paradigm based on the concept of objects which consists of data and code, data in the
# form of fields and code in the form of procedures
# what are keyword arguments vs positional arguments? Keyword arguments have a default value

class CommmissionCalculator:
    """average contract value x salesperson commission (percentages) = gross commission + base-salary - deductions = net pay"""

    def __init__(self, ACV, annual_salary, deductions, sales_commission_percentage):
        self.ACV = float(ACV)
        self.annual_salary = float(annual_salary)
        self.deductions = 1 - float(deductions)
        self.sales_commission_percentage = float(sales_commission_percentage)

        # def ACV(self):

    #     return 25_000

    # def sales_commission_percentage(self):
    #     return .10

    def gross_commission(self):
        return self.ACV * self.sales_commission_percentage

    def biweekly_base_salary(self):
        return (self.annual_salary / 52) * 2

    # def annual_salary(self):
    #     return 100_000

    # def deductions(self):
    #     return .65

    def annual_net_pay(self):
        return self.gross_commission() + self.annual_salary * self.deductions

    def biweekly_net_pay(self):
        return self.gross_commission() + self.biweekly_base_salary() * self.deductions


user_ACV = input("enter your annual contract value: ")
user_annual_salary = input("enter your annual salary: ")
user_deductions = input("enter your deductions: ")
user_sales_commission_percentage = input("enter your sales commission percentage: ")
commission_calculator1 = CommmissionCalculator(ACV=user_ACV,
                                               annual_salary=user_annual_salary,
                                               deductions=user_deductions,
                                               sales_commission_percentage=user_sales_commission_percentage)
# instantiating means creating an instance of the class
print(f"your paycheck is ${commission_calculator1.biweekly_net_pay():.2f}")
print(f"your annual paycheck is ${commission_calculator1.annual_net_pay():.2f}")
