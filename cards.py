def cardPlay(cards):
    numbers = []
    strings = []

    for check in cards:
        if type(check) == int:
            numbers.append(check)
        else:
            strings.append(check)
    
    order_number = []
    while numbers:
        sort_num = min(numbers)
        order_number.append(sort_num)
        numbers.remove(sort_num)
    
    order_number.extend(strings)
    return order_number



cards = [4, 2, 1, 4, 5, 'King', 6, 'Queen', 9, 7, 8, 'Jack']

main = cardPlay(cards)
print(main)