def sorting_cheeses(**kwargs):
    result = ''


    sorted_items = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in sorted_items:

        result += f"{tuple_[0]}\n"
        sorted_product = sorted(tuple_[1], reverse=True)
        for product in sorted_product:
            result += f"{product}\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
