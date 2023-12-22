available_units = {
    '201': {
        "beds": 2,
        "price": 1000,
        "house_type": "Terraced"

    },

    '301': {
        "beds": 3,
        "price": 1500,
        "house_type": "flat"
    }
}

for number in available_units:
    print(available_units[number]['beds'])

# removing duplicates in a list
list_items = ['a', 'b', 'c', 'a', 'd', 'b']

data = list(dict.fromkeys(list_items).keys())
print(data)
