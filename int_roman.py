def int_to_roman(num):
    if not 1 <= num <= 3999:
        raise ValueError("Number must be between 1 and 3999")

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman = ""
    for i in range(len(val)):
        while num >= val[i]:
            roman += syms[i]
            num -= val[i]

    return roman


# Take user input
try:
    number = int(input("Enter a number (1–3999): "))
    print("Roman numeral:", int_to_roman(number))
except ValueError as e:
    print("Error:", e)
