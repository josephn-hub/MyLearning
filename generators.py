def generating_squares(number):
    for x in range(number):
        yield x ** 2


squared_numbers = generating_squares(6000)
print(next(squared_numbers))
print(next(squared_numbers))
print(next(squared_numbers))

