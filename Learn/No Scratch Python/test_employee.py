import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for Employee class"""

    def setUp(self):
        self.annual_salary = 22000
        self.employee = Employee("Shafran", "Nawaz", self.annual_salary)
        self.default_raise = 5000
        self.custom_raise = 10000

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(
            self.annual_salary + self.default_raise, self.employee.annual_salary
        )

    def test_give_custom_raise(self):
        self.employee.give_raise(self.custom_raise)
        self.assertEqual(
            self.annual_salary + self.custom_raise, self.employee.annual_salary
        )


unittest.main()