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
# unit-test: it focuses on the functionality of a single method; solidify behavior against your API
# regression test: ensures that your code doesn't break; running all your aggregate code
# tdd (test-driven-development): you write or create a test before writing a single line of code. Basically what do you expect your code to do.
# test coverage: when you write a unit test you're ensuring a certain aspect of code
# load, stress,
# functional testing:


# Get Ed a fucking brew Immediately!
WEEKS_IN_YEAR = 52


class CommissionCalculator:
    """average contract value x salesperson commission (percentages) = gross commission + base-salary - deductions = net pay"""

    def __init__(self, ACV, annual_salary, effective_tax_rate, sales_commission_percentage):
        self.ACV = float(ACV)
        self.annual_salary = float(annual_salary)
        self.effective_tax_rate = float(effective_tax_rate)
        self.sales_commission_percentage = float(sales_commission_percentage)

        # def ACV(self):

    #     return 25_000
    # def sales_commission_percentage(self):
    #     return .10
    def gross_commission(self):
        """calculates the gross commission for your sales...gross/yuk"""
        return self.ACV * self.sales_commission_percentage

    def biweekly_base_salary(self):
        return self.weekly_base_salary() * 2

    def weekly_base_salary(self):
        return self.annual_salary / WEEKS_IN_YEAR

    # 52 is a variable so we need to make it a constant and define it as weeks
    # Constants usually have all CAPS
    # Uncle Bob "Best Practice Guru": Refactor until you drop which means you want to
    # simplify lengthy methods - best practice to refactor towards improvement
    # DRY "Don't Repeat Yourself"

    # def annual_salary(self):
    #     return 100_000

    # def deductions(self):
    #     return .65

    def annual_net_pay(self):
        return (self.gross_commission() + self.annual_salary) * (1 - self.effective_tax_rate)

    def biweekly_net_pay(self):
        return (self.gross_commission()/WEEKS_IN_YEAR * 2 + self.biweekly_base_salary()) * (1- self.effective_tax_rate)
# Steve gets Costso pizza and a beer without the executive card = Dan must pay in full

if __name__ == '__main__':
    # Ed's getting a shot and a better for that double "M"
    user_ACV = input("enter your annual contract value: ")
    user_annual_salary = input("enter your annual salary: ")
    user_deductions = input("enter your deductions: ")
    user_sales_commission_percentage = input("enter your sales commission percentage: ")
    commission_calculator1 = CommissionCalculator(ACV=user_ACV,
                                                  annual_salary=user_annual_salary,
                                                  effective_tax_rate=user_deductions,
                                                  sales_commission_percentage=user_sales_commission_percentage)
    # instantiating means creating an instance of the class
    print(f"your paycheck is ${commission_calculator1.biweekly_net_pay():.2f}")
    print(f"your annual paycheck is ${commission_calculator1.annual_net_pay():.2f}")
