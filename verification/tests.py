"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""
from random import randint, sample
from my_solution import triangular_islands


def make_random_tests(*num):
    random_tests = []
    for triangle_max in num:
        input_num = sample(range(1, triangle_max + 1), randint(1, triangle_max))
        random_tests.append({
            "input": input_num,
            "answer": sorted(triangular_islands(input_num)),
        })
    return random_tests


TESTS = {
    "Basics": [
        {
            "input": [1],
            "answer": [1],
        },
        {
            "input": [2, 3, 6],
            "answer": [3],
        },
        {
            "input": [4, 3],
            "answer": [2],
        },
        {
            "input": [1, 4, 7, 8],
            "answer": [1, 3],
        },
        {
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "answer": [9],
        },
        {
            "input": [1, 2, 4, 5, 7, 9],
            "answer": [1, 1, 1, 1, 1, 1],
        },
    ],
    "Extra": [
        {
            "input": [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 24, 25],
            "answer": [18],
        },
        {
            "input": list(
                set(range(1, 101)) - {17, 27, 28, 40, 41, 55, 56, 57, 58, 59, 60, 76, 77,
                                      95, 96, 49, 63, 62, 78, 16, 24, 23, 33, 32, 44, 43}),
            "answer": [8, 9, 24, 33],
        },
    ],
    "Randoms": make_random_tests(9, 9, 9, 16, 25, 36, 49, 64, 81, 100, 100, 100, 100),
}
