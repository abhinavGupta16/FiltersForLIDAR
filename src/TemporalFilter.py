from Exceptions import LengthTooLargeError, LengthTooSmallError

class TemporalFilter:
    def __init__(self):
        self.d = -1
        self._min = 0
        self._max = 1000
        self._prevMeasurements = []

    def __median(self, values):
        """
        Calculate median from a given list
        :param values: List of numbers
        :return: float (median value)
        """
        values = sorted(values)
        length = len(values)
        if length % 2 == 0:
            a = int(length / 2) - 1
            b = int(length / 2)
            return (values[a] + values[b]) / 2.0
        else:
            return values[int(length / 2)]

    def update(self, measurements):
        """
        Runs the Temporal Filter to update the measurements
        :param measurements: List of float (List of measurements read by LIDAR)
        :return: NA
        """
        if len(measurements) < self._min:
            LengthTooSmallError.msg = "Length of Measurements is less than min (" + str(self._min) + ') allowed\n'
            raise LengthTooSmallError

        if len(measurements) > self._max:
            LengthTooLargeError.msg = "Length of Measurements is greater than max (" + str(self._max) + ') allowed\n'
            raise LengthTooLargeError

        if len(self._prevMeasurements) > self.d:
            del self._prevMeasurements[0]

        self._prevMeasurements.append(measurements[:])
        values = []
        for i in range(len(measurements)):
            values.append(measurements[i])

            for j in range(len(self._prevMeasurements) - 1):
                if len(self._prevMeasurements[j]) > i:
                    values.append(self._prevMeasurements[j][i])

            measurements[i] = self.__median(values)
            del values[:]

    def change_range(self, min_range, max_range):
        """
        Change the range of allowed values in measurements
        :param min_range: int (lower bound)
        :param max_range: int (Upper bound)
        :return:
        """
        self._min = min_range
        self._max = max_range
