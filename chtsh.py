from ast import keyword
from distutils.cmd import Command
import os
import sys


# This is our shell command, executed by Popen.


def main():
    # get the Command line arguments and if it equals to -help or -h then print the help message
    if len(sys.argv) == 2:
        if (
            sys.argv[1] == "-help"
            or sys.argv[1] == "-h"
            or sys.argv[1] == "--help"
            or sys.argv[1] == "--h"
        ):
            print(
                f"python chtsh.py -list or --list \t to list all the available cheat sheets in the topic queried\
                \ne.g. \
                \npython chtsh.py -list \
                \nEnter topic: python\
                \nreturns a list of topics for topic\n\
                \npython chtsh.py -search or --search \t to search for a cheat sheet in the topic queried\
                \ne.g. \
                \npython chtsh.py -search \
                \nEnter keyword: python\
                \nreturns cheat sheets for keyword\n\
                \npython chtsh.py -learn or --learn \t to learn a queried cheat sheet\
                \ne.g. \
                \npython chtsh.py -learn \
                \nEnter the topic: python\
                \nreturns a big cheat sheet for learning language from scratch\n\
                \npython chtsh.py\
                \ne.g. \
                \nEnter the topic: python\
                \nEnter the subtopic: functions\
                \nreturns a cheat sheet for subtopic in topic if subtopic is not given it returns a cheatsheet for topic\
                "
            )

        elif sys.argv[1] == "-search" or sys.argv[1] == "--search":
            keyword = input("Enter keyword: ")
            keyword = "~" + "+".join(keyword.split(" "))
            print(keyword)
            os.system(f"curl cht.sh/{keyword}")

        elif sys.argv[1] == "-learn" or sys.argv[1] == "--learn":
            topic = input("Enter the topic: ")
            topic = "~" + "+".join(topic.split(" "))
            os.system(f"curl cht.sh/{topic}/:learn")

        elif sys.argv[1] == "-list" or sys.argv[1] == "--list":
            topic = input("Enter the topic: ")
            topic = "~" + "+".join(topic.split(" "))
            os.system(f"curl cht.sh/{topic}/:list")

    else:
        topic = input("Enter the topic: ")
        if topic:
            topic = "/" + "+".join(topic.split(" "))
        sub_topic = input("Enter the sub: ")
        if sub_topic:
            sub_topic = "/" + "+".join(sub_topic.split(" "))
        os.system(f"curl cht.sh/{topic}{sub_topic}")


if __name__ == "__main__":
    main()
