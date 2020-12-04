import sys

def part1():
    expenses = {}
    with open("input.txt") as file:
        for line in file:
            expenses[int(line)] = int(line)

    for key in expenses.keys():
        other_number = 2020 % key
        if other_number in expenses.keys():
            print(other_number * key)

def part2():
    expenses = {}
    with open("input.txt") as file:
        for line in file:
            expenses[int(line)] = True

    for key in expenses.keys():
        other_number = 2020 % key
        if other_number in expenses.keys():
            expenses[key] = False
            expenses[other_number] = False
    left_over = {}
    for key, value in expenses.items():
        if value == True:
            left_over[key] = True
    year = 2020
    keys = list(left_over.keys())
    for first_value in keys:
        for second_value in keys:
            sum = first_value + second_value
            if sum < year and first_value != second_value:
                remainder = year % sum 
                if remainder in left_over.keys(): 
                    print("value:", first_value * second_value * remainder)