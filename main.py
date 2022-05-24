def roman_numerals(num):

    roman_map = {}

    roman_map[1] = "I"
    roman_map[5] = "V"
    roman_map[10] = "X"
    roman_map[50] = "L"
    roman_map[100] = "C"
    roman_map[500] = "D"
    roman_map[1000] = "M"

    roman_numeral_string = ""

    while num > 0:
        if num >= 1000:
            roman_numeral_string += roman_map[1000]
            num -= 1000
        if num >= 500 and num < 1000:
            roman_numeral_string += roman_map[500]
            num -= 500
        if num >= 100 and num < 500:
            roman_numeral_string += roman_map[100]
            num -= 100
        if num >= 50 and num < 100:
            roman_numeral_string += roman_map[50]
            num -= 50
        if num >= 10 and num < 50:
            roman_numeral_string += roman_map[10]
            num -= 10
        elif num >= 5 and num < 10:
            roman_numeral_string += roman_map[5]
            num -= 5
        elif num >= 1 and num < 5:
            roman_numeral_string += roman_map[1]
            num -= 1

    return roman_numeral_string


print(roman_numerals(2000))