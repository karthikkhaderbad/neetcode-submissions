from typing import List

def read_integers() -> List[int]:
    numbers = input()
    numbers_list = numbers.split(",")
    numbers_list_int = []
    for number in numbers_list :
        numbers_list_int.append(int(number))
    return numbers_list_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
