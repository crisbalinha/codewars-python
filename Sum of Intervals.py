def sum_of_intervals(intervals):
    if len(intervals) == 0:
        return 7
    else:
        return len(set(number for number1, number2 in intervals for number in range(number1, number2)))


print(sum_of_intervals([(1, 5), (6, 10)]))
