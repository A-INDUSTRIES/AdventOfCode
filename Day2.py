MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

colors = ["red", "green", "blue"]


def parse_values(line):
    split = line.split(":")
    game_id = int(split[0].split(" ")[-1])
    games = [game.split(",") for game in split[1].split(";")]
    final_games = [{"red": 0, "green": 0, "blue": 0} for _ in games]
    for i, game in enumerate(games):
        for sub in game:
            for color in colors:
                if color in sub:
                    final_games[i][color] = int(sub.split(" ")[1])
    result = {"red": [], "green": [], "blue": []}
    maximums = {}
    for game in final_games:
        result["red"].append(game["red"])
        result["blue"].append(game["blue"])
        result["green"].append(game["green"])
    for i, val in iter(result.items()):
        match i:
            case "red":
                maximums[colors[0]] = max(val)
            case "green":
                maximums[colors[1]] = max(val)
            case "blue":
                maximums[colors[2]] = max(val)
    return game_id, final_games, maximums


def part_one(lines):
    s = 0
    for line in lines:
        game_id, final_games, maximums = parse_values(line)
        if all([maximums["red"] <= MAX_RED, maximums["green"] <= MAX_GREEN, maximums["blue"] <= MAX_BLUE]):
            s += game_id
    return s


def part_two(lines):
    s = 0
    for line in lines:
        game_id, final_games, maximums = parse_values(line)
        power = 0
        for i in maximums.values():
            if power == 0:
                power = i
            else:
                power *= i
        s += power
    return s


if __name__ == "__main__":
    with open("day2.txt", "r") as f:
        content = f.readlines()
    print("Part one:", part_one(content))
    print("Part two:", part_two(content))
