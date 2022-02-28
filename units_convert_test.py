"""
unit test for the units converter funcitons.
"""

# import the code to be tested
from units_converter import mpg2kpl

def describe_a_set_of_units_converters():  
    def that_can_convert_mpg_to_kpl():
        """
        test that the mpg2kpl function works as expected
        """
        assert mpg2kpl(25, 2) == 10.63
        assert mpg2kpl(40, 2) == 17.01


    def that_can_convert_mpg_to_kpl_to_2_decimal_places():
        """
        Allows the user to specify percision to 2 decimal places
        instead of 4. The 2nd parameter inidcates the percisioin.
        """
        assert mpg2kpl(25, 2) == 10.63
        assert mpg2kpl(40, 2) == 17.01