import asyncio
import pytest

from cover import (
    add,
    divide,
    factorial,
    is_even,
    max_of_two,
    multiply,
    subtract,
)


def test_add_returns_awaitable():
    result = asyncio.run(add(2, 3))

    try:
        assert asyncio.iscoroutine(result)
    finally:
        result.close()


def test_divide_and_divide_by_zero():
    assert asyncio.run(divide(6, 2)) == 3

    with pytest.raises(ZeroDivisionError, match="Делить на ноль нельзя"):
        asyncio.run(divide(6, 0))


# def test_subtract():
#     assert subtract(10, 4) == 6
#
#
# def test_multiply():
#     assert multiply(3, 4) == 12


# def test_is_even():
#     assert is_even(8) is True
#     assert is_even(7) is False


def test_max_of_two():
    assert max_of_two(10, 4) == 10
    assert max_of_two(4, 10) == 10


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120

    with pytest.raises(ValueError, match="Факториал определён"):
        factorial(-1)
