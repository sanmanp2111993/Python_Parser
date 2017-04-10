The program is designed to take an xml file as input and perform compression and decompression.
The program takes bookstore.xml which serves as the original input file and takes the file name as an argument.
In accordance the given requirements, the program creates two .xml files to highlight specific compression and decompression.
In order to execute the entire program, kindly give command in the following manner:-
 --> python parser.py bookstore.xml gzip. This commands creates the comprdata.xml which creates a file consisting of compressed data between tags with test=1 value.
 --> python parser.py bookstore.xml gunzip. This command creates the uncomprdata.xml which decompresses the content compressed in the earlier step and presents a clear text data representation.
Kindly, have a look at the comprdata.xml and uncomprdata.xml for viewing the results.
Also multiple temporary files that are being generated during the execution of the program are removed accordingly.
Kindly, process the application by giving the gzip command prior to the gunzip command.
The implementation was compiled and executed on an Ubuntu 16.04 terminal shell tested and edited in an Atom Editor.
The python program is developed for the Python 2.7 version. Kindly, use the same version to execute the script.