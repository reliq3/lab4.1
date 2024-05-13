def digit_sum(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum


def max_digit_sum_number(numbers):
    max_sum = 0
    max_number = None
    for number in numbers:
        sum = digit_sum(number)
        if sum > max_sum:
            max_sum = sum
            max_number = number
    return max_number
