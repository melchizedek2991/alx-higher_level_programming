#!/usr/bin/python3
if __name__ == '__main__':

    import sys

    argc = len(sys.argv) -1
    if argc == 0;
        print("0")
    elif argc == 1;
        print("1")
    else:
        print("{}".format(argc))
    for index in range(argc):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
