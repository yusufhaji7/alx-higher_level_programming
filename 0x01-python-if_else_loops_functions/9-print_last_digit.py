#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
        return -1 * (number % 10)
    else:
        return (number % 10)
