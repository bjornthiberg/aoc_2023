def get_lines(file_path) -> list:
    """Reads a file and returns a list of lines."""
    with open(file_path) as file:
        return file.readlines()


def max_color(line: str) -> list:
    """Finds the maximum value of each color in the given line."""
    color_sets = line.split(";")
    color_map = {"red": 0, "green": 0, "blue": 0}

    for color_set in color_sets:
        for color_info in color_set.split(","):
            parts = color_info.split()
            num, color = int(parts[-2]), parts[-1]
            color_map[color] = max(color_map[color], num)

    return [color_map["red"], color_map["green"], color_map["blue"]]


def main(file_path: str) -> tuple:
    lines = get_lines(file_path)

    part1_answer = 0
    part2_answer = 0
    max_red, max_green, max_blue = 12, 13, 14

    for game_n, line in enumerate(lines):
        max_colors = max_color(line)
        if all(
            max_color <= limit
            for max_color, limit in zip(max_colors, [max_red, max_green, max_blue])
        ):
            part1_answer += game_n + 1
        part2_answer += max_colors[0] * max_colors[1] * max_colors[2]

    return part1_answer, part2_answer


if __name__ == "__main__":
    result = main("input2.txt")
    print(result)
