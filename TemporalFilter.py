class TemporalFilter:
    def __init__(self):
        self.d = -1
        self._prevMeasurements = []

    def median(self, values):
        """
        Calculate median from a given list
        :param values: List of numbers
        :return: float (median value)
        """
        values = sorted(values)
        length = len(values)
        if length % 2 == 0:
            a = int(length / 2)-1
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
        if len(self._prevMeasurements) > self.d:
            del self._prevMeasurements[0]

        self._prevMeasurements.append(measurements[:])
        values = []
        for i in range(len(measurements)):
            values.append(measurements[i])

            for j in range(len(self._prevMeasurements)-1):
                if len(self._prevMeasurements[j]) > i :
                    values.append(self._prevMeasurements[j][i])

            measurements[i] = self.median(values)
            del values[:]
