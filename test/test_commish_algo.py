# unittest, pytest, nose are the most common unit testing libraries
# you want to create a simulation or trigger event - calling the function.
# set a state, set multiple actions and multiples validations
# instantiate a class means attributring values in the objects. certain values that are defined; classes are blueprints and instantiates (values) are the house
import unittest
from unittest import TestCase

from commish_algo import CommissionCalculator


# Ed gets three cocktails and mocktails from Danny
class TestCommissionCalculator(TestCase):
    def setUp(self) -> None:
        """setup and tear-down method will allow you to
        define instructions that will be executed before and after each test method"""
        self.user_ACV = 10_000
        self.user_annual_salary = 100_000
        self.user_effective_tax_rate = .33
        self.user_sales_commission_percentage = .10

    def test_gross_commission(self):
        # Given
        self.user_ACV = 10_000
        self.user_sales_commission_percentage = .10

        # We owe Steve a beer
        commission_calculator1 = CommissionCalculator(ACV=self.user_ACV,
                                                      annual_salary=self.user_annual_salary,
                                                      effective_tax_rate=self.user_effective_tax_rate,
                                                      sales_commission_percentage=self.user_sales_commission_percentage)
        # When
        march_commish = commission_calculator1.gross_commission()
        # Then
        self.assertEqual(1000, march_commish)

    # coverage means the only specific lines that are being tested - any line of code thats executed when a test is run

    def test_biweekly_base_salary(self):
        # Given
        self.user_annual_salary = 52_000

        commission_calculator1 = CommissionCalculator(ACV=self.user_ACV,
                                                      annual_salary=self.user_annual_salary,
                                                      effective_tax_rate=self.user_effective_tax_rate,
                                                      sales_commission_percentage=self.user_sales_commission_percentage)
        # When = action
        biweekly_base_salary = commission_calculator1.biweekly_base_salary()
        # Then = validation/outcome
        self.assertEqual(2000, biweekly_base_salary)

    def test_weekly_base_salary(self):
        # Given
        self.user_annual_salary = 52_000

        commission_calculator1 = CommissionCalculator(ACV=self.user_ACV,
                                                      annual_salary=self.user_annual_salary,
                                                      effective_tax_rate=self.user_effective_tax_rate,
                                                      sales_commission_percentage=self.user_sales_commission_percentage)
        # When = action
        weekly_base_salary = commission_calculator1.weekly_base_salary()
        # Then = validation/outcome
        self.assertEqual(1000, weekly_base_salary)

    def test_annual_net_pay(self):
        #Given
        self.user_ACV = 10_000
        self.user_annual_salary = 100_000
        self.user_effective_tax_rate = .2
        self.user_sales_commission_percentage = .10

        commission_calculator1 = CommissionCalculator(ACV=self.user_ACV,
                                                      annual_salary=self.user_annual_salary,
                                                      effective_tax_rate=self.user_effective_tax_rate,
                                                      sales_commission_percentage=self.user_sales_commission_percentage)
        # When
        actual = commission_calculator1.annual_net_pay()
        # Then
        self.assertEqual(80_800, actual)

    def test_biweekly_net_pay(self):
        self.user_ACV = 5_200
        self.user_annual_salary = 52_000
        self.user_effective_tax_rate = .2
        self.user_sales_commission_percentage = .10

        commission_calculator1 = CommissionCalculator(ACV=self.user_ACV,
                                                      annual_salary=self.user_annual_salary,
                                                      effective_tax_rate=self.user_effective_tax_rate,
                                                      sales_commission_percentage=self.user_sales_commission_percentage)
        # When
        actual = commission_calculator1.biweekly_net_pay()
        # Then
        self.assertEqual(1_616, actual)