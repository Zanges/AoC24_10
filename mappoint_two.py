from mappoint import MapPoint


class MapPointTwo(MapPoint):
    def __init__(self: "MapPointTwo", value: int) -> None:
        super().__init__(value)

    def calculate_valid_path(self: "MapPointTwo") -> int:
        # If the current point is 9, we have found a valid trail
        if self._value == 9:
            return 1

        trail_count = 0
        for neighbor in self._neighbors.values():
            if neighbor is not None and neighbor.get_value() == self._value + 1:
                trail_count += neighbor.calculate_valid_path()

        return trail_count