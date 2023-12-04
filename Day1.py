with open("day1.txt", "r") as f:
    lines = f.readlines()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

line_values = []

for line in lines:
    value = first = last = "0"
    for i in range(0, len(line)):
        if first == "0":
            for b, num in enumerate(numbers):
                if num in line[0:i + 1]:
                    first = str(b + 1)
            if line[i].isdigit():
                first = line[i]

        if last == "0":
            for b, num in enumerate(numbers):
                if num in line[-i - 1:-1]:
                    last = str(b + 1)
            if line[-i - 1].isdigit():
                last = line[-i - 1]

        value = first + last
    line_values.append(value)

line_values = [int(value) for value in line_values]
answer = sum(line_values)

print(answer)
