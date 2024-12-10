from task1 import load
from mappoint_two import MapPointTwo
from mappoint import Direction


def create_topographical_map(data: list[str]) -> tuple[dict[tuple[int, int], MapPointTwo], list[tuple[int, int]]]:
    """
    Create a topographical map from the data.

    :param data: list of strings from the input file

    :return: a tuple containing the topographical map and the coordinates of the trail starts
    """
    topographical_map = {}
    trail_starts_coordinates = []
    for y, row in enumerate(data):
        for x, value in enumerate(row):
            topographical_map[(x, y)] = MapPointTwo(int(value))
            if value == "0":
                trail_starts_coordinates.append((x, y))
    return topographical_map, trail_starts_coordinates


def connect_neighbors(topographical_map: dict[tuple[int, int], MapPointTwo], width: int, height: int) -> None:
    """
    Connect the neighbors of the map points.

    :param topographical_map: the topographical map
    :param width: the width of the map
    :param height: the height of the map
    """
    for y in range(height):
        for x in range(width):
            current_point = topographical_map[(x, y)]
            if x > 0:
                current_point.set_neighbor(Direction.WEST, topographical_map[(x - 1, y)])
            if x < width - 1:
                current_point.set_neighbor(Direction.EAST, topographical_map[(x + 1, y)])
            if y > 0:
                current_point.set_neighbor(Direction.NORTH, topographical_map[(x, y - 1)])
            if y < height - 1:
                current_point.set_neighbor(Direction.SOUTH, topographical_map[(x, y + 1)])


def main():
    data = load("input.txt")
    height = len(data)
    width = len(data[0])
    topographical_map, trail_starts_coordinates = create_topographical_map(data)
    connect_neighbors(topographical_map, width, height)
    total_paths = 0
    for start in trail_starts_coordinates:
        total_paths += topographical_map[start].calculate_valid_path()
    print(total_paths)


if __name__ == "__main__":
    main()