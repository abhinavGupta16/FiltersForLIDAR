class RangeFilter:
    def __init__(self):
        self._min_range = 0.03
        self._max_range = 50

    def update(self, measurements):
        """
        Runs the RangeFilter to update the measurements
        :param measurements: List of float (List of measurements read by LIDAR)
        :return: NA
        """
        for i in range(len(measurements)):
            if measurements[i] < self._min_range:
                measurements[i] = self._min_range
            elif measurements[i] > self._max_range:
                measurements[i] = self._max_range

    def change_range(self, min_range, max_range):
        """
        Change the range of allowed upper and lower limit in measurements
        :param min_range: int (lower bound)
        :param max_range: int (Upper bound)
        :return:
        """
        self._min_range = min_range
        self._max_range = max_range
