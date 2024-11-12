# My Solution
def getRomanUnits(num_units, roman_base_unit, roman_five, roman_ten):
    roman_units = ""
    if num_units > 0:
        if num_units == 9:
            roman_units += roman_base_unit + roman_five
        elif num_units == 4:
            roman_units += roman_base_unit + roman_ten
        elif num_units >= 5:
            roman_units += roman_ten
            for i in range(num_units - 5):
                roman_units += roman_base_unit
        else:
            for i in range(num_units):
                roman_units += roman_base_unit
    return roman_units

def intToRoman(num):
    roman = ""
    thousands = num // 1000 % 10
    hundreds = num // 100 % 10
    tens = (num // 10) % 10
    ones = num % 10
    roman += getRomanUnits(thousands, "M", "", "")
    roman += getRomanUnits(hundreds,"C", "M", "D")
    roman += getRomanUnits(tens,"X", "С", "L")
    roman += getRomanUnits(ones,"I", "X", "V")
    return roman


def intToRoman2(num):
    roman_numerals = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]
    res = ""
    for roman, integer in roman_numerals:
        new_roman = num // integer
        num = num % integer
        for i in range(new_roman):
            res += str(roman)
    return res
print(intToRoman2(486))
