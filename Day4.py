def parse_numbers(lines):
    result = []

    for line in lines:
        numbers = line.split(":")[1].split("|")
        winning_numbers = clean_numbers(numbers[0])
        scratched_numbers = clean_numbers(numbers[1])
        result.append([winning_numbers, scratched_numbers])

    return result


def clean_numbers(numbers):
    numbers = numbers.split(" ")
    numbers = [number for number in numbers if not number == ""]
    numbers = [int(number) for number in numbers]

    return numbers


def part1(lines):
    cards = parse_numbers(lines)
    total = 0

    for card in cards:
        count = 0
        for number in card[1]:
            if number in card[0]:
                count += 1
        score = pow(2, count-1)

        total += score

    return total


def part2(lines):
    cards = parse_numbers(lines)
    cards_count = {}
    for i in range(0, len(cards)):
        cards_count[str(i)] = 1

    for i, card in enumerate(cards):
        number_count = 0
        for number in card[1]:
            if number in card[0]:
                number_count += 1
        for b in range(0, number_count):
            cards_count[str(i + b + 1)] += cards_count[str(i)]

    return sum(cards_count.values())


if __name__ == '__main__':
    with open("day4.txt", "r") as f:
        content = f.readlines()

    print(part1(content))
    print(part2(content))
