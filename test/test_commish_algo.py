# unittest, pytest, nose are the most common unit testing libraries
# you want to create a simulation or trigger event - calling the function.
# set a state, set multiple actions and multiples validations
# instantiate a class means attributring values in the objects. certain values that are defined; classes are blueprints and instantiates (values) are the house
from unittest import TestCase

from commish_algo import CommissionCalculator


# Ed gets three cocktails and mocktails from Danny
class TestCommissionCalculator(TestCase):
    def test_gross_commission(self):
        # Given
        user_ACV = 10_000
        user_annual_salary = 100_000
        user_deductions = 5_000
        user_sales_commission_percentage = .10

        # We owe Steve a beer
        commission_calculator1 = CommissionCalculator(ACV=user_ACV,
                                                      annual_salary=user_annual_salary,
                                                      deductions=user_deductions,
                                                      sales_commission_percentage=user_sales_commission_percentage)
        # When
        march_commish = commission_calculator1.gross_commission()
        # Then
        self.assertEqual(1000, march_commish)
