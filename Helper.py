from RangeFilter import RangeFilter


def calculate_range_filter(measurements):
    """
    Calculate the measurements after applying Range Filter
    :param measurements: List of numbers
    :return: NA
    """
    range_filter = RangeFilter()
    range_filter.update(measurements)


def calculate_temporal_filter(temporal_filter, measurements):
    """
    Calculate the measurements after applying Temporal Filter
    :param temporal_filter: TemporalFilter class object
    :param measurements: List of numbers
    :return: NA
    """
    temporal_filter.update(measurements)


def take_list_input_from_file(input_file):
    """
    Reads the measurements inputs from a file and stores it in a list
    :param input_file: file object
    :return: list of float
    """
    measurements = list(map(float, input_file.readline().rstrip('\n').split(' ')))
    return measurements


def choose_filter(argument, temporal_filter, input_file, output_file):
    """
    Takes in the type of filter that needs to be run
    Runs the Range Filter is the input is "r"
    Runs the Temporal Filter is the input is "t"
    Else gives Invalid Input
    :param argument: String (type of filter to be run)
    :param temporal_filter: TemporalFilter class object
    :param input_file: file object (Input File)
    :param output_file: file object (Output File)
    :return: NA
    """
    if argument == "r":
        measurements = take_list_input_from_file(input_file)
        calculate_range_filter(measurements)
    elif argument == "t":
        if temporal_filter.d == -1:
            temporal_filter.d = int(input_file.readline().rstrip('\n'))
        measurements = take_list_input_from_file(input_file)
        calculate_temporal_filter(temporal_filter, measurements)
    else:
        output_file.write("Invalid Input" + '\n')
        return
    output_file.write(str(measurements) + '\n')