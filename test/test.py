import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_right(self):
        assert self.calc.multiply(self, 5, 6) == 30

    def test_division_right(self):
        assert self.calc.division(self, 20, 4) == 5

    def test_subtraction_right(self):
        assert self.calc.subtraction(self, 7, 3) == 4

    def test_adding_right(self):
        assert self.calc.adding(self, 5, 5) == 10