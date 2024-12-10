from enum import Enum

Direction = Enum("Direction", ["NORTH", "EAST", "SOUTH", "WEST"])


class MapPoint:
    def __init__(self: "MapPoint", value: int) -> None:
        self._value = value
        self._neighbors = {}
        for direction in Direction:
            self._neighbors[direction] = None

    def get_value(self: "MapPoint") -> int:
        return self._value

    def set_neighbor(self: "MapPoint", direction: Direction, neighbor: "MapPoint" or None) -> None:
        self._neighbors[direction] = neighbor

    def get_neighbor(self: "MapPoint", direction: Direction) -> "MapPoint" or None:
        return self._neighbors[direction]

    def calculate_valid_path(self: "MapPoint", reached_nines=None) -> set:
        if reached_nines is None:
            reached_nines = set()

        if self._value == 9:
            reached_nines.add(self)
            return reached_nines

        for neighbor in self._neighbors.values():
            if neighbor is not None and neighbor.get_value() == self._value + 1:
                neighbor.calculate_valid_path(reached_nines)

        return reached_nines
