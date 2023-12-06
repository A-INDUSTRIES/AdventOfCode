from math import sqrt, floor, ceil


def parser(file_content):
    times = [float(time) for time in file_content.split("\n")[0].split(":")[1].split(" ") if time != ""]
    distances = [float(dist) for dist in file_content.split("\n")[1].split(":")[1].split(" ") if dist != ""]
    return times, distances


def calc(times, distances):
    result = 1
    for i in range(0, len(times)):
        start = 0.5 * - times[i] - 0.5 * sqrt(pow(times[i], 2) - 4 * distances[i])
        end = 0.5 * - times[i] + 0.5 * sqrt(pow(times[i], 2) - 4 * distances[i])
        start = floor(start)
        end = ceil(end)
        count = end - start - 1
        result *= round(count)
    return result


def part1(file_content):
    times, distances = parser(file_content)
    return calc(times, distances)


def part2(file_content):
    times, distances = parser(file_content)
    time = [float("".join([str(int(num)) for num in times]))]
    distance = [float("".join([str(int(num)) for num in distances]))]
    return calc(time, distance)


if __name__ == "__main__":
    with open("day6.txt", "r") as f:
        content = f.read()
    print(part1(content))
    print(part2(content))
