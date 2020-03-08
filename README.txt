The module implements the LIDAR noise filters - Range and Temporal Filter

1) Run the main function by simply running - "python Main.py" from the root directory
2) Run the Unit Tests by simply running - "python UnitTest.py" from the Test directory
3) The input is taken via ".txt" file, which ca be easily changed in the future due to the modular design
4) The input file reads the as follows -
    <Type of filter (t/r)>
    <D value>
    <measurements>
    <Type of filter (t/r)>
    <measurements>
    <Type of filter (ut/ur)>
    <min max>
    <Type of filter (t/r)>
    <measurements>
    .....
    .....
5) An output file is generated of the output as filtered. This can again be changes easily due to the modular design
6) Output file will contain measurements after filters in each line.
7) Parse errors of the file simply throws an error and stops execution
8) MainTest executes unit testing (100% coverage). All the functions and methods are run and tested.