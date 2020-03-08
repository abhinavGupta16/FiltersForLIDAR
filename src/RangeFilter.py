class RangeFilter:
    def __init__(self):
        self._minRange = 0.03
        self._maxRange = 50

    def update(self, measurements):
        """
        Runs the RangeFilter to update the measurements
        :param measurements: List of float (List of measurements read by LIDAR)
        :return: NA
        """
        for i in range(len(measurements)):
            if measurements[i] < self._minRange:
                measurements[i] = self._minRange
            elif measurements[i] > self._maxRange:
                measurements[i] = self._maxRange