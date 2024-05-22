try:
    name_dict = {"joseph": 30, "Jay": 30, "christy": 4}
    picked_name = name_dict["queeny"]
    print(f"Picked name is {picked_name}")
except KeyError as e:
    print(f"Error:{e}")

