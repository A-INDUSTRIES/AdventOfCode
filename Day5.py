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
    results = result = []
    for m in maps:
        for r in m:
            length = r[2]
            start = r[1]
            end = start + length
            offset = start - r[0]
            for i in [i*2 for i in range(0, int(len(seeds) * 0.5 - 1))]:
                s_start = seeds[i]
                s_end = seeds[i] + seeds[i + 1]
                if s_end < start or s_start > end:
                    continue
                result.append(min(s_start, start))
                result.append(max(s_start, start) - 1)
                result.append(max(s_start, start) - offset)
                result.append(min(s_end, end) - offset)
                result.append(min(s_end, end) + 1)
                result.append(max(s_end, end))
                print(result)
    return results


if __name__ == '__main__':
    with open("day5.txt") as f:
        content = f.read()
    print(part1(content))
    print(part2(content))
