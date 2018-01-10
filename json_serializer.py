#!/usr/bin/env python

import storageHandler as sh
import sys
import getopt

def __usage():
    print("use -c or --call to recieve information and -p:(json) or --push=(json) to add information with the json formated behind the argument")

def __main(argv):
    try:
        opts,args = getopt.getopt(argv,'hcp:',['help','call', 'push='])
    except getopt.GetoptError:
        __usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h","--help"):
            __usage()
            sys.exit()
        elif opt in ("-c","--call"):
            print(sh.send_to_front_end())
        elif opt in ("-p", "--push"):
            sys.exit()


if __name__ == "__main__":
    __main(sys.argv[1:])