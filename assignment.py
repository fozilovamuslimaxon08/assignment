def classify(value):
    if value < 248:
        return "Below range"
    elif value <= 252 and value >= 248:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    average = total / count
    average_result = average
    return average_result

num_jars = int(input("Enter the number of jars: "))
total_volume= 0
below= 0
in_range= 0
above= 0
for i in range(num_jars):
    vol = int(input("Enter the jar volume: "))
    category = classify(vol)
    print(category)

    total_volume += vol

    if category == "Below range":
        below += 1
    elif category == "In range":
        in_range += 1
    else:
        above += 1
avg_volume = calculate_average(total_volume, num_jars)
print(f"Total volume: {total_volume} ml")
print(f"Average volume: {avg_volume} ml")
print(f"Below range: {below}")
print(f"In range: {in_range}")
print(f"Above range: {above}")