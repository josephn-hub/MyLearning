import os


def user_input(add_details):
    result = add_details("Hope everything is good")
    print(result)


def add_info(str_pass):
    return str_pass.upper()


user_input(add_info)


string_name = [
    {"last_name": "kiran",
     "first_name": "joseph",
     "sur_name": "kambham"
     }
]
print(enumerate(string_name[0].items()))
# use_join = ',' . join([value for name, value in enumerate(string_name[0].items())])

# print(use_join)

# file = os.makedirs("/Users/josephkambham/new_folder", exist_ok= True)

# with open(file, "r") as f:
#     content = f.read()
#     print(content)
