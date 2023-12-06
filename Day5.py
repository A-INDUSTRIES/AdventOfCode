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
    result = []
    for m in maps:
        for r in m:
            length = r[2]
            start = r[1]
            end = start + length
            offset = start - r[0]
            i = 0
            while i < len(seeds) - 1:
                s_start = seeds[i]
                s_end = seeds[i] + seeds[i + 1]
                s_length = seeds[i + 1]
                if s_start > end or s_end < start:
                    print("unchanged")
                    result.append(s_start)
                    result.append(s_length)
                elif s_start < start and s_end > end:
                    print("s bigger")
                    result.append(start - offset)
                    result.append(length)
                elif s_start > start and s_end < end:
                    print("s smaller")
                    result.append(s_start - offset)
                    result.append(s_length)
                elif s_start > start and s_end > end:
                    print("case 1")
                    result.append(s_start - offset)
                    result.append(end - s_start)
                    result.append(end - offset)
                    result.append(s_end - (end - offset))
                elif s_start < start and s_end < end:
                    print("case 2")
                    result.append(s_start)
                    result.append(start - s_start)
                    result.append(start - offset)
                    result.append((s_end - offset) - (start - offset))
                i += 2
            print(result)
            seeds = result
            result = []
    return seeds


if __name__ == '__main__':
    with open("day5.txt") as f:
        content = f.read()
    # print(part1(content))
    print(part2(content))
