def to_lst():
    numbers = []

    with open('stock_price_list', 'r') as file:
        for line in file:
            numbers.append(int(line[:-1]))

    return numbers