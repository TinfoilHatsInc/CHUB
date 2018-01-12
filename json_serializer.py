#!/usr/bin/env python

import storageHandler as sh
import sys
import getopt
import ast

def __usage():
    print("\n\nThis script is used to pass and recieve information from the CHUB frontend and the CHUB itself.\n")
    print("     Argument            Option      Description")
    print("     -h, --help                      Brings up this menu")
    print("     -c, --call                      Retrieves the current status of the CHUB")
    print("     -r, --add_room      <name>      Adds a room to the CHUB along with the <name> as the name of the room")
    print("     -m, --move_mod      'tuple'     Moves the module to given room. 'tuple' must contain (module_id, target_room_id)")
    print("     -u, --update_event  'tuple'     Updates the importance of the event for storing purposes. 'tuple' must contain (event_id, room_id, importance) where importance is a boolean\n\n")


def __main(argv):

    try:
        opts,args = getopt.getopt(argv,'hcr:m:u:',['help','call','add_room=','move_mod=','update_event=','get_armed','set_armed'])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h","--help"):
            __usage()
        elif opt in ("-c","--call"):
            print(sh.send_to_front_end())
        elif opt in ("-r", "--add_room"):
            sh.add_room(arg)
        elif opt in ("-m", "--move_mod"):
            tup = ast.literal_eval(arg)
            #sh.move_module(tup[0],tup[1])
        elif opt in ("-u", "--update_event"):
            tup = ast.literal_eval(arg)
            sh.update_event_status(tup[0],tup[1],tup[2])
        elif opt in ("--get_armed"):
            print(sh.check_armed_status())
        elif opt in ("--set_armed"):
            sh.set_armed_status()
    sys.exit()



if __name__ == "__main__":
    __main(sys.argv[1:])