#!/usr/bin/env python3
# Author ID: Sandip K C

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    file = open(file_name, 'r')     
    content = file.read()           
    file.close()                    
    return content              

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # return its entire contents as a list of lines without new-line characters
    file = open(file_name, 'r')     
    lines = file.readlines()        
    file.close()                   
    return [line.strip() for line in lines]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))