def parse_file(file_content):
    groups = file_content.split("\n\n")
    seeds = [int(number) for number in groups[0].split(":")[1].split(" ") if not number == ""]
    maps = [[[int(n) for n in number.split(" ")] for number in group.split("\n")[1:] if not number == ""] for group in groups[1:]]
    return seeds, maps


def part1(file_content):
    seeds, maps = parse_file(file_content)
    for i in range(0, len(seeds)):
        for m in maps:
            for r in m:
                if r[1] < seeds[i] < r[1] + r[2]:
                    seeds[i] -= (r[1] - r[0])
                    break
    return min(seeds)


def part2(file_content):
    seeds, maps = parse_file(file_content)
    results = []
    # ........
    #   ....
    # ,,....,,
    # //////////
    # ,,....,,//
    return results


if __name__ == '__main__':
    with open("day5.txt") as f:
        content = f.read()
    print(part1(content))
    print(part2(content))
