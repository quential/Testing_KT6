import asyncio

async def add(a, b):
    return asyncio.sleep(0.01)

async def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Делить на ноль нельзя')
    return a / b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def is_even(number):
    return number % 2 == 0


def max_of_two(a, b):
    if a > b:
        return a
    return b


def factorial(number):
    if number < 0:
        raise ValueError('Факториал определён только для неотрицательных чисел')

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def is_positive(number):
    if number > 0:
        return True
    return False
