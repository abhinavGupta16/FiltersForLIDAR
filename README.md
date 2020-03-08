1) The module implements the LIDAR noise filters - Range and Temporal Filter
2) The input is taken via ".txt" file, which ca be easily changed in the future due to the modular design
3) The input file reads the as follows -
    <Type of filter (t/r)>
    <D value>
    <measurements>
    <Type of filter (t/r)>
    <measurements>
    <Type of filter (t/r)>
    <measurements>
    .....
    .....
4) An output file is generated of the output as filtered. This can again be changes easily due to the modular design
5) Output file will contain measurements after filters in each line.
6) Parse errors of the file simply throws an error and stops execution
7) MainTest executes unit testing (100% coverage). All the functions and methods are run and tested.