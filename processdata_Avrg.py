def process_data(data):
    result = []
    for value in data:
        if value > 10:
            result.append(value * 2)
        else:
            result.append(value)
        if value < 0:  # This condition doesn't make sense here
            return None
    return result

def compute_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)
