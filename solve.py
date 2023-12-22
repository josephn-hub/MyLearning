numbers = [1, 3, 5, 6, 11, 23]
sum = 9
b = []


# def check_numbers(numbers, sum=9):

for i, number in enumerate(numbers):
      complementary = sum - numbers[i]
      if complementary in numbers[i+1:]:
          print(f"checking number are: {complementary}, {number}")



# result_check = check_numbers(numbers)

# print(result_check)