def add_two_numbers() -> int:
    numbers = input()
    numbers_list = numbers.split(",")
    sum = int(numbers_list[0]) + int(numbers_list[1])
    return sum

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
