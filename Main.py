from Helper import choose_filter
from TemporalFilter import TemporalFilter


def main(input_file_name="files/input.txt", output_file_name="files/output.txt"):
    """
    Main Function drives the whole Program
    LIDAR reads input from a text file
    LIDAR writes the output file values to a text file
    :return: NA
    """
    try:
        temporal_filter = TemporalFilter()
        input_file = open(input_file_name, 'r')
        output_file = open(output_file_name, 'w')

        while True:
            argument = input_file.readline().rstrip('\n')
            if not argument:
                break
            choose_filter(argument, temporal_filter, input_file, output_file)

        input_file.close()
        output_file.close()
    except:
        print("Something went wrong, check the input file")
        raise

if __name__ == "__main__":
    main()
