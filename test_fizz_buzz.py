'''
## Challenge: FizzBuzz Variation

Write a function called `fizz_buzz_variation(n)` that takes an integer `n` as input and returns a list of strings
representing the numbers from 1 to `n`. However, for multiples of 3, return "Fizz" instead of the number,
for multiples of 5, return "Buzz", and for numbers that are multiples of both 3 and 5, return "FizzBuzz".
'''

def fizz_buzz_variation(n):
    output = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output.append('FizzBuzz')      
        elif i % 3 == 0:
            output.append('Fizz')
        elif i % 5 == 0:
            output.append('Buzz')
        else:
            output.append(str(i))
    return output

# Concise test cases with key checks
compact_tests = [
    (1, ['1']),
    (2, ['2']),
    (3, ['Fizz']),
    (4, ['4']),
    (5, ['Buzz']),
    (6, ['Fizz']),
    (7, ['7']),
    (8, ['8']),
    (9, ['Fizz']),
    (10, ['Buzz']),
    (12, ['Fizz']),
    (13, ['13']),
    (14, ['14']),
    (15, ['FizzBuzz']),
    (16, ['16']),
    (18, ['Fizz']),
    (20, ['Buzz']),
    (21, ['Fizz']),
    (23, ['23']),
    (25, ['Buzz']),
    (30, ['FizzBuzz']),
    (33, ['Fizz']),
    (35, ['Buzz']),
    (45, ['FizzBuzz']),
    (50, ['Buzz']),
    (60, ['FizzBuzz']),
    (75, ['FizzBuzz']),
    (90, ['FizzBuzz']),
    (100, ['Buzz']),
    (105, ['FizzBuzz'])
]

for i, (input_n, expected_values) in enumerate(compact_tests):
    try:
        result = fizz_buzz_variation(input_n)
        expected_last = expected_values[-1]
        assert result[-1] == expected_last, (
            f"Expected last element '{expected_last}' but got '{result[-1]}' for n={input_n}"
        )
        print(f"\033[92mTest case {i + 1} passed.\033[0m")
    except AssertionError as e:
        print(f"\033[91m{e}\033[0m")
