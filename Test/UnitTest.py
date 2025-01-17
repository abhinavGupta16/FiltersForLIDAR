import sys
sys.path.insert(0, '..')

from numpy.testing import assert_
from src.Helper import calculate_range_filter, calculate_temporal_filter
import src.TemporalFilter
from src.RangeFilter import RangeFilter
import Main


def test_main():
    """
    Test the main() function
    :return: NA
    """
    print("Testing Main")
    Main.main("../files/sample_input.txt", "../files/output.txt")
    output_file = open("../files/output.txt", 'r')
    expected_output_file = open("../files/expected_output.txt", 'r')

    while True:
        output = output_file.readline()[:-1]
        expected_output = expected_output_file.readline()[:-1]
        if not output:
            if expected_output is not None:
                assert_(output == expected_output,
                        generate_error_string(output, expected_output))
            break

        if not expected_output:
            if output is not None:
                assert_(output == expected_output,
                        generate_error_string(output, expected_output))
            break

        assert_(output == expected_output, generate_error_string(expected_output, output))

    output_file.close()
    expected_output_file.close()
    print("Testing Main Success")


def test_range_filter():
    """
    Test the Range Filter for various values
    :return: NA
    """
    print("Testing Range Filter")
    range_filter = RangeFilter()
    measurements = [0.0, 1.0, 2.0, 1.0, 3.0]
    calculate_range_filter(measurements, range_filter)
    assert_(measurements == [0.03, 1.0, 2.0, 1.0, 3.0],
            generate_error_string(measurements, [0.03, 1.0, 2.0, 1.0, 3.0]))

    measurements = [0.0, 1.0, 2.0, 1.0, 100]
    calculate_range_filter(measurements, range_filter)
    assert_(measurements == [0.03, 1.0, 2.0, 1.0, 50],
            generate_error_string(measurements, [0.03, 1.0, 2.0, 1.0, 50]))
    print("Testing Range Filter Success")


def test_temporal_filter():
    """
    Test the Temporal Filter for various values
    :return: NA
    """
    print("Testing Temporal Filter")
    measurements = [0.0, 1.0, 2.0, 1.0, 3.0]
    temporal_filter = src.TemporalFilter.TemporalFilter()
    temporal_filter.d = 0
    calculate_temporal_filter(temporal_filter, measurements)
    assert_(measurements == [0.0, 1.0, 2.0, 1.0, 3.0],
            generate_error_string(measurements, [0.0, 1.0, 2.0, 1.0, 3.0]))

    temporal_filter.d = 3
    measurements = [1, 5, 7, 1, 3]
    calculate_temporal_filter(temporal_filter, measurements)
    assert_(measurements == [0.5, 3.0, 4.5, 1.0, 3.0],
            generate_error_string(measurements, [0.5, 3.0, 4.5, 1.0, 3.0]))

    measurements = [2, 3, 4, 1, 0]
    calculate_temporal_filter(temporal_filter, measurements)
    assert_(measurements == [1.0, 3.0, 4.0, 1.0, 3.0],
            generate_error_string(measurements, [1.0, 3.0, 4.0, 1.0, 3.0]))

    measurements = [3, 3, 3, 1, 3]
    calculate_temporal_filter(temporal_filter, measurements)
    assert_(measurements == [1.5, 3.0, 3.5, 1.0, 3.0],
            generate_error_string(measurements, [1.5, 3.0, 3.5, 1.0, 3.0]))

    measurements = [10, 2, 4, 0, 0]
    calculate_temporal_filter(temporal_filter, measurements)
    assert_(measurements == [2.5, 3.0, 4.0, 1.0, 1.5],
            generate_error_string(measurements, [2.5, 3.0, 4.0, 1.0, 1.5]))

    print("Testing Temporal Filter Success")


def generate_error_string(output, expected_output):
    """
    Generate the error string if test fails
    :param output: generated output
    :param expected_output: expected output
    :return: String
    """
    output = str(output)
    expected_output = str(expected_output)

    if output.strip(' ') == "":
        output = "<Blank>"
    if expected_output.strip(" ") == "":
        expected_output = "<Blank>"
    return "Mismatch, found expected %s but found %s " % (expected_output, output)


def run_all_test():
    """
    Run all test cases
    :return: NA
    """
    test_temporal_filter()
    test_range_filter()
    test_main()


if __name__ == '__main__':
    run_all_test()
