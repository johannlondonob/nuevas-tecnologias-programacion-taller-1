def print_odds_numbers(dictionary):
    odds_numbers = []
    for item in dictionary:
        if str(dictionary[item]).isalpha():
            pass
        elif int(dictionary[item]) % 2 == 0:
            odds_numbers.append(dictionary[item])

    print(odds_numbers)


print(print_odds_numbers({
    0: "oe",
    1: 1,
    2: 2,
    3: 3,
    4: [
        0,
        3,
        " ",
        2,
        5,
        "Hola, mundo",
        False
    ],
    5: True,
    6:
        {
            1: 1.6,
            2: 4.9,
            3: 5,
            4: 2,
            5: 7
        },
    7: 25,
    8: 39
}))
