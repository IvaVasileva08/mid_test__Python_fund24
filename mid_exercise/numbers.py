numbers = list(map(int, input().split()))
average_sum = sum(numbers) / len(numbers) if numbers else 0
greather_numbers = [num for num in numbers if num > average_sum]
if greather_numbers:
    top_numbers = sorted(greather_numbers, reverse = True)[:5]
    print(' '.join(map(str, top_numbers)))
else:
    print('No')