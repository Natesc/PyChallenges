import text_to_lst

stock_price_list = text_to_lst.to_lst()

def stock_prices(lst):
    lowest = min(lst)
    lowest_index = lst.index(min(lst))

    highest = max(lst)
    highest_index = lst.index(max(lst))

    while lowest_index > highest_index:
        lst.pop(highest_index)

        if len(lst) > 1:
            highest = max(lst)
            highest_index = lst.index(max(lst))
        else:
            break

    return 0 if lowest_index == lst.index(lst[-1])\
        else highest - lowest


print(stock_prices(stock_price_list))