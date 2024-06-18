vehicles = ["car","van","truck","lorry"]

for row_id, vehicle in enumerate(vehicles, start=100):
    print(f"Vehicle list with {row_id} {vehicle} \t ")



fruits = {"apple", "orange", "banana"}
quantity = {5,6,7}

for fruit, quantity in zip(fruits, quantity):
    print(f"fruits quantity: {fruit}:{quantity}")


