"""
a set of functions to convert numeric values 
from one set of units to another
"""


# usful constants
KPM = 1.609344 # Kilometers per mile
GPL = 0.2641720524 # gallons per liter

def mpg2kpl(mpg, percision = 4):
    """
    conversts mpg to kpl percisely to the specifed
    number decimal places (defaults to 4)
    """
    return round(mpg * KPM * GPL, percision)