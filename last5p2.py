#!/usr/bin/env python3

import sys
from tqdm import tqdm

# Python program to demonstrate
# command line arguments
 
import getopt
 
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
 
# Options
options = "hp:s:"
 
# Long options
long_options = ["help", "percent=", "search="]
 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    p=1
    searchString = ""
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print ("use -p for percentage of output and -s for search string")
            sys.exit()
             
        elif currentArgument in ("-p", "--percent"):
            p=currentValue
            
        elif currentArgument in ("-s", "--search"):
            searchString=currentValue
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))


def reverse_file_lines(input_file_path, output_file_path, p, searchString):
    lines = [] # initalize list for lines
    with open(input_file_path, "rb") as fin, open(output_file_path, "wb") as fout:
        lenLines = sum(1 for _ in fin)
        skipLines = round(lenLines*(1-p))
        
        fin.seek(0) # go to first bit and skip first rows (old entries)
        for _ in range(skipLines):
            next(fin)
        
        with tqdm(total=lenLines-skipLines) as pbar:
            if searchString=="":
                for line in fin:
                    lines.append(line) # go through lines and add lines to list
                    pbar.update(1)
                pbar.close()
            else:
                for line in fin:
                    if searchString in str(line):
                        lines.append(line) # go through lines and add lines to list
                    pbar.update(1)
                pbar.close()
        
        fout.writelines(reversed(lines)) # reverse list elements and adds them to new document
        
reverse_file_lines("server.html", "lines.html", float(p), str(searchString))